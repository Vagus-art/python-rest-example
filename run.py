from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/methods', methods=["POST","GET"])
def methodsHandler():
    if request.method == "POST":
        return "posted"
    elif request.method == "GET":
        return "getted"
    else:
        return "not posted nor getted"

@app.route('/echo/<var>')
def echoesHandler(var=''):
    return f"You wrote {var}!"