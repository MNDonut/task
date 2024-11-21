- Create environment:
python3 -m venv env

- Activate env:
source env/bin/activate (Mac)

- Install requirements:
pip install -r requirements.txt

- Run migrations:
python manage.py migrate

- Create super admin:
python manage.py createsuperuser

- Run backend:
python manage.py runserver

Available endpoints:
api/expenses/ - get list of expenses / create a new one
api/expenses/{id}/ - get/update/delete a specific expense
api/users/{id}/expenses/?start_date=...&end_date=... - get user's expenses for a specific period
api/users/{id}/summary/ - get summary of user's transactions by categories
