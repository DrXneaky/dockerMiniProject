import sys
#sys.path.append("C:/Users/Ahmed/Desktop/dockerMiniProject/flask")
from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
  return "Index page of docker flask application"

if __name__ == "__main__":
  app.run()

