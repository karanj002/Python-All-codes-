import pymysql

conn=pymysql.connect(host='local',user='demo',password='demo1234',db='contacts')
a=conn.cursor()
sql='select * from `form`;'
a.execute(sql)
countrow=a.execute(sql)
print('no of rows : ',countrow)
data=a.fetchone()
print(data)
