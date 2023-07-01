.PHONY: up
up: migrate
	docker-compose up

.PHONY: close_docker-compose_file
down:
	docker-compose down -v

.PHONY: db
db:
	docker-compose up -d db

makemigrations: db
	docker-compose run web python manage.py makemigrations

migrate: makemigrations
	docker-compose run web python manage.py migrate

.PHONY: superuser
superuser: migrate
	docker-compose run web python manage.py createsuperuser
