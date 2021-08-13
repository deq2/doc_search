import unittest
from app import app
from flask import json

class BasicTestCase(unittest.TestCase):
	def test_landing_page(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')

		print(response)
		self.assertEqual(response.status_code, 200)

		response = tester.post('/', data=dict(root='/Users/deirdrequillen/weavegrid_app/test/'))
		# Test input page redirects
		self.assertEqual(response.status_code, 302)

	def test_directories(self):
			tester = app.test_client(self)
			response = tester.get('/view?root=%2FUsers%2Fdeirdrequillen%2Fweavegrid_app%2Ftest')
			import pdb
			self.assertEqual(response.status_code, 200)
			response = tester.post('/view?root=%2FUsers%2Fdeirdrequillen%2Fweavegrid_app%2Ftest',
				data=dict(path="/"))
			self.assertEqual(response.status_code, 200)
			self.assertIn(b'\"name\": \"foo\"', response.data)
			self.assertIn(b'\"name\": \"test.txt\"', response.data)

			response = tester.post('/view?root=%2FUsers%2Fdeirdrequillen%2Fweavegrid_app%2Ftest',
				data=dict(path="/foo"))			
			self.assertIn(b'\"name\": \"bar1.txt\"', response.data)
			data = json.loads(response.get_data(as_text=True))
			assert {'name': 'baz', 'is_directory': True, 'size': 96, 'owner': 'deirdrequillen', 'permission': '755'} in data

			response = tester.post('/view?root=%2FUsers%2Fdeirdrequillen%2Fweavegrid_app%2Ftest',
				data=dict(path="/foo/baz"))
			self.assertIn(b'\"name\": \".hidden\"', response.data)



if __name__ == '__main__':
	unittest.main()