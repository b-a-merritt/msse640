from flask import Flask, abort, render_template_string
from werkzeug.middleware.proxy_fix import ProxyFix


application = Flask(__name__)
application.wsgi_app = ProxyFix(
    application.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


@application.route("/")
def main_page():
    return """
        <body>
            <h1>Main page</h1>
            <p>This is the main page</p>
        </body>
    """


@application.route("/expensive/<int:num_items>")
def expensive_page(num_items: int):
    template = """
    <!doctype html>
    <html>
        <body>
            <h1>Expensive page</h1>
            {% for item in items %}
                <p>Item #{{ item + 1 }}</p>
            {% endfor %}
        </body>
    </html>
    """

    if num_items < 0:
        abort(400, description='Number of items cannot be negative')
    if num_items > 500:
        abort(400, description="Number of items cannot be greater than 500")

    items = []

    for i in range(num_items):
        item_num = i
        for _ in range(num_items):
            for k in range(num_items):
                item_num = i * k
        items.append(item_num)

    return render_template_string(template, items=range(0, num_items))


@application.errorhandler(404)
def page_not_found(error):
    return "<p>404, Page not found!</P>", 404
