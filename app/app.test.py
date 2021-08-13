import unittest
from app import app
from flask import json
import pdb


class BasicTestCase(unittest.TestCase):

	def test_directories(self):
			app.config['root'] = "/Users/deirdrequillen/doc_search/test"

			tester = app.test_client(self)
			response = tester.get('/?path=%2F')
			self.assertEqual(response.status_code, 200)
			data = json.loads(response.get_data())
			assert {'owner': 'deirdrequillen', 'size': 160, 'permission': '755', 'is_directory': True, 'name': 'foo'} in data
			assert {'name': 'test.txt', 'size': 35, 'is_directory': False, 'owner': 'deirdrequillen', 'permission': '644'} in data

			response = tester.get('/?path=%2Ffoo')
			self.assertEqual(response.status_code, 200)
			data = json.loads(response.get_data())
			print(data)
			assert {"is_directory":True,"name":"baz","owner":"deirdrequillen","permission":"755","size":96} in data
			assert {"is_directory":False,"name":"bar1.txt","owner":"deirdrequillen","permission":"644","size":4} in data


			response = tester.get('/?path=%2Ffoo%2Fbaz')
			self.assertEqual(response.status_code, 200)
			data = json.loads(response.get_data())
			print(data)
			assert {"is_directory":False,"name":".hidden","owner":"deirdrequillen","permission":"644","size":22} in data

			response = tester.get('/?path=%2Ffoo%2Fbaz%2F.hidden')
			self.assertEqual(response.status_code, 200)
			data = json.loads(response.get_data())
			assert {"contents":"This is a hidden file!"} == data


if __name__ == '__main__':
	unittest.main()