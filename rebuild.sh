rm ../stock.sqlite3
./manage.py syncdb
./manage.py migrate blog
