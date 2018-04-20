from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {
        'id': 1,
        'title': u'muesli',
        'note': u'with nuts and raisins',
        'done': False
    },
    {
        'id': 2,
        'title': u'cat food',
        'note': u'',
        'done': False
    }
]

@app.route('/api/v1.0/items', methods=['GET'])
def get_tasks():
    return jsonify({'items': items})


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
