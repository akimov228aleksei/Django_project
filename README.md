# Django_project
[![Python-package Actions Status](https://github.com/akimov228aleksei/Django_project/workflows/Python-package/badge.svg?branch=prod)](https://github.com/akimov228aleksei/Django_project/actions)
[![Coverage Status](https://coveralls.io/repos/github/akimov228aleksei/Django_project/badge.svg?branch=prod)](https://coveralls.io/github/akimov228aleksei/Django_project?branch=prod)

### Run 

To run the application, set the environment variables according to your database, 
then go to the folder where manage.py is located and do the following:


```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata department/fixtures   
python manage.py runserver
```
---

### Tests

To run the tests, do the following while in the folder with the manage.py file:
```
python manage.py test --settings=department.tests.test_settings
```
---

### Coverage

To check coverage, do the following while on the management/department path:
```
coverage run --source="." -m pytest tests/
coverage report
```
---
![](https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png)