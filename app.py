from flask import Flask
from eremiza import Client
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["*"])

client = Client("", "")


@app.route('/alarmy', methods=["GET"])
def get_alarms():
    output = client.get_alarms(count=15, offset=0)
    return output


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6900)
