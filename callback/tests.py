from django.test import Client, TestCase


class ApiTest(TestCase):

    def setup(self):
        self.client = Client()

    def test_save_shop(self):
        response = self.client.post(
            '/api/shop/',
            {
                "name": "Test Shop10",
                "city": "Madrid",
                "street": "Spanish street2",
                "number": "5",
                "opening_time": "09:00",
                "closing_time": "22:00"
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    def test_get_cities(self):
        self.client.post(
            '/api/shop/',
            {
                "name": "Test Shop10",
                "city": "Madrid",
                "street": "Spanish street2",
                "number": "5",
                "opening_time": "09:00",
                "closing_time": "22:00"
            },
            content_type='application/json'
        )
        response = self.client.get('/api/city/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()['cities'],
            [
                {'city': 'Madrid'}
            ]
        )

    def test_get_address(self):
        self.client.post(
            '/api/shop/',
            {
                "name": "Test Shop10",
                "city": "Madrid",
                "street": "Spanish street2",
                "number": "5",
                "opening_time": "09:00",
                "closing_time": "22:00"
            },
            content_type='application/json'
        )
        response = self.client.get('/api/city/1/addresses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()['addresses'],
            [
                {
                    'city': {'city': 'Madrid'},
                    'name': 'Spanish street2',
                    'number': '5'
                }
            ]
        )

    def test_get_shop(self):
        self.client.post(
            '/api/shop/',
            {
                "name": "Test Shop10",
                "city": "Madrid",
                "street": "Spanish street2",
                "number": "5",
                "opening_time": "09:00",
                "closing_time": "22:00"
            },
            content_type='application/json'
        )
        response = self.client.get('/api/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()['shops'],
            [
                {
                    'name': 'Test Shop10',
                    'address': {
                        'city': {
                            'city': 'Madrid',
                        },
                        'name': 'Spanish street2',
                        'number': '5'
                    },
                    'opening_time': '09:00:00',
                    'closing_time': '22:00:00'
                }
            ]
        )
        response = self.client.get('/api/shop/?open=test')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()['message'],
            "Error: OPEN parameter must be a number: 0/1"
        )
        self.assertEqual(
            response.json()['status'], 400
        )

    def test_exceptions(self):
        response = self.client.post(
            '/api/shop/',
            {
                "name": "Test Shop4",
                "city": "Berlin",
                "street": "Germany street1",
                "number": "357",
                "opening_time": "18:00",
                "closing_time": "01:30"
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()['message'],
            "Error: The opening time cannot be later than the closing time"
        )
        self.assertEqual(
            response.json()['status'], 400
        )
