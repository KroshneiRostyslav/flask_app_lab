import unittest
import html
from app import app

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        app.testing = True
        self.client = app.test_client()

    def test_empty_form(self):
        response = self.client.post('/login', data={}, follow_redirects=True)
        response_text = html.unescape(response.data.decode('utf-8'))
        self.assertIn('Поле обов\'язкове', response_text)

    def test_invalid_login(self):
        response = self.client.post('/login', data={
            'username': 'wrong',
            'password': 'wromg',
            'remember': 'y'
        }, follow_redirects=True)
        response_text = html.unescape(response.data.decode('utf-8'))
        self.assertIn('Логін чи пароль невірний', response_text)

    def test_successful_login_remember_checked(self):
        response = self.client.post('/login', data={
            'username': 'user',
            'password': 'password',
            'remember': 'y'
        }, follow_redirects=True)
        response_text = html.unescape(response.data.decode('utf-8'))
        self.assertIn('Вхід успішний запам\'ятати', response_text)

    def test_successful_login_remember_unchecked(self):
        response = self.client.post('/login', data={
            'username': 'user',
            'password': 'password',
        }, follow_redirects=True)
        response_text = html.unescape(response.data.decode('utf-8'))
        self.assertIn('Вхід успішний не запам\'ятовувати', response_text)

    if __name__ == '__main__':
        unittest.main()