# Challenge
Python application developed with Pyramid Framework. 

Routes:

* **/** - page with content "Index".
* **/quotes** - page with all quotes from [API](https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes) in *bullet points* format.
* **/quote/{id}** - page with quote by id from [API](https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes).
* **/quotes/random** - page with a random quote.

Quotes API:
* https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes

RESTful API to get sessions(date, hour, last page):

* **/api/sessions**
* **/api/session/{id}**

#### Development

##### Python Version: 3.7

##### Manual
```
~/challenge$ pip install -e quotes/.
~/challenge$ pip install -e .
~/challenge$ alembic -c challenge.ini upgrade head
~/challenge$ alembic -c challenge.ini revision --autogenerate -m "init"
~/challenge$ pserve challenge.ini
```

##### Docker

**Build docker image**
```
docker build -t desafio:1.0 -f dockerfile .
```
**Run docker image**
```
docker run -ti -p 6543:6543 desafio:1.0
```

#### Tests
**Run lib tests**
```
~/quotes$ pytest tests/test_quotes.py
```
**Run pyramid tests**
```
~/challenge$ pytest
```