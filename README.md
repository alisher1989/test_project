# test_project

В settings.py 
EMAIL_HOST_PASSWORD = 'your_password' (здесь укажите свой пароль)
EMAIL_HOST_USER = 'your_email' (здесь укажите свой gmail)


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

9) ./manage.py loaddata fixtures/auth.json 

10) ./manage.py loaddata fixtures/dump.json  

11) ./manage.py runserver


                    API ENDPOINTS
                    
    LOG IN                
 1) POST запрос на этот эндпоинт http://localhost:8000/auth/token/login/ , заполнив в Body, form-data 2 поля:
      * username : admin
      * password : admin
      получите примерно такой ответ: {"auth_token": "31d315c62e60d38aaf79efa0efe983d48b333141"},т.е. получаете токен.
      
      
 2) GET запросом http://localhost:8000/auth/users/me/ , заполнив Headers 
    * Authorization : Token 31d315c62e60d38aaf79efa0efe983d48b333141
    получите информация о своем профиле: {"email": "kada@test.com", "id": 1, "username": "admin"}
    
 
 3) PUT запросом http://localhost:8000/change_password/тут должно быть user_ID / , заполнив в Body, form-data 3 поля:
    * password : admin12345
    * password2 : admin12345
    * old_password : admin
    Также заполнив Headers 
    * Authorization : Token 31d315c62e60d38aaf79efa0efe983d48b333141
    этим запросом поменяете свой пароль
    
 4) PUT запросом http://localhost:8000/update_profile/тут должно быть user_ID / , заполнив в Body, form-data 4 поля:
    * username : admin12345
    * first_name : admin12345
    * last_name : admin
    * email: admin@admin.com
    Также заполнив Headers 
    * Authorization : Token 31d315c62e60d38aaf79efa0efe983d48b333141
    этим запросом отредактируете свои данные
    
    REGISTER
 5) POST запросом  http://localhost:8000/auth/users/ , заполнив в Body, form-data 3 поля:
    * username : admin
    * password : admin12345
    * email : admin@admin.com
    Также заполнив Headers 
    * Authorization : Token 31d315c62e60d38aaf79efa0efe983d48b333141
    этим запросом регистрируетесь, но чтоб получить токен, надо зайти в свой email.
    
    AKTIVATE ACCOUNT
  6) POST запросом http://localhost:8000/auth/users/activation/ , заполнив в Body, с emaila возьмете uid, token и через form-data 2 поля:
      * uid : MTU
      * token : aiinkd-1547ab0e819cc812c5e074dac17f4191
        аккаунт активируется
