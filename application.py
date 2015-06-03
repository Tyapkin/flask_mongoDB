# All imports
from mongokit import Connection, Document
from flask import Flask, jsonify, render_template

# configuration
HOST = 'localhost'
PORT = 27017
DATABASE = 'test'

# little app
app = Flask(__name__)
app.config.from_object(__name__)

# connect to test database
connection = Connection(app.config['HOST'],
                        app.config['PORT'])
db = connection[DATABASE]


# Our document
class City(Document):
    __collection__ = 'cities'
    structure = {
        'city': basestring,
        'loc': [float],
        'pop': int,
        'state': basestring
    }
    required_fields = ['city', 'loc', 'pop', 'state']


# register our document
connection.register([City])


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/get-cities', methods=['GET'])
def rating_of_cities():
    query = list(
        db.City.find().sort('pop', -1).limit(20)
    )
    return jsonify({'cities': query})


if __name__ == '__main__':
    app.run()
