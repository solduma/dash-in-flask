# Layout 오버라이드

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%css%}
        </head>
        <body class="dash-template">
            <header>
                <h1 style="margin-left:10px">Dash in Flask 샘플 화면입니다</h1>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""
