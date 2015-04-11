# Stock

Learning Django. Basic blog application.

## Installation

* Install Python 3.4, Virtualenv, PostgreSQL
* Create database
* git clone https://github.com/speranskydanil/stock.git; cd stock
* virtualenv -p python3.4 ../STOCK
* source ../STOCK/bin/activate
* pip install -r requirements.txt
* sed -i 's/smart_unicode/smart_text/g' ../STOCK/lib/python3.4/site-packages/sanitizer/models.py
* Edit stock/settings.py
* ./setup.sh
* ./seed.py (test data)
* ./manage.py runserver

## Deployment

* Install Nginx
* Edit deploy/
* Use configuration from nginx_server.conf for Nginx
* uwsgi --ini deploy/stock.ini
* service nginx restart
* ./manage.py collectstatic

