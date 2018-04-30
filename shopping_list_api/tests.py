import os
import base64
import unittest
from unittest import TestCase
from app import app
from models import db
from models import Item, User


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

    def test_failure_item(self):
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        myitem = Item.query.filter_by(id='1').first()
        assert myitem.title=='test title'

    def test_fail_item(self):
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        myitem = Item.query.filter_by(id='1').first()
        assert myitem.note=='fail note'

    def test_get_items(self):
        response = self.app.get('/api/v1.0/items')
        assert response.status_code==200

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

    def test_add_item(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Basic dXNlcjE6cGFzc3dvcmQ='
        }
        self.app.post('/api/v1.0/login', json={'name': 'user1', 'password': 'password'}, headers=headers)
        response = self.app.post('/api/v1.0/items', json={'title': 'item1', 'note': 'note1'}, headers=headers)
        assert response.status_code==201

    def test_failure_unauthorized_add_item(self):
        response = self.app.post('/api/v1.0/items', json={'title': 'item1', 'note': 'note1'})
        assert response.status_code==401

    def test_get_single_item(self):
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        response = self.app.get('/api/v1.0/items/1')
        assert response.status_code==200

    def test_failure_get_single_item(self):
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        response = self.app.get('/api/v1.0/items/2')
        assert response.status_code==404

    def test_update_item(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Basic dXNlcjE6cGFzc3dvcmQ='
        }
        self.app.post('/api/v1.0/login', json={'name': 'user1', 'password': 'password'}, headers=headers)
        response = self.app.put('/api/v1.0/items/1', json={'title': 'change', 'note': 'change'}, headers=headers)
        assert response.status_code==200

    def test_failure_unauthorized_update_item(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        response = self.app.put('/api/v1.0/items/1', json={'title': 'change', 'note': 'change'})
        assert response.status_code==401

    def test_delete_item(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Basic dXNlcjE6cGFzc3dvcmQ='
        }
        self.app.post('/api/v1.0/login', json={'name': 'user1', 'password': 'password'}, headers=headers)
        response = self.app.delete('/api/v1.0/items/1', headers=headers)
        assert response.status_code==200

    def test_unauthorized_delete_item(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        i = Item(title='test title', note='test note', user_id='1')
        db.session.add(i)
        db.session.commit()
        response = self.app.delete('/api/v1.0/items/1')
        assert response.status_code==401

    def test_index_view(self):
        response = self.app.get('/')
        assert response.status_code==200


if __name__ == "__main__":
    unittest.main()
