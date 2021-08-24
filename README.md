## Instructions to Run

Requires docker-compose

To run with docker:

```
cd deployments
./run.sh {ROOT_DIRECTORY}
```

Where {ROOT_DIRECTORY} is the root directory to give as input for the app.
For example, we could give the /test folder as the root directory:
```
./run.sh /test
```
will run the application in the /test root directory.


To run the app with the root directory as a file on your local computer, do:

```
./run.sh /my_local_directory
```

To run locally from the command line (requires flask and Python 3):
```
export FLASK_APP=app
cd app
python app.py
```
In both cases, the app will run on localhost:5000.

To run the unit test:

```
# Run from in the doc_search/ directory
cd ../
pip install pytest
python app/app.test.py. {$USER}
```

## API Documentation

```
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
					description: Successfully returned file or directory.
					content: json
						schema: array or json
						items:
							type:object
							properties:
								name
								owner
								size
								permission
								is_directory
								content
				'400':
					description: Invalid request, if the path is not file or directory,
						or if the server receives keys other than path.
					content:
					application/json:
					  schema:
					    type: object
					    properties:   
					      message:
					        type: string

```
