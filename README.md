## Instructions to Run

Requires docker-compose

To run with docker:

```
cd deployments
./run.sh {ROOT_DIRECTORY}
```

for example,
```
./run.sh /test
```
will run the application in the /test root directory.

To run locally from the command line (requires flask and Python 3):
```
export FLASK_APP=app
cd app
python app.py
```
In both cases, the app will run on localhost:5000.

To run the tests:

```
pip install pytest
cd app
python app.test.py.
```

## API Documentation

paths:
	/:
		get:
		description: Displays directory content or file content
			parameters:
				name: path
				description: If a directory, displays the contents of a directory.
				If a file, displays the file contents.
				type: string
			responses:
				'200':
					description:
					content:

