from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Testing that the information displayed is correct"""

        with self.client:
            response = self.client.get("/")
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('number_plays'))
            self.assertIn(b'<p>High Score', response.data)

    def test_invalid_word(self):
        """Test if the word is on the board"""

        self.client.get('/')
        response = self.client.get('/check-word?word=freakish')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_not_real_word(self):
        """Test if the word is in the dictionary"""

        self.client.get('/')
        response = self.client.get('/check-word?word=adsfjasdfl')
        self.assertEqual(response.json['result'], 'not-word')
