from flask import Blueprint, jsonify, request, render_template, redirect
from project.api.models import Album, Image
from project import db
from sqlalchemy import exc
import datetime
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask import Flask, jsonify


# creating an instance of an app and configuring Flask-Uploads
app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = 'static'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# creating a blueprint
albums_blueprint = Blueprint('albums', __name__)


@albums_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        album = Album(title=title, description=description)
        album.images = photos_list
        db.session.add(album)
        db.session.commit()
    albums = Album.query.order_by(Album.created_at.desc()).all()
    return render_template('index.html', albums=albums)

@albums_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'kittykats!'
    })

@albums_blueprint.route('/albums', methods=['POST'])
def add_album():
    post_data = request.form
    if not post_data:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400

    title = request.form['title']
    try:
        album = Album.query.filter_by(title=title).first()
        if not album:
            description = request.form['description']
            filename = photos.save(request.files['photos'])
            img_url = photos.url(filename) # saving images via Flask-Uploads
            new_image = Image(name=filename, url=img_url)
            new_album = Album(title=title, description=description)
            new_album.images=[new_image] # One-to-many relationship instantiation
            db.session.add(new_album)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': f'{title} was added!'
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. That title already exists.'
            }
            return jsonify(response_object), 400
    except (exc.IntegrityError, ValueError) as e:
        db.session().rollback()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400

@albums_blueprint.route('/albums/<album_id>', methods=['GET'])
def get_single_album(album_id):
    """Get single album details"""
    response_object = {
        'status': 'fail',
        'message': 'Album does not exist'
    }
    try:
        album = Album.query.filter_by(id=int(album_id)).first()
        if not album:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                  'title': album.title,
                  'description': album.description,
                  'created_at': album.created_at.isoformat(),
                  'images': [str(i.url) for i in album.images] # sending image url to React
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404

@albums_blueprint.route('/albums', methods=['GET'])
def get_all_albums():
    """Get all albums"""
    albums = Album.query.order_by(Album.created_at.desc()).all()
    albums_list = []
    for album in albums:
        album_object = {
            'id': album.id,
            'title': album.title,
            'description': album.description,
            'created_at': album.created_at.isoformat(),
            'images': [str(i.url) for i in album.images] # sending image url to React
        }
        albums_list.append(album_object)
    response_object = {
        'status': 'success',
        'data': {
            'albums': albums_list
        }
    }
    return jsonify(response_object), 200
