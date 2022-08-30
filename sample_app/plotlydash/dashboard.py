# Dash 앱 생성과 관련된 스크립트
from dash import dash_table
from dash import Dash
from dash import html
from dash import dcc
from .data import create_dataframe
from .layout import html_layout


# Plotly Dash 대시보드 생성
def init_dashboard(server):
  dash_app = Dash(
    server=server,
    routes_pathname_prefix='/dashApp/',
    external_stylesheets=[
      '/static/dist/css/styles.css',
    ]
  )

  # 빈 DataFrame 생성
  df = create_dataframe()

  # HTML 레이아웃 템플릿 불러오기
  dash_app.index_string = html_layout

  # 레이아웃 생성 및 내용
  dash_app.layout = html.Div(
    children=[
      create_historgram(df),
      create_data_table(df)
    ],
    id='dash-container'
  )
  return dash_app.server


# 대시보드에 들어갈 히스토그램 컴포넌트 생성
def create_historgram(df):
  graph = dcc.Graph(
    id='histogram-graph',
    figure={
      'data': [{
        'x': df['Species'],
        'text': df['Species'],
        'customdata': df['Id'],
        'name': '# Data',
        'type': 'histogram'
      }],
      'layout': {
        'title': '# of Data per Species',
        'height': 500,
        'padding': 150
      }
    })
  return graph


# 대시보드에 들어갈 데이터테이블 컴포넌트 생성
def create_data_table(df):
  table = dash_table.DataTable(
    id='database-table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    sort_action="native",
    sort_mode='native',
    page_size=300
  )
  return table