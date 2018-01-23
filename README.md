# APIC

This API can be used to post/get data to/from database.

# Requirements
* python=3.5
* bottle=0.12.13

# Introduction

API is built on bottle(python framework). This app can be easily deployed on heroku.

# Deployment

Follow the following setups and you should be up and running:

*This project inculeds all the files need for deployment*
* Log on to heroku and create a new app
* install heroku CLI
* log in to heroku on CLI
    * heroku login
* goto your project directory and run the following command
    *  heroku git:remote -a apicpost
    * git push heroku master
    
URL to my app on heroku: https://apicpost.herokuapp.com/

# API usage

Use the following end points:

1) Status: /api/status
2) POST: /post (accepts json data only)
3) GET: /posts

