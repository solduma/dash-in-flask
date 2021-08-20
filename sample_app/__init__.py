# Dash가 탑재된 Flask 앱 시작
from flask import Flask

def init_app():
  # Flask 앱 시작
  app = Flask(__name__, instance_relative_config=False)
  app.config.from_object('config.Config')

  # Dash 앱 탑재
  with app.app_context():
    # 라우트 정보 가져오기
    from sample_app import routes

    # Dash 앱 생성
    from .plotlydash.dashboard import init_dashboard
    app = init_dashboard(app)

    return app
