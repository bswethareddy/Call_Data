# Call_Data

Introduction
The Call API Project is a Django-based web application that allows users to initiate calls and view call records. This project demonstrates the implementation of RESTful API endpoints, database integration, HTML templates, pagination, and deployment using GitHub.

Getting Started
Prerequisites
Python 3.x
Django
PostgreSQL (for database storage, optional)
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
Install required packages:

Copy code
pip install -r requirements.txt
Project Structure
The project follows a typical Django project structure:

lua
Copy code
CallAPIProject/
|-- call_records/
|   |-- migrations/
|   |-- templates/
|   |-- admin.py
|   |-- models.py
|   |-- urls.py
|   |-- views.py
|-- CallAPIProject/
|-- manage.py
|-- requirements.txt
call_records: Django app containing models, views, and templates.
CallAPIProject: Project-level settings and configurations.
Configuration
Database Setup
To configure the database, update the DATABASES setting in CallAPIProject/settings.py to use PostgreSQL or the database of your choice.

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Static Files
Configure static files settings in CallAPIProject/settings.py:

python
Copy code
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
Endpoints
/initiate-call
Method: POST
Parameters:
from_number: Sender's phone number
to_number: Receiver's phone number
/call-report
Method: GET
Parameters:
phone: Phone number to filter call records
Frontend
HTML Templates
HTML templates are stored in the call_records/templates directory. The main templates include:

initiate_call.html: Form to initiate a call.
call_report.html: View call records and pagination.
Pagination
The django.core.paginator.Paginator class is used for pagination in the /call-report endpoint. The call_report view fetches and displays call records page-wise.

