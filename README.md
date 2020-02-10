# insta-clone

### By **Alex Kiprop**. 


## Description

A web applications that allows users to share comment and like photos posted by users
<a href="https://instgramm.herokuapp.com/"><img src="/media/photos/insta.png"></a>

## User Stories
As a user I would like:
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.


## Setup/Installation Requirements

### Prerequisites
* Python 3.6.9
* Virtual environment
* PostgreSQL


### Installation Process
* run `git clone REPO-URL` in your terminal
* write `cd insta-clone`
* create a virtual environment with `python3.6 -m venv virtual`
* enter virtual environment `. virtual/bin/activate`
* run `pip install -r requirements.txt`
* create Postgres Database and name it `insta` and configure the settings
* run `python3.6 manage.py runserver` to run the application



## Technologies Used
- Python ( **ver 3.6** )
- Django ( **ver 2.0.5** )
- Django Bootstrap 3
- PostgreSQL

## Behavior Driven Development

| Behaviour| Input | Output |
| ------------- | ----------------- | ------------------ |
| Save uploaded images | Upload image | Saves image |
| Update images as app user | update image  | Updates |
| Search by username| search username | returns the user |


## License

This project is licensed under the MIT Open Source license, (c) Alex Kiprop



