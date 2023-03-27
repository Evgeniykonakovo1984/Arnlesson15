import json
import datetime
import pymysql
from config import load_config

with open('fake-data.json') as json_file:
    data = json.load(json_file)



config = load_config()
con = pymysql.connect(host=config.db.host, user=config.db.user,
                       password=config.db.password, db=config.db.database)
cursor=con.cursor()
for item in data:
    name = item['name']
    age = item['age']
    email = item['email']
    is_enrolled = item['is_enrolled']
    registered_at = item['registered_at']
    print(type(registered_at))
    date_time_obj = datetime.datetime.strptime(registered_at, '%Y-%m-%dT%H:%M:%SZ')
    print(type(date_time_obj))
    print(date_time_obj)
    cursor.execute(
        'INSERT INTO students (name, age, email, is_enrolled, registered_at) '
        'VALUES(%s, %s, %s, %s, %s)', (name, age, email, is_enrolled, date_time_obj)
    )
    con.commit()

x=[]
sum=[]
i=0
for txt in data:
    print(txt['grades'])
    x.append(list(txt['grades'].keys()))
    print(x)
    sum = sum + x[i]
    print(sum)
    i=i+1
print(sum)
#sum_clean=[]
for txt in sum:
    if sum.count(txt) > 1:
        sum.remove(txt)
print(sum)
for txt in sum:
    cursor=con.cursor()
    cursor.execute('INSERT INTO courses (name) VALUES(%s)', (txt))
    con.commit()
i=0
j=0
grades=[]
key=[]
value=[]
for txt in data:
    key.append(list(txt['grades'].keys()))
    value.append(list(txt['grades'].values()))
    print(key[0][0])
    print(value[0][0])
    count=len(key[0])
    for txt in key[0]:
        n = sum.index(txt)+1
        val=value[0][j]
        grades.append([i+1, n, val])
        j= j+1
    key.clear()
    value.clear()
    j=0
    i=i+1
print(grades)

for txt in grades:
    cursor=con.cursor()
    cursor.execute(
                   'INSERT INTO grades (user_id, courses_id, grade) VALUES (%s, %s, %s)',
                    (int(txt[0]), int(txt[1]), int(txt[2]))
    )
    con.commit()

con.close()
