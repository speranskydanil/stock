rm ../stock.sqlite3
./manage.py migrate
./manage.py flush --noinput
./manage.py migrate
./manage.py syncdb

