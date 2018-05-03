import os
import unittest
from unittest import TestCase
from app import app
from models import db, User


class BasicTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        project_dir = os.path.dirname(os.path.abspath(__file__))
        database_file = "sqlite:///{}".format(os.path.join(project_dir, "test.db"))
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        myuser = User.query.filter_by(id='1').first()
        assert myuser.name=='user1'

    def test_failure_user(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        myuser = User.query.filter_by(id='1').first()
        assert myuser.name=='user2'

    def test_get_users(self):
        response = self.app.get('/api/v1.0/users')
        assert response.status_code==200

    def test_signup(self):
        response = self.app.post('/api/v1.0/signup', json={
                'name': 'flask', 'password': 'secret'
            })
        assert response.status_code==200

    def test_unauthorized_login(self):
        response = self.app.post('/api/v1.0/login', json={
                'name': 'flask', 'password': 'secret'
            })
        assert response.status_code==400

    def test_login(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Basic dXNlcjE6cGFzc3dvcmQ='
        }
        response = self.app.post('/api/v1.0/login', json={'name': 'user1', 'password': 'password'}, headers=headers)
        assert response.status_code==200

    def test_logout(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Basic dXNlcjE6cGFzc3dvcmQ='
        }
        self.app.post('/api/v1.0/login', json={'name': 'user1', 'password': 'password'}, headers=headers)
        response = self.app.get('/api/v1.0/logout', json={'name': 'user1', 'password': 'password'}, headers=headers)
        assert response.status_code==200

    def test_index_view(self):
        response = self.app.get('/')
        assert response.status_code==200


if __name__ == "__main__":
    unittest.main()
