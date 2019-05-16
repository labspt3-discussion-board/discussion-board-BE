### Getting Started

Run the following commands to clone the repository and change to the project directory:
```
>git clone https://github.com/labspt3-discussion-board/discussion-board-BE.git
>cd discussion-board-BE
```

Activate the virtual environment and install the required dependencies:
```
>pipenv shell
>pipenv install
```

Then you will need to [create and connect to a local database](#Create-and-connect-to-a-local-database)

Launch the development server: `>python manage.py runserver`

To work on a new feature, create a new branch: `>git checkout -b <feature>`

To work on a feature in progress, switch to the branch: `>git checkout <branch>`

### Create and connect to a local database

1. [Download](https://www.postgresql.org/download/) and install PostgreSQL for your operating system. Be sure to select the option to install pgAdmin 4, as this will make it much easier to manage your local database.

2. Once PostgreSQL and pgAdmin 4 are installed, open pgAdmin 4. Enter a password for the default user account (postgres). Remember this password, you will need it later to connect your Django project to your PostgreSQL database.

3. For this step, you can either use the default database that was created during installation (postgres), or you can create a new one. To create a new database, right click "PostgreSQL < version >" under the "Servers" collapsible panel on the left side of the window and select "Create > Database...". Give your database a name and click the "Save" button. Verify that it was created by opening the "Databases" collapsible panel. You should see your database listed below.

4. Next, you will need to install [psycopg2](http://initd.org/psycopg/); the driver that allows your Django project to interface with PostgreSQL. To do this, open a terminal and change your current working directory to your Django projects root directory. Be sure to activate the virtual environment by running the command `>pipenv shell`. Then run the command `>pipenv install psycopg2`. 

5. In the root directory of your Django project, create a .env file and create the following variables:

```
LOCAL_DB_ENGINE=django.db.backends.postgresql
LOCAL_DB_NAME=postgres || <your database name>
LOCAL_DB_USER=postgres || <your pg username>
LOCAL_DB_PASSWORD=<your pg password>
LOCAL_DB_HOST=127.0.0.1
LOCAL_DB_PORT=5432
```

*NOTE:* The database settings in the projects settings.py file should already be configured to import the environment variables needed to connect to your database.

6. Next, you will need to implement the data models by running the migrations for PostgreSQL. To do this, run the command: `>python manage.py migrate`. Verify that the migrations worked by opening pgAdmin 4 and opening the collapsible panels: "Servers > PostgreSQL *< version # >* > Databases > *< your databse >* > Schemas > Tables. Below, you should see the projects tables along with the default Django tables.

*NOTE*: If you need to update your database, you will need to define your models in the application's models.py file and run the command: `>python manage.py makemigrations`.
