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
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # def test_get_items(self):
    #     response = self.app.get('/api/v1.0/items')
    #     assert response.status_code, 200
    #
    # def test_get_users(self):
    #     response = self.app.get('/api/v1.0/users')
    #     assert response.status_code, 200


# with app.test_client() as c:
#     rv = c.post('/api/auth', json={
#         'username': 'flask', 'password': 'secret'
#     })
#     json_data = rv.get_json()
#     assert verify_token(email, json_data['token'])
