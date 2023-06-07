#
Python must be installed in the pc


Unzip the folder
Get in the richfeyn folder in vs code 
Enter this command : Venv\scripts\activate      
Cd to richfeyn project   :  cd richfeyn

Python manage.py createsuperuser



   (enter name ,  leave email , enter password 123 again 123 not visible then y  ) then go to 
(create a superuser and go to the http://127.0.0.1:8000/admin/) to view the database

Then in the richfeyn folde ender these commands :
Python manage.py makemigrations

Python manage.py migrate

Python manage.py runserver



If venv not working 
Delete venv 
Then enter this command : python -m venv venv 
Then : venv\scripts\activate
Then : pip install django
Then : cd richfeyn and go through the steps 


Data base may look like this 








