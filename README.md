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

### Create .env file and fill with required data
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
FIRST_METHOD=<CORS_ALLOW_METHODS #1>
SECOND_METHOD=<CORS_ALLOW_METHODS #2>
THIRD_METHOD=<CORS_ALLOW_METHODS #3>
FOURTH_METHOD=<CORS_ALLOW_METHODS #4>
FIFTH_METHOD=<CORS_ALLOW_METHODS #5>
SIXTH_METHOD=<CORS_ALLOW_METHODS #6>
```
### Run docker-compose file
```
docker-compose up
```
### Admin panel will be available

http://localhost:8000/admin

- login: admin@admin.net
- password: admin
### After all application wil be available

http://localhost:8000/api/schema/swagger-ui/

### For check a documentation u can follow
http://localhost:8000/api/schema/redoc/

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
- LinkedIn: https://www.linkedin.com/in/dmitry-tokariev/
- Email: moon0939110824@gmail.com
***
### Technology

- Python 3
- Django REST Framework
- Simple JWT
- Djoser
- Docker
- Swagger
- PostgreSQL