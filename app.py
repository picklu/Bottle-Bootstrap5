import json
from os import environ, path
from math import ceil
from bottle import error, route, run, template
from data import get_data

articles_per_page = 10
data = get_data()
total_articles = len(data)


@route("/")
@route("/<page:int>")
def index(page=1):
    start_page = 1
    end_page = ceil(total_articles / articles_per_page)
    articles = data[(page - 1) * articles_per_page:page * articles_per_page]
    return template("index",
                    page=page,
                    start_page=start_page,
                    end_page=end_page,
                    base_index=(page - 1) * articles_per_page,
                    articles_per_page=articles_per_page,
                    total_articles=total_articles,
                    articles=articles)


@error(404)
def error404(error):
    return "Nothing here, sorry!"


if __name__ == "__main__":
    if environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8000, reloader=True, debug=True)
