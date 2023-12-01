import os
from flask import Flask, request

from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# GET /albums
# Returns a list of albums
# Try it:
#   ; curl http://localhost:5001/albums
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join([
        str(album) for album in repository.all()
    ])


# GET /albums/<id>
# Returns a single album
# Try it:
#   ; curl http://localhost:5001/albums/1
@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return str(repository.find(id))


# POST /albums
# Creates a new album
# Try it:
#   ; curl -X POST -d "title=Dave&author_name=Caden%20Lovelace" http://localhost:5001/albums
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album = repository.create(album)
    return "Album added successfully"


# DELETE /albums/<id>
# Deletes a album
# Try it:
#   ; curl -X DELETE http://localhost:5001/albums/1
@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return "Album deleted successfully"



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

