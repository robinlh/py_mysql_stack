# Python + MySQL stack

## To use
pull/clone repo
```
cd py_mysql_stack
docker-compose build
docker-compose run -d
docker-compose exec app bash
```
Once inside your python container:
```
python test_db.py #or whatever script you want
```

## Notes
- I've got iPython installed in the python container which is nice for developing if you're not familiar with the python-db software
- I used sqlalchemy because the connection string is a lot more explicit. This will work with whatever, you just need to figure out what connection params your package needs
