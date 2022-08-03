# Dash-in-Flask
Flask를 웹서버로 사용하는 Plotly Dash 대시보드 샘플 코드입니다.

## 실행법
1. $ pip install -r requirements.txt
2. $ python wsgi.py
3. localhost:3000 으로 접속

## 파일 구조
dash-inflask\
ㄴdata                    - 데이터를 저장하는 폴더입니다.\
  ㄴIris.csv              - Iris 데이터를 사용했습니다.\
ㄴsample_app              - 프론트\
  ㄴplotlydash            - Dash 어플리케이션에 관한 폴더입니다.\
    ㄴdashboard.py        - 대시보드를 생성하기 위한 파일입니다.\
    ㄴdata.py             - 대시보드에 들어갈 데이터 로드 및 전처리를 위한 파일입니다.\
    ㄴlayout.py           - 대시보드 화면 레이아웃을 오버라이드합니다.\
  ㄴstatic                - 정적인 asset들을 보관하기 위한 폴더입니다. CSS 파일을 저장하기 위해서만 사용 했습니다.\
  ㄴ__init__.py           - Flask와 Dash를 구동하고 Flask에 Dash를 탑재 시키는 파일입니다.\
  ㄴroutes.py             - 웹 URI 접근에 대한 라우팅 정보를 담고 있는 파일입니다. 페이지가 하나인 관계로 리다이렉팅에만 사용 했습니다.\
ㄴconfig.py               - Flask 환경설정 파일입니다.\
ㄴwsgi.py                 - Web Server와 Python Script 간의 통신 인터페이스입니다.

## 실행 순서
2. wsgi.py                - 웹-앱 인터페이스 생성                                                     ->  2번
2. __init__.py            - Flask 앱 구동\
                          - Dash 앱 탑재\
                            - Route 정보 추가                                                        -> 3번\
                            - 대시보드 탑재                                                          -> 4번
3. routes.py              - URI로 들어오는 접근에 대한 라우팅 정보 정의\
                            - '0.0.0.0:3000/'에 대한 접근을 '0.0.0.0:3000/dashApp/'으로 리다이렉팅
4. dashboard.py           - 대시보드 생성\
                            - 데이터 로드                                                            -> 5번\
                            - 레이아웃 템플릿 로드                                                    -> 6번\
                            - Dash 대시보드 레이아웃 및 시각화 컴포넌트 배치
5. data.py                - 데이터 전처리 및 서빙
6. layout.py              - HTML 화면 및 스타일 정의
