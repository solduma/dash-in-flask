# Dash 앱 생성과 관련된 스크립트
import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from .data import create_dataframe
from .layout import html_layout

def init_dashboard(server):
  # Plotly Dash 대시보드 생성
  dash_app = dash.Dash(
    server=server,
    routes_pathname_prefix='/dashapp/',
    external_stylesheets=[
      '/static/dist/css/styles.css',
    ]
  )

  # 빈 DataFrame 생성
  df = create_dataframe()

  # Custom HTML layout
  dash_app.index_string = html_layout

  # Create Layout
  dash_app.layout = html.Div(
    children=[dcc.Graph(
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
      }),
      create_data_table(df)
    ],
    id='dash-container'
  )
  return dash_app.server


def create_data_table(df):
  # Pandas 데이터프레임으로 부터 Dash 데이터테이블 생성
  table = dash_table.DataTable(
    id='database-table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    sort_action="native",
    sort_mode='native',
    page_size=300
  )
  return table