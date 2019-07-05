import cgi
import psycopg2
import random
form = cgi.FieldStorage()

question_list = ["一年生ですか？","二年生ですか？"]

que = random.choice(question_list)


answer = form.getvalue('answer','')


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
</div>

<div class="flex">
	<div class="ido">
			<div class="question_box">
    		<p id="question_text">{que}</p>
			</div>
            <form method="POST" action="">
			<div class="question_btn">
				<button type="submit" class="yes_btn" value="10" name="answer">はい</button>
				<button type="submit" class="no_btn" value="-10" name="answer">いいえ</button>
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
""".format(que=que,answer=answer))

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


