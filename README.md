# Django Social Media Clone

This is the first clone project since following the Udemy Course for [Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/).<br />
There are some changes applied since this project is written in `Django==4.0.4` unlike the course material which follows `Django==1.0.0`.

## Common Usage
The application itself allows you to do the following:
- register multiple users
- create groups on various topics
- create /delete posts in each group only when logged in
- differentiate posts from different users with their profiles
- view user profile with list of posts only when logged in
- leave / join groups only when logged in

---

## Requirements
- Python 3.9.x
- Git
- Python Virtual Environment (preferable)
---
## Common setup
Clone the repo and install the dependencies.
``` 
git clone https://github.com/ana-gujabidze/django_first_social_media_project.git
cd django_first_social_media_project
```
Secret key in the settings module should not be hardcoded, it is a better and safer practice to keep it as an environment variable. Because of that create `.env` file similar to `.env_sample` file and specify `SECRET_KEY` there, which must a large random value.

---
## Run locally

### With virtual environment

Run the following command in the environment:
```
python3 -m pip install -r requirements.txt
```
Follow by running migrations:
`python3 manage.py migrate` & `python3 manage.py makemigrations`

After that start the server by running:
```
python3 manage.py runserver
```
Open the browser and follow the link 
```
http://127.0.0.1:8000/
```

### Without virtual environment

Run the following command in the environment:
```
pip3 install -r requirements.txt
```
The rest is the same as for the virtual environment.
