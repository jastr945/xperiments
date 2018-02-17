from flask import Flask, jsonify
from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for
from project.api.models import Album, Image
from project import db
from sqlalchemy import exc
import datetime
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_oauthlib.client import OAuth
from flask_cors import CORS

# creating an instance of an app and configuring Flask-Uploads
app = Flask(__name__)
CORS(app)
app.config['UPLOADED_PHOTOS_DEST'] = 'static'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app, 32 * 1024 * 1024) # limits uploaded images to 32 megabytes

# login with Google
GOOGLE_CLIENT_ID = '418257197191-lpv9abrospnd232fbbaup896fvngikk6.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'xeWXWVM6CQdXUopgt-oTACeJ'
oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key=GOOGLE_CLIENT_ID,
    consumer_secret=GOOGLE_CLIENT_SECRET,
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

# creating a blueprint
albums_blueprint = Blueprint('albums', __name__)


@albums_blueprint.route('/', methods=['GET', 'POST'])
def index():
    albums = Album.query.order_by(Album.created_at.desc()).all()
    # Google authorization
    if 'google_token' in session:
        me = google.get('userinfo')
        return jsonify({"data": me.data})
    return redirect(url_for('albums.login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        album = Album(title=title, description=description)
        album.images = photos_list
        db.session.add(album)
        db.session.commit()
    return render_template('index.html', albums=albums)

@albums_blueprint.route('/login')
def login():
    return google.authorize(callback=url_for('albums.authorized', _external=True))

@albums_blueprint.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('albums.index'))

@albums_blueprint.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    return redirect("url_for('albums.index')")

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

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
            new_album = Album(title=title, description=description)
            new_album.images=[]
            for i in request.files.getlist('photos'):
                filename = photos.save(i) # saving images via Flask-Uploads
                img_url = photos.url(filename) # extracting image url with Flask-Uploads
                new_image = Image(name=filename, url=img_url)
                new_album.images.append(new_image) # One-to-many relationship instantiation
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
