from app import app
import unittest
from unittest import TestCase

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_thing(self):
        response = self.app.get('/api/v1.0/items')
        print(response.data)



# with app.test_client() as c:
#     rv = c.post('/api/auth', json={
#         'username': 'flask', 'password': 'secret'
#     })
#     json_data = rv.get_json()
#     assert verify_token(email, json_data['token'])
