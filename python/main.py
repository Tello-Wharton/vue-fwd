from flask import Flask, request, Response


import requests
from requests.models import PreparedRequest

app = Flask(__name__)




def forward(path, params):
    req = PreparedRequest()
    url = "http://localhost:3000/" + path
    req.prepare_url(url, params)


    response = requests.get(req.url)

    print(response.encoding)

    return Response(response.content, mimetype=response.headers['content-type'])



@app.route('/<path:path>', methods=['GET', 'POST'])
def all_routes(path):
    return forward(path, request.args.to_dict())

@app.route('/', methods=['GET', 'POST'])
def root_route():
    return forward("", request.args.to_dict())



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)