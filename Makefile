manage=./manage.py
python=python3

runserver:
	$(python) $(manage) runserver 0.0.0.0:8000

collectstaic:
	$(python) $(manage) collectstatic

check:
	$(python) $(manage) check

install:
	pip install -r requirements.txt

migrate:
	$(python) $(manage) makemigrations  && $(python) $(manage) migrate

freeze:
	pip freeze > requirements.txt

shell:
	$(python) $(manage) shell_plus

reset-db:
	$(python) $(manage) reset_db
	make migrate

superuser:
	$(python) $(manage) createsuperuser

create-user:
	$(python) $(manage) user

celery-worker:
	celery -A sporket_backend worker -l info