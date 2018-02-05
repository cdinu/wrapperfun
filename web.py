from somedudessklearn import predict
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Fake sklearn here. Use /user/event to get what you want'

@app.route('/<user>/<event>')
def predict_wrapper(user, event):
    return predict(user, event)

if __name__ == '__main__':
    app.run(debug=True)
