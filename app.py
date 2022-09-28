import json
from os import environ, path
from bottle import error, route, run, template


data_file = "combined_data.json"


@route("/")
def index():
    data = []
    filePath = path.join(path.dirname(__file__), data_file)
    with open(filePath, mode="r", encoding="utf8") as f:
        data = json.loads(f.read())
    return template("index", data=data)


@error(404)
def error404(error):
    return "Nothing here, sorry!"


if __name__ == "__main__":
    if environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8000, reloader=True, debug=True)
