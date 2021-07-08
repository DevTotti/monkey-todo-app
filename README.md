# Todo App
A Todo application that users can use to schedule tasks, update, delete and view tasks

## Installation

To run the application, you need to install dependencies first.

Taking a linux environment as a point of reference, first you need to clone this repo.

```
git clone https://github.com/DevTotti/monkey-todo-app.git
```

then navigate to the folder

```bash
cd monkey-todo-app
```

then you have to setup a vitrual environment

```bash
python3 -m venv env

source env/bin/activate
```

Now that is done, we need to install all dependencies needed for the app

```bash
pip install -r requirements.txt
```

You can also run this application as a docker image, to do that run

```
docker-compose up
```
The docker-compose will set it up and install the requirements and dependencies automatically


## Run Tests
First we have to run Unit test on the app to be sure everything works well. To run test, simply run the command

```
python manage.py test
```


#Usage
To run the server, by default the server runs on 5000 but you can change it to anything. You can do this by reading the comment in ```app.py``` line 89

When all is set, run the server using

```
python manage.py runserver
```

Then create a super user to access the admin portal

```
python manage.py createsuperuser
```



## API Documentation 
The API documentation is available on postman collection URL

```
https://www.getpostman.com/collections/550d77b6921b71f4c6ea

```

I hope you found it easy

Paul