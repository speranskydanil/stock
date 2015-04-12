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

## Features

* Users, profile
* Categories, indexes
* Articles, pagination, WYSIWYG editor, filtering data
* Likes
* Feedback
* Most popular and most recent articles
* Administration through Django Admin
* Responsive design

![screen](https://raw.github.com/speranskydanil/stock/master/screenshot.jpg)

**Author (Speransky Danil):**
[Personal Page](http://dsperansky.info) |
[LinkedIn](http://ru.linkedin.com/in/speranskydanil/en) |
[GitHub](https://github.com/speranskydanil?tab=repositories) |
[StackOverflow](http://stackoverflow.com/users/1550807/speransky-danil)

