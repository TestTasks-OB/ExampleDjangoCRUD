# ExampleDjangoCRUD

## How to run locally
Before to create structure for DB

```shell
python manage.py makemigrations crudapp   
python manage.py migrate              
```

then you can run locally 
```shell
python manage.py runserver          
```

## How to run in docker 

```shell
docker-compose up --build
```