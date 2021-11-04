from flask import jsonify

from pyms.flask.app import Microservice

ms = Microservice() 
app = ms.create_app() 


@app.route("/") 
def example():
    return jsonify({"main": "Hello, Yellow taxi"})


if __name__ == '__main__':
    app.run()