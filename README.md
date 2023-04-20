## Steps

1. Install Python3, Pip3, virtualenv

   ```sudo apt install libpq-dev```

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
gunicorn
gunicorn --workers=4 --bind 0.0.0.0:8500 wsgi:app


docker-compose down --volumes
docker-compose up


https://www.youtube.com/watch?v=WFzRy8KVcrM
https://github.com/CryceTruly/bookmarker-api


Agent: http://127.0.0.1:5002/

https://app.datadoghq.eu/


docker build -t flask-bookmarks .
docker run  --name flask-api -p 8400:8500 flask-bookmarks



kubectl apply -f k8s/

kubectl apply -f k8s/bookmarks.namespace.yml
kubectl apply -f k8s/

kubectl delete -f k8s/
