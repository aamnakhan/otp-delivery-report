from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "LOCAL_DB_URL"
app.debug = True

from views import *

if __name__ == '__main__':
    app.run()
