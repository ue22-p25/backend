"""
the flask version of the cookie example

this app sets a cookie in the browser called 'visit'
that tracks the number of times the user has visited the page.
"""

from flask import Flask, request, make_response

app = Flask(__name__)

# this is the way to catch all routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def serve_with_cookie(path):
    """
    display the number of times the page has been visited
    """

    cookies = request.cookies
    # does the client cookies have a 'visit' field ?
    if 'visit' in cookies:
        visit = int(cookies['visit']) + 1
    else:
        visit = 0

    # the text to display
    if visit == 0:
        html = f"<h1>Welcome for your first time here !</h1>"
    else:
        html = f"<h1>You have seen this page {visit} times !</h1>"
    html += f"this is the flask version - you were visiting path /<code>{path}</code> !"

    # build a response
    response = make_response(html)
    # set the cookie - this will end up in the browser cookie store
    # and from then on, it will automatically send it back to the server
    # on each request to the same domain
    response.set_cookie('visit', str(visit))

    return response
