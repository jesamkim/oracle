# 사전에 Oracle Instantclient 19.5 버전 rpm 설치 필요
# sudo python3 -m pip install cx_Oracle --upgrade   수행 필요

import cx_Oracle
import os

# ADW Wallet zip 파일을 unzip 한 디렉토리
os.environ['TNS_ADMIN'] = "/usr/lib/oracle/19.5/client64/lib/network/admin"

p_username = 'ADMIN'
p_password = 'Welcomeoracle1'
p_service = 'madbrosdb_low'
con = cx_Oracle.connect(p_username, p_password, p_service)

print(con)
print(con.version)  # ADW 버전은 19.5

cur = con.cursor()

## 쿼리 테스트
sql = "select * from CAMP_SITE where rownum < 10"
cur.execute(sql)

results = []

for row in cur.fetchall():
    results.append(row)

print(results)

con.close()
