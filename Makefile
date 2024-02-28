up:
	docker compose up --build

down:
	docker compose down -v

test:
	docker-compose run web coverage run manage.py test -v 2

report:
	docker-compose run web coverage report