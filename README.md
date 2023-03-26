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

Build the project
```
docker build -t rock-paper-scissor .
```

Build the project
```
docker run --volume $(pwd):/app rock-paper-scissor flask --app game init-db
docker run --publish 5000:5000 --volume $(pwd):/app rock-paper-scissor 
```

### Running the tests

```
docker run --volume $(pwd):/app rock-paper-scissor coverage run -m pytest
```

Coverage report
```
docker run --volume $(pwd):/app rock-paper-scissor coverage report
```

### Running the linter

```
docker run --volume $(pwd):/app rock-paper-scissor black .
```


### What I would do more?

I decided to make something simple based on time limitations, if I were to do something extra, I would:

* Separate UI x Backend: UI in react vs Flask API backend.
* Multiplayer (optional requirement)
* User authentication

### Screenshots

#### First screen
<img width="569" alt="image" src="https://user-images.githubusercontent.com/4131432/227778075-e1ff9d88-2cd5-40cb-a50b-4a6c260034c5.png">

#### Name screen
<img width="552" alt="image" src="https://user-images.githubusercontent.com/4131432/227778160-2b97ca16-5f0e-41a0-864d-3062b6c85a55.png">

#### Make your move screen
<img width="564" alt="image" src="https://user-images.githubusercontent.com/4131432/227778187-ae84fb2c-978f-4bf9-9311-d03eab0e09c1.png">

#### Result screen
<img width="570" alt="image" src="https://user-images.githubusercontent.com/4131432/227778223-33057d53-bf14-499e-9ecd-f4ec97ef266e.png">

#### 404 screen
<img width="566" alt="image" src="https://user-images.githubusercontent.com/4131432/227778235-3fd745f4-2038-4d5d-96b0-9ac493d08738.png">

#### Coverage
<img width="450" alt="image" src="https://user-images.githubusercontent.com/4131432/227778290-0bae4596-1038-41ff-af23-40aab9d942cb.png">
