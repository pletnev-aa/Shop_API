dev_start:
	poetry run python manage.py runserver --settings=config.dev

test_coverage:
	poetry run coverage run --source='.' --omit="*tests.py*" manage.py test --settings=config.dev
	poetry run coverage xml

lint:
	poetry run flake8 callback
	poetry run flake8 config/urls.py
	poetry run flake8 service
	poetry run flake8 shop/admin.py
	poetry run flake8 shop/models.py

docker_build:
	docker-compose --env-file ./.env up --detach --build