from sanic import Sanic
from sanic import response

from htmlx.tags import html, head, body, script, button, div
from htmlx.dom import DocumentFragment

app = Sanic(name="htmxtest")

page = html(
    head(
        # DocumentFragment(
            """
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="../../favicon.ico">
        <title>HTMX Test</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
        <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>        
        """,
        # ),
        script(_src="https://unpkg.com/htmx.org@1.5.0"),
    ),
    body(
        button(
            "Do something",
            **{"_data-hx-post": "/clicked"},
            **{"_data-hx-swap": "outerHTML"},
        ),
        button(
            "Do something",
            **{"_data-hx-post": "/clicked"},
            **{"_data-hx-swap": "outerHTML"},
        ),
        button(
            "Do something",
            **{"_data-hx-post": "/clicked"},
            **{"_data-hx-swap": "outerHTML"},
        ),
    ),
)


@app.route("/")
async def home(request):
    return response.html(f"{page}")


@app.route("/clicked", methods=["POST", "GET"])
async def clicked(request):
    return response.html(f'{div("Button was replaced")}')


app.run(host="0.0.0.0", port=8000)
