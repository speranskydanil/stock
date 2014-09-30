rm ../stock.sqlite3
./manage.py sqlclear blog stock admin auth contenttypes sessions messages staticfiles south pipeline | ./manage.py dbshell
./manage.py syncdb
./manage.py migrate stock
./manage.py migrate blog

