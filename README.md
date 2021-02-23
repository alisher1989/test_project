# test_project


1) git clone https://github.com/alisher1989/test_project.git

2) cd test_project/

3) virtualenv -p python3.7 venv

4) source venv/bin/activate

5) pip install --upgrade pip

6) pip install -r req.txt

7) sudo -u postgres psql

      * CREATE DATABASE test_project;

      * CREATE USER test_user WITH PASSWORD 'test_password';

      * ALTER ROLE test_user SET client_encoding TO 'utf8';
      
      * ALTER ROLE test_user SET timezone TO 'UTC';
      
      * GRANT ALL PRIVILEGES ON DATABASE test_project TO test_user;
      
      * \q

8) ./manage.py migrate

9) ./manage.py runserver
