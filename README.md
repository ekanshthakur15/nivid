# Nivid

Freelance Project

## Installation Instructions

Follow these steps to set up the project locally.

### 1. Create a Virtual Environment

Create a virtual environment to isolate dependencies.

```sh
python -m venv .env
```
# or
```sh
python3 -m venv .env
```
2. Activate the Virtual Environment
Activate the virtual environment.

On Windows:
```sh

.\.env\Scripts\activate
```
On macOS/Linux:
```sh

source .env/bin/activate
```
3. Install Dependencies
Install the required dependencies.

```sh

pip install -r requirements.txt
```
4. Run Django Commands
Make migrations and apply them.


```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Create a Superuser
Create a superuser to access the admin dashboard.


```sh
python3 manage.py createsuperuser
```
6. Run the Server
Start the development server.

```sh
python3 manage.py runserver
```
7. Access the Admin Dashboard
Go to the following URL to access the admin dashboard.

```bash
http://localhost:8000/admin/
```
