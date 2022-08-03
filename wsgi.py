# Web Server와 Python Script 간의 통신 인터페이스

from sample_app import init_app

app = init_app()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000, debug=True)
