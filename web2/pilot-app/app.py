from flask import Flask, render_template
from models.service import service

from mlab import mlab_connect

app = Flask(__name__)
mlab_connect()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<int:gender>')
def search(gender):
    filter_service = service.objects(gender = gender, occupied = False)
    # for service in all_service:
    # first_service = all_service[0]
    return render_template('search.html', all_service = filter_service)

if __name__ == '__main__':
  app.run( debug=True)
