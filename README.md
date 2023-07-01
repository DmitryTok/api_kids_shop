[![Python](https://img.shields.io/badge/-Python-%233776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0a)](https://www.python.org/)
[![Django Rest Framework](https://img.shields.io/badge/-Django%20Rest%20Framework-%2300B96F?style=for-the-badge&logo=django&logoColor=white&labelColor=0a0a0a)](https://www.django-rest-framework.org/)
[![JWT Authentication](https://img.shields.io/badge/-JWT%20Authentication-%23FFB300?style=for-the-badge&logo=json-web-tokens&logoColor=white&labelColor=0a0a0a)](https://jwt.io/)
[![Djoser](https://img.shields.io/badge/-Djoser-%23365DFF?style=for-the-badge&logo=django&logoColor=white&labelColor=0a0a0a)](https://djoser.readthedocs.io/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-%23316192?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=0a0a0a)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-%232496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=0a0a0a)](https://www.docker.com/)
[![Swagger](https://img.shields.io/badge/-Swagger-%2385EA2D?style=for-the-badge&logo=swagger&logoColor=white&labelColor=0a0a0a)](https://swagger.io/)
# Kids online shop

## Run the project 

#### 1) Create .env file and fill with required data
```
SECRET_KEY=django-insecure--n*k=k^euc4t_*2!=0n*fo1k%slbmzu)#o(a7qjz(c*cz8(&ly
DB_ENGINE=django.db.backends.postgresql
DB_NAME=kids_shop
DB_USER=dmitry_tok
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
POSTGRES_USER=dmitry_tok
POSTGRES_PASSWORD=postgres
POSTGRES_DB=kids_shop
```

#### 2) Open terminal and find folder api_kids_shop

#### 3) In folder api_kids_shop run the docker compose file with command
```
make up
```

#### After creating a docker container application will make a migrations and create a tables in database
#### Example of output in terminal
```
docker-compose up -d db
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Running 1/0
 ✔ Container api_kids_shop-db-1  Running                                                                                                                          0.0s 
docker-compose run web python manage.py makemigrations
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Creating 1/0
 ✔ Container api_kids_shop-db-1  Running                                                                                                                          0.0s 
[+] Building 0.0s (0/0)                                                                                                                                                
No changes detected
docker-compose run web python manage.py migrate
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Creating 1/0
 ✔ Container api_kids_shop-db-1  Running                                                                                                                          0.0s 
[+] Building 0.0s (0/0)                                                                                                                                                
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, sessions, users
Running migrations:
  No migrations to apply.
docker-compose up
[+] Building 0.0s (0/0)                                                                                                                                                
[+] Running 2/0
 ✔ Container api_kids_shop-db-1   Running                                                                                                                         0.0s 
 ✔ Container api_kids_shop-web-1  Created                                                                                                                         0.0s 
Attaching to api_kids_shop-db-1, api_kids_shop-web-1
```
#### After creating a container application wil be available by address

```
http://localhost:8000
```

### For check a documentation u can follow on this urls
```
http://localhost:8000/api/schema/redoc/
```
```
http://localhost:8000/api/schema/swagger-ui/
```

#### To stop container
```
ctrl + C
```

#### To delete container
```
make down
```
