up:
	docker compose up --build

down:
	docker compose down -v

test:
	docker-compose run web coverage run manage.py test

report:
	docker-compose run web coverage report

html:
	docker-compose run web coverage html