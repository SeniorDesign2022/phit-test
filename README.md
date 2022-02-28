# phit-test

# Initial Setup
Only do these steps if this is your first time working on the project.

## Dependencies
Activate virtual environment and run the following command to install all dependencies as outlined in requirements.txt. Run `python -m pip install -r requirements.txt` 

## Setting up Django Admin 
Then cd into phittestv1. Run `python manage.py migrate`. Then run `python manage.py createsuperuser` to create an admin account to log into Django Admin Dashboard. The username could be anything that you choose, and it could be set differently for each member of the group. However, I used "admin" for both the username and password. When it asks for the email, you can skip by pressing an "enter" on your keyboard. If you use a short password, it will warn you, but just respond "y" and you can still create an account. 

## Running the website locally
Make sure you have cd-ed into phittestv1. Then run `python manage.py runserver`. To quit the server, press control+C. 
