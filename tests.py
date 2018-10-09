import unittest
import json
import requests


iss_now_url = 'http://api.open-notify.org/iss-now.json'
astros_url = 'http://api.open-notify.org/astros.json'


class TestApi(unittest.TestCase):
    def test_response_location_api(self):
        response = requests.get(iss_now_url)
        self.assertEqual(200, response.status_code)
        return response.text

    def test_response_content_location(self):
        response = requests.get(iss_now_url)
        data = json.loads(response.text)
        self.assertIn('longitude', data['iss_position'])

    def test_response_astro_api(self):
        response = requests.get(astros_url)
        self.assertEqual(200, response.status_code)

    def test_astros(self):
        response = requests.get(astros_url)
        data = json.loads(response.text)
        self.assertEqual(type(data['number']), int)
        self.assertEqual(len(data['people']), data['number'])


if __name__ == '__main__':
    unittest.main()
