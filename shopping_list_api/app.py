from flask import Flask, jsonify, abort, make_response, request

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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})


@app.route('/api/v1.0/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})


@app.route('/api/v1.0/items', methods=['POST'])
def add_item():
    if not request.json or not 'title' in request.json:
        abort(400)
    item = {
        'id': items[-1]['id'] + 1,
        'title': request.json['title'],
        'note': request.json.get('note', ""),
        'done': False
    }
    items.append(item)
    return jsonify({'item': item}), 201


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
