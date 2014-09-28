rm ../stock.sqlite3
./manage.py syncdb
./manage.py migrate stock
./manage.py migrate blog
