# Django_project
[![Python-package Actions Status](https://github.com/akimov228aleksei/Django_project/workflows/Python-package/badge.svg?branch=prod)](https://github.com/akimov228aleksei/Django_project/actions)
[![Coverage Status](https://coveralls.io/repos/github/akimov228aleksei/Django_project/badge.svg?branch=prod)](https://coveralls.io/github/akimov228aleksei/Django_project?branch=dev_trash)

To run the project, write the following while in the folder where the manage.py file is located:
1) python manage.py **makemigrations** 
2) python manage.py **migrate**
3) python manage.py **loaddata department/fixtures**   
4) python manage.py **runserver** 

To run the tests, do the following while in the folder with the manage.py file:
1) python manage.py **test**


To check coverage, do the following while on the management/department path:
1) coverage **run --source="." -m pytest tests/**
2) coverage **report**

