import cgi
import psycopg2
import random

form = cgi.FieldStorage()

# 質問テーブルの質問をselect
conn = psycopg2.connect("dbname=codi user=postgres password=password")
cur = conn.cursor()
cur.execute("select question_id,question from question order by question_id asc")

# #作業用テーブル作成
# # work_conn = psycopg2.connect("dbname=prac user=postgres password=password")
work_cur = conn.cursor()
work_cur.execute("select * from information_schema.tables where table_name=%s", ('work',))
table_exist = bool(work_cur.rowcount)
print(table_exist)

#answerテーブル作成
answer_cur  = conn.cursor()
answer_cur.execute("select student_id,sum(answer) as sum_ans from answer group by student_id order by student_id asc")

# 質問文を変数へ追加
answer_list = []
for answer_row in answer_cur:
    answer_list.append((answer_row[1]))

print(answer_list)
if table_exist == False:
    sql = 'create table work(id SERIAL NOT NULL PRIMARY KEY, sum int)'
    work_cur.execute(sql)
else:
    table_exist = True

action_url = ""


# 質問文を変数へ追加
question_list = []
next_question = 0
for row in cur:
    question_list.append((row[1]))

answer = form.getvalue('answer', '-10')



# 作業用テーブルへ追加
sql_insert = "insert into work(sum) values(" + answer + ")"
work_cur.execute(sql_insert)

sql_select = 'select id,sum from work order by id asc'
work_cur.execute(sql_select)

# 作業用の中身を表示
work_list = []
workid_list = []
for work_row in work_cur:
    work_list.append((work_row[1]))
    workid_list.append((work_row[0]))

work_index = len(workid_list) - 1

que_index = work_index
maina = "-10"

href_url = ""
# 映画の分岐
if que_index == 6:
    if work_list[6] == -10:
        que_index = 16
        # 作業用テーブルへ追加
        for eiga_row in range(10):
            sql_insert = "insert into work(sum) values(" + maina + ")"
            work_cur.execute(sql_insert)
    else:
        print("-10以外！")
#音楽の分岐
if que_index == 17:
    if work_list[17] == -10:
        que_index = 26
        # 作業用テーブルへ追加
        for eiga_row in range(9):
            sql_insert = "insert into work(sum) values(" + maina + ")"
            work_cur.execute(sql_insert)
    else:
        print("-10以外！")
#ゲームの分岐
if que_index == 27:
    if work_list[27] == -10:
        que_index = 33
        # 作業用テーブルへ追加
        for eiga_row in range(6):
            sql_insert = "insert into work(sum) values(" + maina + ")"
            work_cur.execute(sql_insert)
    else:
        print("-10以外！")
#スポーツの分岐
if que_index == 34:
    if work_list[34] == -10:
        que_index = 46
        # 作業用テーブルへ追加
        for eiga_row in range(12):
            sql_insert = "insert into work(sum) values(" + maina + ")"
            work_cur.execute(sql_insert)
    else:
        print("-10以外！")
print(question_list[57])
#ラーメンの分岐
if que_index == 47:
    if work_list[47] == -10:
        que_index = 58
        # 作業用テーブルへ追加
        for eiga_row in range(5):
            sql_insert = "insert into work(sum) values(" + maina + ")"
            work_cur.execute(sql_insert)
    else:
        print("-10以外！")
#旅行の分岐
if que_index == 53:
    if work_list[53] == -10:
        action_url = 'n.py'
        # href_url = "localhost.href='/aaa/index.html'"
        # 作業用テーブルへ追加
        for eiga_row in range(6):
            sql_insert = "insert into work(sum) values(" + maina + ")"
            work_cur.execute(sql_insert)
if que_index == 57 :
        action_url = 'n.py'
        # href_url = "localhost.href='/aaa/index.html'"

work_sum = 0

for work_test in work_list:
    work_sum = work_test + work_sum

# que = random.choice(question_list)
que = question_list[que_index]

print(work_list)
print(len(workid_list) - 1)
print(next_question)
print(work_sum - work_list[0])

print("Content-Type: text/html; charset=utf-8")
print("""
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8" />
	<title>コーディネイター - 入力フォーム</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous" />

	<link rel="stylesheet" type="text/css" href="../css/form.css">

</head>
<body>

<div class="move">
	<h2 class="question_title">cody's question!</h2>
	<div>test</div>
</div>

<div class="flex">
	<div class="ido">
			<div class="question_box">
    		<p id="question_text" class="text-monospace">{que}</p>
			</div>
            <form method="POST" action="{action_url}">
			<div class="question_btn">
				<button class="yes_btn" value="10" name="answer" onclick="{href_url}">はい</button>
				<button class="no_btn" value="-10" name="answer" onclick="{href_url}">いいえ</button>
			</div>

			<div class="btn-group dropright">
				  <button type="button " class="btn btn-secondary dropdown-toggle bg-white text-dark" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				    その他
				  </button>
				<div class="dropdown-menu" x-placement="right-start" style="position: absolute; transform:translate3d(111px, 0px, 0px); top: 0px; left: 0px; will-change: transform;">
 			 		<button class="dropdown-item" href="#" value="5" name="answer">多分はい</button>
  		    		<button class="dropdown-item" href="#" value="0" name="answer">分からない</button>
  		    		<button class="dropdown-item" href="#" value="-5" name="answer">多分いいえ</button>
  			    </div>

			</div>
		    </form>


		</div>
		<img class="form_image" src="../css/12.png">
</div>



<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
//ボタンにより数値を取得、コンソールに表示  
<script>
 console.log({answer})
</script>
""".format(que=que, answer=answer,action_url=action_url,href_url=href_url))

# <script>
# 			var que_array = ['１年生ですか？','2年生ですか？','高度職業実践科ですか？','webCGクリエイターコースですか？','アプリ開発コースですか？','音楽をよく聞きますか？'];
#
# 			var random = Math.floor(Math.random() * que_array.length	);
#
# 			console.log(que_array[0]);
# 			document.getElementById('question_text').innerHTML = que_array[random];
#
# </script>
# </body>
# </html>

conn.commit()