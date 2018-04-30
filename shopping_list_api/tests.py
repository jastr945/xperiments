import os
from flask import Flask
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

    def test_fail_user(self):
        u = User(name='user1')
        u.hash_password('password')
        db.session.add(u)
        db.session.commit()
        myuser = User.query.filter_by(id='1').first()
        assert myuser.name=='user2'

    def test_item(self):
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


# with app.test_client() as c:
#     rv = c.post('/api/auth', json={
#         'username': 'flask', 'password': 'secret'
#     })
#     json_data = rv.get_json()
#     assert verify_token(email, json_data['token'])

if __name__ == "__main__":
    unittest.main()
