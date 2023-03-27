import pymysql
from config import load_config

config = load_config()
con = pymysql.connect(host=config.db.host, user=config.db.user,
                       password=config.db.password, db=config.db.database)
cursor=con.cursor()
cursor.execute(
    'SELECT students.name, courses.name,grades.grade FROM grades LEFT JOIN students ON grades.user_id = students.id '
    'LEFT JOIN courses ON grades.courses_id = courses.id WHERE grades.grade > 90'
)
grade = cursor.fetchall()
print(grade)


con.close()

from chanel_control.models import Grades
grades = Grades.objects.filter(grade__gt=90).select_related('user', 'courses')
for grade in grades:
    print(grade.grade, grade.user.name, grade.courses.name)