import sys

from flask import (Flask,
render_template,
request,
url_for,
flash,
redirect,
jsonify,
make_response)

from os.path import exists, isfile, isdir, join, normpath, abspath
from os import listdir, stat

from pwd import getpwuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'k*(2HJ9ahjk#(sd5'

# The page where the user can navigate through directories
# and files.
@app.route('/', methods=['GET'])
def view_documents():
	root = app.config['root']

	if not isdir(root):
		message = jsonify(message='Root directory does not exist')
		return make_response(message, 400)

	relative_path = request.args.get('path')
	# relative_path = request.form['path']

	if relative_path is None:
		return render_template('view_documents.html', root=root)

	else:
		# Strip / at the beginning, to comply with os.path.join.
		if relative_path[0] == '/':
			relative_path = relative_path[1:]

		path = join(root, relative_path)

		# Return an error message if the file or directory does not exist.
		if not exists(path):
			message = jsonify(message='File or directory does not exist')
			return make_response(message, 400)
		# If it's a file, then return a json with contents of the file.
		if isfile(path):
			with open(path, 'r') as file:
				data = file.read()
			return jsonify([contents=data])
		# If the user enters a directory, list information for all files 
		# in the directory.
		if isdir(path):
			print(listdir(path))
			files = []
			for filename in listdir(path):
				status=stat(join(path, filename))
				files.append({
				'name': filename,
				'owner': getpwuid(status.st_uid).pw_name,
				'size': status.st_size,
				'permission': oct(status.st_mode)[-3:],
				'is_directory': isdir(join(path, filename))})
			return jsonify(files)

if __name__ == '__main__':
	root = sys.argv[1]
	app.config['root'] = root
	app.run(host='0.0.0.0', port='5000')