import cgi
import psycopg2

work_conn = psycopg2.connect("dbname=codi user=postgres password=password")
work_cur = work_conn.cursor()
work_cur.execute("select * from information_schema.tables where table_name=%s", ('work',))
table_exist = bool(work_cur.rowcount)
print(table_exist)

if table_exist == True:
  print(table_exist)
  sql = 'drop table work'
  work_cur.execute(sql)
else:
  table_exist = False


form = cgi.FieldStorage()

print("Content-Type: text/html; charset=utf-8")
print("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="sample.css" type="text/css">
  </head>
  <body>
    <p class="sample1">学生のことならな～んでも知ってます～！</p>
		<p class="sample1">test_umi！</p>
		<button class="shadow">トップへ</button>
  </body>
</html>""")

work_conn.commit()