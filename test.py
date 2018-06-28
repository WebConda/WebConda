from main import WebConda, render_template

App = WebConda(__name__)

def home():
    return render_template("test.html")

App.route(f=home,route="/")
App.run()