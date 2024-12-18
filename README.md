## DRF basic template

### Clone the repository:
```bash
git clone https://github.com/javohir-swe/drf.git
cd drf
```
### Database setup for those who don't use docker.
 - Installing PostgreSQL
 - You can install PostgreSQL with the following command in the terminal.

```bash
sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
```
 - On macOS, you can install posgresql in the terminal with brew:
```bash
brew install postgresql
```
 - Now, you may start up postresql after its installation with the following command.
```bash
brew services start postgresql
```
 - If you use a Windows machine, you can download a compatible [PostgreSQL installer](https://www.postgresql.org/download/windows/) from the official website of PostgreSQL.

### Creating a Database
 - As part of the installation, PostgreSQL already created a user, postgres by default for carrying out administrative responsibilities. We shall change to the user to create our database and new user.
   ```bash
   sudo su - postgres
   ```
 - `psql` gives us access to the Postgres interactive terminal where we can use the PostgreSQL queries.
   ```bash
   psql
   ```
 - Now, we shall create a database for this project. Always make sure to create a separate database for each project you work on.
   ```bash
   CREATE DATABASE mydb;
   ```
 - In the above command, we have used the CREATE command in SQL to create our database which we named mydb. We also ended the line with a semi-colon which comes after every command in SQL.

 - Creating a Database User
 - Now, we shall create a database user for our database. We will call the user `myuser`. Replace `password` with a strong password below.
   ```bash
   CREATE USER myuser WITH PASSWORD 'password';
   ```
 - Let us now grant access rights to our new user to enable it to work on the database.
   ```bash
   GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
   ```
 - We can then exit the current user's shell session and get back to the postgres user's session
   ```bash
   \q
   ```
 - Now, let us leave the PostgreSQL interactive terminal back to the terminal.
   ```bash
   exit
   ```
---
#### Create an environment file:
   ```bash
   cp .env.example .env
   ```

---
### If you want to use docker 
1. Build and start Docker containers:
   ```bash
   docker-compose up --build
   ```

2. If you want you can create database migrations:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

3. Create a superuser account:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

---
### If you don't want to use docker then the following commands are for you
1. Create a Virtual Environment activate it:
   ```bash
   python3 -m venv venv
   ```
   ```bash
   source venv/bin/activate
   ```
2. Migrate
   ```bash
   python3 manage.py migrate
   ```
3. Create Superuser account
   ```bash
   python3 manage.py createsuperuser
   ```
4. And then run the project
   ```bash
   python3 manage.py runserver
   ```
   If the result is as shown below, congratulations, you have successfully launched the project. 🎉 If there is any error, let [ChatGPT](https://chatgpt.com/) help you )
   ```bash
   Watching for file changes with StatReloader
   Performing system checks...
   
   System check identified no issues (0 silenced).
   December 18, 2024 - 16:48:14
   Django version 5.1.4, using settings 'core.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
      
   ```
---
### Access Points

After successful installation, you can access:

- **API Documentation**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Django Admin**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **API Endpoints**: [http://localhost:8000/api/](http://localhost:8000/api/)
---
### API Features

- Custom User Authentication
- JWT Token Authentication
- Swagger Documentation
- RESTful API Endpoints
- ---
## This template was written by [Javohir](https://github.com/javohir-swe).
