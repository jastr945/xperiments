import os
from flask import Flask, jsonify, abort, make_response, request, render_template, redirect, url_for, g, session
from flask_httpauth import HTTPBasicAuth
import flask_login
from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from models import db, Item, User


app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "shopping.db"))
app.config['SECRET_KEY'] = 'ahfeireibuungohl7ePhmooboozaibei1AeNiepedow5eeRoh2EePh5Ailas'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
auth = HTTPBasicAuth()
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@app.cli.command()
def initdb():
    """Initialize the database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@auth.error_handler
def unauthorized():
    """Handling unauthorized access"""
    return make_response(jsonify({'error': 'Access denied'}), 403)


@app.errorhandler(404)
def not_found(error):
    """Handling 404 nicely"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/api/v1.0/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })


@app.route('/api/v1.0/login', methods=['POST'])
@auth.verify_password
def verify_password():
    # # first try to authenticate by token
    # user = User.verify_auth_token(username_or_token)
    # if not user:
        # try to authenticate with username/password
    user = User.query.filter_by(name=request.form['username']).first()
    if not user or not user.verify_password(request.form['password']):
        response_object = {
            'status': 'fail',
            'message': 'Login failed.'
        }
        return jsonify(response_object), 400
    flask_login.login_user(user)
    response_object = {
        'status': 'success',
        'message':  'User {} logged in!'.format(user.name)
    }
    return jsonify(response_object), 200


@app.route('/api/v1.0/logout')
def logout():
    flask_login.logout_user()
    response_object = {
        'status': 'success',
        'message':  'User logged out!'
    }
    return jsonify(response_object), 200


@app.route('/api/v1.0/users', methods=['GET'])
def get_users():
    """Listing all users"""
    users = User.query.all()
    users_list = []
    for user in users:
        user_object = {
            'id': user.id,
            'name': user.name,
            'password': user.password_hash,
        }
        users_list.append(user_object)
    response_object = {
        'status': 'success',
        'data': {
            'users': users_list
        }
    }
    return jsonify(response_object), 200


@app.route('/api/v1.0/signup', methods=['POST'])
def signup():
    """Creating a new user"""
    error = None
    if not request.json and not request.form:
        abort(400)
    # for curl command
    if request.json:
        if 'name' in request.json and type(request.json['name']) != unicode:
            abort(400)
        name = request.json['name']
        samename = User.query.filter_by(name=name).first()
        if not samename:
            password = request.json['password']
            new_user = User(name=name)
            new_user.hash_password(password)
            db.session.add(new_user)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message':  'New user {} was added!'.format(newname)
            }
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. This name is already taken.'
            }
            return jsonify(response_object), 400
    # for JavaScript Client
    if request.form:
        newname = request.form['newname']
        samename = User.query.filter_by(name=newname).first()
        if not samename:
            newpassword = request.form['newpassword']
            new_user = User(name=newname)
            new_user.hash_password(newpassword)
            db.session.add(new_user)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'New user {} was added!'.format(newname)
            }
            return redirect(url_for('index'))
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. This name is already taken.'
            }
            return jsonify(response_object), 400
    return jsonify(response_object), 200


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
                    'data': {
                        'title': title,
                        'note': note
                    }
                }
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

    if current_user.is_authenticated:
        user = current_user.name
    else:
        user=None
    items = Item.query.all()
    return render_template('index.html', items=items, user=user)


if __name__ == "__main__":
    app.run(debug=True)
