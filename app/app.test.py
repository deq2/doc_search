import unittest
from app import app
from flask import json
from os import getcwd
from os.path import join, basename
import sys

class AppTestCase(unittest.TestCase):

	USER = 'deirdrequillen'

	def test_invalid_root(self):
		app.config['root'] = 'a'
		tester = app.test_client(self)
		response = tester.get('/')
		self.assertEqual(response.status_code, 400)

	def test_directories(self):
			test_directory = join(getcwd(), 'test')
			app.config['root'] = test_directory

			tester = app.test_client(self)

			# Test invalid request response.
			response = tester.get('/?anything')
			self.assertEqual(response.status_code, 400)

			
			response = tester.get('/?path=%2F')
			self.assertEqual(response.status_code, 200)
			data = json.loads(response.get_data())
			
			check_foo_name = False
			check_foo_owner = False
			check_foo_permission = False
			check_foo_is_dir = False
			check_test_name = False
			check_test_owner = False
			check_test_permission = False
			check_test_is_dir = False

			# Check file name, owner, permissions, is_directory.
			# File size may vary across machines due to how files
			# are allocated.
			for file in data:
				if file['name'] == 'foo':
					check_foo_name = True
					if file['owner'] == self.USER:
						check_foo_owner = True
					if file['permission'] == '755':
						check_foo_permission = True
					if file['is_directory'] == True:
						check_foo_is_dir = True
				if file['name'] == 'test.txt':
					check_test_name = True
					if file['owner'] == self.USER:
						check_test_owner = True
					if file['permission'] == '644':
						check_test_permission = True
					if file['is_directory'] == False:
						check_test_is_dir = True

			self.assertTrue(check_foo_name)
			self.assertTrue(check_foo_owner)
			self.assertTrue(check_foo_permission)
			self.assertTrue(check_foo_is_dir)

			self.assertTrue(check_test_name)
			self.assertTrue(check_test_owner)
			self.assertTrue(check_test_permission)
			self.assertTrue(check_test_is_dir)


			response = tester.get('/?path=%2Ffoo')
			self.assertEqual(response.status_code, 200)
			data = response.get_data()
			self.assertIn(b'\"name\": \"baz\"', data)
			self.assertIn(b'\"name\": \"bar1.txt\"', data)
			data_json = json.loads(response.get_data())
			for file in data_json:
				if file['name'] == 'baz':
					self.assertTrue(file['is_directory'])
				if file['name'] == 'bar1.txt':
					self.assertEqual(file['is_directory'], False)


			# Check we can see a hidden file.
			response = tester.get('/?path=%2Ffoo%2Fbaz')
			self.assertEqual(response.status_code, 200)
			data = response.get_data()
			self.assertIn(b'\"name\": \".hidden\"', data)

			response = tester.get('/?path=%2Ffoo%2Fbaz%2F.hidden')
			self.assertEqual(response.status_code, 200)
			data = json.loads(response.get_data())
			self.assertEqual({'contents':'This is a hidden file!'}, data)

			response = tester.get('/?path=%2Fblah')
			self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		AppTestCase.USER = sys.argv.pop()

	if not basename(getcwd()) == 'doc_search':
		raise RuntimeError('This test must be run from working directory doc_search')
	unittest.main()