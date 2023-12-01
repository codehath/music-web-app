# Tests for your routes go here

def test_post_albums(web_client):
    post_response = web_client.post("/albums", data={
        'title':'Graduation',
        'release_year':'2005',
        'artist_id':'1'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == "Album added successfully"

    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)\n" \
        "Album(13, Graduation, 2005, 1)"
    










# """
# GET /albums
# """
# def test_get_albums(db_connection, web_client): # Note web_client fixture, see conftest.py
#     # We seed our database with the album store seed file
#     db_connection.seed("seeds/album_store.sql")

#     # We make a GET request to /albums
#     response = web_client.get("/albums")

#     # We assert that the response status code is 200
#     assert response.status_code == 200

#     # We assert that the response data is the same as the string we expect
#     assert response.data.decode("utf-8") == "\n".join([
#         "Album(1, Invisible Cities, Italo Calvino)",
#         "Album(2, The Man Who Was Thursday, GK Chesterton)",
#         "Album(3, Bluets, Maggie Nelson)",
#         "Album(4, No Place on Earth, Christa Wolf)",
#         "Album(5, Nevada, Imogen Binnie)"
#     ])

# """
# GET /albums/<id>
# """
# def test_get_album(db_connection, web_client):
#     db_connection.seed("seeds/album_store.sql")

#     response = web_client.get("/albums/1")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "" \
#         "Album(1, Invisible Cities, Italo Calvino)"

# """
# POST /albums
# """
# def test_create_album(db_connection, web_client):
#     db_connection.seed("seeds/album_store.sql")

#     response = web_client.post("/albums", data={
#         "title": "The Great Gatsby",
#         "author_name": "F. Scott Fitzgerald"
#     })

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "Album added successfully"

#     response = web_client.get("/albums")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "\n".join([
#         "Album(1, Invisible Cities, Italo Calvino)\n" +
#         "Album(2, The Man Who Was Thursday, GK Chesterton)\n" +
#         "Album(3, Bluets, Maggie Nelson)\n" +
#         "Album(4, No Place on Earth, Christa Wolf)\n" +
#         "Album(5, Nevada, Imogen Binnie)\n" +
#         "Album(6, The Great Gatsby, F. Scott Fitzgerald)"
#     ])

# """
# DELETE /albums/<id>
# """
# def test_delete_album(db_connection, web_client):
#     db_connection.seed("seeds/album_store.sql")

#     response = web_client.delete("/albums/1")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "Album deleted successfully"

#     response = web_client.get("/albums")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "\n".join([
#         "Album(2, The Man Who Was Thursday, GK Chesterton)\n" +
#         "Album(3, Bluets, Maggie Nelson)\n" +
#         "Album(4, No Place on Earth, Christa Wolf)\n" +
#         "Album(5, Nevada, Imogen Binnie)"
#     ])

