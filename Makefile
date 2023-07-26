.PHONY: up
up: superuser
	docker-compose up

.PHONY: close_docker-compose_file
stop:
	docker-compose stop

.PHONY: db
db:
	docker-compose up -d db

makemigrations: db
	docker-compose run web python manage.py makemigrations

migrate: makemigrations
	docker-compose run web python manage.py migrate

load_products: migrate
	docker-compose run web python manage.py load_products data/goods.csv

superuser: load_products
	docker-compose run web python manage.py createsuperuser

.PHONY: run
run:
	docker-compose up
