from flask import Flask

application = app = Flask(__name__)

@application.route("/")
def index():
    return "<p><font color=brown>Hello Oleksii Saiun.version2</font></p>"

if __name__ == "__main__":
    application.debug = True
    application.run()