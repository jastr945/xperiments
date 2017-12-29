from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from project.api.models import Album, Image
from project import db
from sqlalchemy import exc
import datetime


albums_blueprint = Blueprint('albums', __name__)

@albums_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        photos_list = photos.save(request.files['photos'])
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
    post_data = request.get_json()
    if not post_data:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400
    title = post_data.get('title')
    description = post_data.get('description')
    try:
        album = Album.query.filter_by(title=title).first()
        if not album:
            db.session.add(Album(title=title, description=description))
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': f'{title} was added!'
            }
            return jsonify(response_object), 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. That album already exists.'
            }
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
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
                  'images': str(album.images)
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
            'images': [str(i.img) for i in album.images]
        }
        albums_list.append(album_object)
    response_object = {
        'status': 'success',
        'data': {
            'albums': albums_list
        }
    }
    return jsonify(response_object), 200
