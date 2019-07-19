import cgi
import psycopg2
form = cgi.FieldStorage()

conn = psycopg2.connect("dbname=codi user=postgres password=password")
work_cur = conn.cursor()
work_cur.execute("select * from information_schema.tables where table_name=%s", ('work',))
table_exist = bool(work_cur.rowcount)
print(table_exist)

# 作業用を変数へ追加
work_list = []
work_cur.execute("select * from work")

for work_row in work_cur:
    work_list.append((work_row[1]))

print(work_list)

work_sum = 0

for work_test in work_list:
    work_sum = work_test + work_sum

print(work_sum)
work = str(work_sum)

ans_curr= conn.cursor()
ans_curr.execute("select student_id,sum(answer) as ansum from answer group by student_id having sum(answer)="+work+";")

ans_list=[]

for ans_row in ans_curr:
    ans_list.append((ans_row[0]))

ans_len = len(ans_list)

stu_curr = conn.cursor()

stu_list=[]
for stu_row in range(ans_len):
    str_row = str(stu_row)
    stu_curr.execute("select name from student where student_id="+str_row+"")
    stu_row2 = stu_curr
    stu_list.append(stu_row2)

print(stu_list)
stu_div = stu_list
print(ans_list)
if table_exist == True:
  print(table_exist)
  sql = 'drop table work'
  work_cur.execute(sql)
else:
  table_exist = False

print("Content-Type: text/html; charset=utf-8")
print("""
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
        サンプルページ
    </title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>


<body style="width: 100%; background-color: #eee; background-image : url( );
background-image : url(../css/あきあき.png);">

    <div class="d-flex justify-content-center">
    
        <div class="w-75" style="margin-left:150px;margin-top: 50px; margin-bottom: 50px;  width: 1200px; height: 180px; background-color: #fee; border: 1px solid #333333;">
        
            <div>{stu_div}</div>
            
        </div>
        
    </div>
    
    <br />
    <div>
    
        <div class="d-flex w-100" style="margin-left: 600px;">
            <div class="d-flex justify-content-center">
                <img class="rounded-0" src="../css/300x300.png" alt="" style="border: 1px solid #333333;"></img>
            </div>
        <div style="margin-left: 100px;">
        <form method="POST" action="top_index.py">
            <button type="submit" class="btn btn-outline-danger" style="margin-left: 80px; background-color: #faa; margin-top: 150px; width: 180px; height: 80px;">イエス</button>
            <br />
            <button type="submit" class="btn btn-outline-success" style="background-color: #afa; margin-top: 30px; width: 360px; height: 80px;">違います</button>
        </form>
        </div>
        </div>



    </div>
       
             



<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>

</html>
""".format(stu_div=stu_div))
#こだまさく
conn.commit()
