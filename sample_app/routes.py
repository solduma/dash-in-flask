# 웹 요청에 대한 라우터
from flask import render_template
from flask import current_app as app


# 메인 URI에 들어오는 요청에 대한 답변 - 랜딩페이지 렌더링
@app.route('/')
def home():
  return render_template(
    'index.jinja2',
    title='홈 화면입니다',
    template='home-template',
    body="This is a homepage served with Flask."
  )
