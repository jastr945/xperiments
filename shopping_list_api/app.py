import os
from flask import Flask, jsonify, abort, make_response, request, render_template, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from models import db, Item


app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "shopping.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
auth = HTTPBasicAuth()


@app.cli.command()
def initdb():
    """Initialize the database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@auth.get_password
def get_password(username):
    if username == 'polina':
        return 'kittykat'
    return None


@auth.error_handler
def unauthorized():
    """Handling unauthorized access"""
    return make_response(jsonify({'error': 'Access denied'}), 403)


@app.errorhandler(404)
def not_found(error):
    """Handling 404 nicely"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    """Listing all items"""
    items = Item.query.all()
    items_list = []
    for item in items:
        item_object = {
            'id': item.id,
            'title': item.title,
            'note': item.note,
        }
        items_list.append(item_object)
    response_object = {
        'status': 'success',
        'data': {
            'items': items_list
        }
    }
    return jsonify(response_object), 200


@app.route('/api/v1.0/items', methods=['POST'])
def add_item():
    """Adding an item to the list"""
    if not request.json and not request.form:
        abort(400)
    # for curl command
    if request.json:
        if 'title' not in request.json:
            abort(400)
        if 'title' in request.json and type(request.json['title']) != unicode:
            abort(400)
        if 'note' in request.json and type(request.json['note']) is not unicode:
            abort(400)
        title = request.json['title']
        note = request.json.get('note', "")
        new_item = Item(title=title, note=note)
        db.session.add(new_item)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Item was added!'
        }
    # for JavaScript Client
    if request.form:
        title = request.form['title']
        note = request.form['note']
        new_item = Item(title=title, note=note)
        db.session.add(new_item)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Item was added!'
        }
        return redirect(url_for('index'))
    return jsonify(response_object), 201


@app.route('/api/v1.0/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Getting a single item"""
    try:
        item = Item.query.filter_by(id=item_id).first()
        if not item:
            abort(404)
        else:
            response_object = {
                'status': 'success',
                'data': {
                  'id': item.id,
                  'title': item.title,
                  'note': item.note,
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        abort(400)


@app.route('/api/v1.0/items/<int:item_id>', methods=['PUT'])
# @auth.login_required
def update_item(item_id):
    """Updating a single item"""
    try:
        item = Item.query.filter_by(id=item_id).first()
        if not item:
            abort(404)
        else:
            # for curl command
            if request.json:
                if 'title' not in request.json:
                    abort(400)
                if 'title' in request.json and type(request.json['title']) != unicode:
                    abort(400)
                if 'note' in request.json and type(request.json['note']) is not unicode:
                    abort(400)
                title = request.json['title']
                note = request.json.get('note', "")
                item.title = title
                item.note = note
                db.session.commit()
                response_object = {
                    'status': 'success',
                    'message': 'Item was updated!'
                }
            # for JavaScript Client
            if request.form:
                title = request.form['title']
                note = request.form['note']
                item.title = title
                item.note = note
                db.session.commit()
                response_object = {
                    'status': 'success',
                    'message': 'Item was updated!'
                }
                return redirect(url_for('index'))
    except ValueError:
        abort(400)
    return jsonify(response_object), 200


@app.route('/api/v1.0/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Deleting a single item"""
    try:
        item = Item.query.filter_by(id=item_id).first()
        if not item:
            abort(404)
        else:
            db.session.delete(item)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Item was deleted!'
            }
    except ValueError:
        abort(400)
    return jsonify(response_object), 204


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page view"""
    items = Item.query.all()
    return render_template('index.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)
