import unittest
from app import app
import json

class WeatherAppTestCase(unittest.TestCase):
    def setUp(self):
        # set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # send a GET request to the home route
        response = self.app.get('/')
        
        self.assertEqual(response.status_code, 200)
        
        # parse response JSON data
        data = json.loads(response.data)
        
        # Check that the JSON data has expected keys and values
        self.assertIn("city", data)
        self.assertIn("temperature", data)
        self.assertIn("condition", data)
        
        self.assertEqual(data["city"], "London")
        self.assertEqual(data["temperature"], "12°C")
        self.assertEqual(data["condition"], "Partly Cloudy")

if __name__ == '__main__':
    unittest.main()
