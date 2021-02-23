# test_project


1) git clone https://github.com/alisher1989/test_project.git

2) cd test_project/

3) virtualenv -p python3.7 venv

4) source venv/bin/activate

5) pip install --upgrade pip

6) pip install -r req.txt

7) sudo -u postgres psql
      postgres=# CREATE DATABASE test_project;
      CREATE DATABASE
      postgres=# CREATE USER test_user WITH PASSWORD 'test_password';
      CREATE ROLE
      postgres=# ALTER ROLE test_user SET client_encoding TO 'utf8';
      ALTER ROLE
      postgres=# ALTER ROLE test_user SET timezone TO 'UTC';
      ALTER ROLE
      postgres=# GRANT ALL PRIVILEGES ON DATABASE test_project TO test_user;
      GRANT
      postgres=# \q

8) ./manage.py migrate

9) ./manage.py runserver
