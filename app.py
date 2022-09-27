import platform
from bottle import error, route, run, template
from data import get_data


@route("/")
def index():
    data = get_data("combined_data.json")
    return template("index", data=data)


@error(404)
def error404(error):
    return "Nothing here, sorry!"


if __name__ == "__main__":
    if platform.system() == "Linux":
        run(host="localhost", port=5000, reloader=True, debug=True)
    elif platform.system() == "Windows":
        run(host="localhost", port=8000, reloader=True, debug=True)