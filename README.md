## Ice and Fire API (Django Rest Framework)
This project uses Ice and Fire API to get books. It also provides CRUD operations for books.


### Clone the repository 
```
git clone https://github.com/saadyousafarbi/got.git
```

### Setup virtual environment for project
```
virtualenv -p python3 ice-and-fire
source ice-and-fire/bin/activate
pip install -r requirements.txt
```

### Run database migrations 
```
python manage.py makemigrations
python manage.py migrate
```

### Run tests
```
python manage.py test
```

### Run server
```
python manage.py runserver
```

### API endpoints
| Endpoint        |   URL                                          |
| ----------------| -----------------------------------------------|
| External books  | `http://127.0.0.1:8080/api/external-books`     |
| Books           | `http://127.0.0.1:8080/api/v1/books`           |
