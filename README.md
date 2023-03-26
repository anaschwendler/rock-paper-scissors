# Rock, paper, scissor

### How it was done

Since this was supposed to be a simple application, I decided to use Flask to develop a small application
containing both back and front-end.

Also, I decided for Flask as I've worked before with it, so I have familiarity with this web framework.

For the development, I started defining how I would save the session, for that I decided to use a database to save the current session. After that I started designing how I wanted the game to look like and decided how the visuals would look like. Then after starting working on the application, I started developing the routes and tests to make sure all is valid and working as supposed.

Then when a rough app was completed, I started decoupling and cleaning up a bit the code, so I created a helpers to decouple the functionalities.

### What was used

As mentioned before I decided to use Flask as web framework, and to get me up to date with the framework I started by taking a look at a [small example](https://flask.palletsprojects.com/en/2.2.x/tutorial/) provided in the documentation.

### Running the project  

#### Locally

Create virtual environment
```
python3 -m venv game-env
```

Activate virtual environment
```
. game-env/bin/activate
```

Install requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```

Initialize database:
```
flask --app game init-db
```

Run app
```
flask --app game run --debug
```

Deactivate virtual environment
```
deactivate
```

#### With Docker

Build the project
```
docker build -t rock-paper-scissor .
```

Build the project
```
docker run --publish 5000:5000 --volume $(pwd):/app rock-paper-scissor flask --app game init-db
docker run --publish 5000:5000 --volume $(pwd):/app rock-paper-scissor 
```

### Running the tests

#### Locally
```
coverage run -m pytest
```

Coverage report
```
coverage report
```

#### With Docker
```
docker run --volume $(pwd):/app rock-paper-scissor coverage run -m pytest
```

Coverage report
```
docker run --volume $(pwd):/app rock-paper-scissor coverage report
```

### Running the linter

#### Locally
```
black .
```

#### With Docker

```
docker run --volume $(pwd):/app rock-paper-scissor black . # --exclude '/game-env/'
```


### What I would do more?

I decided to make something simple based on time limitations, if I were to do something extra, I would:

* Separate UI x Backend: UI in react vs Flask API backend.
* Multiplayer (optional requirement)
* User authentication

### Screenshots

