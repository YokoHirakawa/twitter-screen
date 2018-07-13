
# Introduction

My first Django app that connects to my Twitter API:

* Show the list of tweets with the given hashtag
* Show the list of tweets that user has on his feed

# Installation

```
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver
```

NOTE: You also need my python-twitter API running on the same server

http://www.github.com/yokohirakawa/python-twitter-api/

# Tests

TODO

# Usage

Run the server and go to:

http://127.0.0.1/users/<screenname>

	or

http://127.0.0.1/hashtags/<hashtag>

Note: hashtag without the #

