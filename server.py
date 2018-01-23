import time
import json
import sqlite3
import os

from bottle import route, run, get, post, request, response

con = sqlite3.connect('blog.db')

@route('/api/status')
def api_status():
    return {'status':'online', 'servertime':time.time()}

#
@route('/')
@route('/info')
def info():
    return 'Hello! <ul><li>To check server status: /api/status</li><li>To Post to db: /post</li><li>To get posts: /posts</li> </ul>'



@post('/post')
def create():
    try:
        # parse input data
        try:
            data = request.body.read()
        except:
            raise ValueError

        if data is None:
            raise ValueError

    except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return


    title = request.json['title']
    body = request.json['body']

    c = con.cursor()
    c.execute("INSERT INTO posts (title,body) VALUES (?,?)", (title, body))
    con.commit()
    c.close()

    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'title': title, 'body': body})

@get('/posts')
def list():
    c = con.cursor()
    c.execute("SELECT * FROM posts")
    result = c.fetchall()
    c.close()

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(result)


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)