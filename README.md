## Steps

1. Install Python3, Pip3, virtualenv
2. create virtual env

    ```
       virtualenv venv
       .\venv\Scripts\activate 
     ```

3. Install Flask

    ```pip install flask```

- on the terminal cd into the app folder 
- run `pip install -r requirements.txt` to install required modules
- run `python manage.py db init ` to setup alembic migrations
- run `python manage.py db migrate -m='<your migration message>'` to create migration files
- then run `python manage.py db upgrade` to create tables

https://www.youtube.com/watch?v=WFzRy8KVcrM
https://github.com/CryceTruly/bookmarker-api