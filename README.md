[![Python](https://img.shields.io/badge/-Python-%233776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0a)](https://www.python.org/)
[![Django Rest Framework](https://img.shields.io/badge/-Django%20Rest%20Framework-%2300B96F?style=for-the-badge&logo=django&logoColor=white&labelColor=0a0a0a)](https://www.django-rest-framework.org/)
[![JWT Authentication](https://img.shields.io/badge/-JWT%20Authentication-%23FFB300?style=for-the-badge&logo=json-web-tokens&logoColor=white&labelColor=0a0a0a)](https://jwt.io/)
[![Djoser](https://img.shields.io/badge/-Djoser-%23365DFF?style=for-the-badge&logo=django&logoColor=white&labelColor=0a0a0a)](https://djoser.readthedocs.io/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-%23316192?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=0a0a0a)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-%232496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=0a0a0a)](https://www.docker.com/)
[![Swagger](https://img.shields.io/badge/-Swagger-%2385EA2D?style=for-the-badge&logo=swagger&logoColor=white&labelColor=0a0a0a)](https://swagger.io/)
[![pre-commit](https://img.shields.io/badge/-pre--commit-yellow?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=0a0a0a)](https://pre-commit.com/)
[![Ruff](https://img.shields.io/badge/-Ruff-%23E10098?style=for-the-badge&logo=ruff&logoColor=white&labelColor=0a0a0a)](https://docs.astral.sh/ruff/)
[![isort](https://img.shields.io/badge/isort-enabled-brightgreen?style=for-the-badge&logo=isort&logoColor=white&labelColor=0a0a0a)](https://pycqa.github.io/isort/)
# Kids online shop

## Run the project 
***

### 1) Create .env file and fill with required data
```
SECRET_KEY=<SEKRET_KEY>
DB_ENGINE=<DB ENGINE postgres, mysql ...>
DB_NAME=<database name>
DB_USER=<database user>
DB_PASSWORD=<database password>
DB_HOST=<database host>
DB_PORT=<database port>
POSTGRES_USER=<database user>
POSTGRES_PASSWORD=<database password>
POSTGRES_DB=<database name>
EMAIL_HOST_USER=<your@email.com>
EMAIL_HOST_PASSWORD=<tour_password>
```
***
### 2) In folder api_kids_shop run the docker-compose file with command
```
docker-compose up -d db
```
Output example
```
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Running 3/3
 ✔ Network api_kids_shop_mynetwork  Created                                                                                                                       0.0s 
 ✔ Volume "api_kids_shop_db_data"   Created                                                                                                                       0.0s 
 ✔ Container api_kids_shop-db-1     Started 
```
***
### 3) Run web container
```
docker-compose up -d web
```
Output example
```
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Running 2/2
 ✔ Container api_kids_shop-db-1   Running                                                                                                                         0.0s 
 ✔ Container api_kids_shop-web-1  Started 
```
### 4) Next command prepares a makemigrations file for our new model, or creates a new migrations file for any changes if the models have been modified
```
docker-compose run web python manage.py makemigrations
```
Output example
```
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Creating 1/0
 ✔ Container api_kids_shop-db-1  Running                                                                                                                          0.0s 
[+] Building 0.0s (0/0)                                                                                                                                                
Migrations for 'users':
  users/migrations/0002_alter_customuser_username.py
    - Alter field username on customuser
```
***
### 5) Create tables and rows in database with command
```
docker-compose run web python manage.py migrate
```
Output example
```
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Creating 1/0
 ✔ Container api_kids_shop-db-1  Running                                                                                                                          0.0s 
[+] Building 0.0s (0/0)                                                                                                                                                
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, sessions, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying users.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
  Applying sessions.0001_initial... OK
  Applying users.0002_alter_customuser_username... OK
```
***
### 6) Load data to database(not required)
```
docker-compose run web python manage.py load_products data/goods.csv
```
Output example
```
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Creating 1/0
 ✔ Container api_kids_shop-db-1  Running                                                                                                                          0.0s 
[+] Building 0.0s (0/0)                                                                                                                                                
2023-07-04 11:23:38,629 - INFO - kids_shop.logger - Starting to upload data from data/goods.csv to the database
2023-07-04 11:23:38,666 - INFO - kids_shop.logger - Objects created: 20                                                                                                                       0.0s 
2023-07-18 18:58:55,790 - INFO - kids_shop.logger - Starting to upload --- CATEGORY --- to the database
2023-07-18 18:58:55,804 - INFO - kids_shop.logger - Objects created: 3
2023-07-18 18:58:55,805 - INFO - kids_shop.logger - Starting to upload --- SECTION --- to the --- ACCESSORIES CATEGORY ---
2023-07-18 18:58:55,816 - INFO - kids_shop.logger - Objects created: 9
2023-07-18 18:58:55,817 - INFO - kids_shop.logger - Starting to upload --- SECTION --- to the --- CHOSE CATEGORY ---
2023-07-18 18:58:55,830 - INFO - kids_shop.logger - Objects created: 11
2023-07-18 18:58:55,830 - INFO - kids_shop.logger - Starting to upload --- SECTION --- to the --- CLOTHES CATEGORY ---
2023-07-18 18:58:55,861 - INFO - kids_shop.logger - Objects created: 28
2023-07-18 18:58:55,861 - INFO - kids_shop.logger - Data has been uploaded successfully
```

### 7) Final command to look on all request urls and status codes
```
docker-compose up
```
Output example
```
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Running 2/0
 ✔ Container api_kids_shop-db-1   Running                                                                                                                         0.0s 
 ✔ Container api_kids_shop-web-1  Created                                                                                                                         0.0s 
Attaching to api_kids_shop-db-1, api_kids_shop-web-1
api_kids_shop-web-1  | Watching for file changes with StatReloader
api_kids_shop-web-1  | Performing system checks...
api_kids_shop-web-1  | 
api_kids_shop-web-1  | System check identified no issues (0 silenced).
api_kids_shop-web-1  | July 04, 2023 - 11:43:26
api_kids_shop-web-1  | Django version 4.2.2, using settings 'kids_shop.settings'
api_kids_shop-web-1  | Starting development server at http://0.0.0.0:8000/
api_kids_shop-web-1  | Quit the server with CONTROL-C.
```
### After all application wil be available

* [http://localhost:8000/api/schema/swagger-ui/

### For check a documentation u can follow

* http://localhost:8000/api/schema/redoc/

***
### To stop container
```
ctrl + C
```
Output example
```
Aborting on container exit...
[+] Stopping 2/2
 ✔ Container api_kids_shop-web-1  Stopped                                                                                                                         0.2s 
 ✔ Container api_kids_shop-db-1   Stopped                                                                                                                         0.2s 
canceled
make: *** [up] Error 130
```
### To stop container
```
docker-compose stop
```
Output example
```
[+] Stopping 2/0
 ✔ Container api_kids_shop-web-1  Stopped                                                                                                                         0.0s 
 ✔ Container api_kids_shop-db-1   Stopped 
```
### To delete container
```
docker-compose down -v
```
```
[+] Running 4/0
 ✔ Container api_kids_shop-web-1    Removed                                                                                                                       0.0s 
 ✔ Container api_kids_shop-db-1     Removed                                                                                                                       0.0s 
 ✔ Volume api_kids_shop_db_data     Removed                                                                                                                       0.1s 
 ✔ Network api_kids_shop_mynetwork  Removed
```
***
### Project author:
* https://www.linkedin.com/in/dmitry-tokariev/
* Email: moon0939110824@gmail.com
***
### Technology

- Python 3
- Django REST Framework
- Simple JWT
- Djoser
- Docker
- Swagger
- PostgreSQL