# 웹 요청에 대한 라우터
from flask import redirect
from flask import current_app as app


# 메인 URI에 들어오는 요청에 대한 답변 - 대시 어플리케이션 페이지로 리다이렉트
@app.route('/')
def home():
  return redirect("/dashApp", code=302)