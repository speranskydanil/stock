rm ../stock.sqlite3
./manage.py sqlclear admin auth contenttypes sessions messages staticfiles south pipeline stock blog | ./manage.py dbshell
./manage.py syncdb
./manage.py migrate stock
./manage.py migrate blog

