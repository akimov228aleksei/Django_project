# Django_project
[![Python-package Actions Status](https://github.com/akimov228aleksei/Django_project/workflows/Python-package/badge.svg?branch=prod)](https://github.com/akimov228aleksei/Django_project/actions)
[![Coverage Status](https://coveralls.io/repos/github/akimov228aleksei/Django_project/badge.svg?branch=prod)](https://coveralls.io/github/akimov228aleksei/Django_project?branch=prod)

### Run 

To run the application, go to the settings.py file and in the DATABASES line change the database settings for your database,
next write the following while in the folder where the manage.py file is located:

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
python manage.py test
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