import unittest
import requests
import os

ENV = os.getenv('ENV', 'local')
BASE_URL = "http://localhost:80/api" if ENV == 'local' else "http://host.docker.internal:4000/api"
DATA_URL = "/data"
QUERY_URL = "/query"
DATA_ID = "/4"
class APITestSuite(unittest.TestCase):

    def test_response_200(self):
        response = requests.get(BASE_URL + DATA_URL)
        self.assertEqual(response.status_code, 200, "Status code is not 200")

    def test_response_404(self):
        response = requests.get(BASE_URL + "/nonexistent")
        self.assertEqual(response.status_code, 404, "Status code is not 404")

    def test_get_json(self):
        response = requests.get(BASE_URL + DATA_URL)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertIsInstance(response.json(), list, "Response is not JSON")

    def test_get_by_id(self):
        response = requests.get(BASE_URL + DATA_URL + DATA_ID)
        expected_json_data = {"date":"2012-01-05",
                              "precipitation":"1.3",
                              "temp_max":"8.9",
                              "temp_min":"2.8",
                              "wind":"6.1",
                              "weather":"rain"}
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertEqual(response.json(), expected_json_data, "Response data by id does not equal expected data")

    def test_query_data_limit_2(self):
        params = {'limit': 5}
        response = requests.get(BASE_URL + QUERY_URL, params=params)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertIsInstance(response.json(), list, "Response is not JSON")
        self.assertEqual(len(response.json()), 5, "Limit is not working")

    def test_query_data_date(self):
        params = {'date': '2012-06-04'}
        response = requests.get(BASE_URL + QUERY_URL, params=params)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertIsInstance(response.json(), list, "Response is not JSON")
        for record in response.json():
            self.assertEqual(record.get('date'), '2012-06-04', "Date filter is not working")
    def test_query_data_weather_rain(self):
        params = {'weather': 'rain'}
        response = requests.get(BASE_URL + QUERY_URL, params=params)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertIsInstance(response.json(), list, "Response is not JSON")
        for record in response.json():
            self.assertEqual(record.get('weather'), 'rain', "Weather filter is not working")

    def test_query_data_weather_rain_and_limit_5(self):
        params = {'weather': 'rain', 'limit': 5}
        response = requests.get(BASE_URL + QUERY_URL, params=params)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertIsInstance(response.json(), list, "Response is not JSON")
        self.assertEqual(len(response.json()), 5, "Limit is not working")
        for record in response.json():
            self.assertEqual(record.get('weather'), 'rain', "Weather filter is not working")

    def test_query_data_response_404(self):
        params = {'weather': 'blablabla'}
        response = requests.get(BASE_URL + QUERY_URL, params=params)
        self.assertEqual(response.status_code, 404, "Status code is not 404")

if __name__ == '__main__':
    unittest.main()