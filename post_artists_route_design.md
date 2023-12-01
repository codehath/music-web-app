# POST /artists Route Design

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```

## 2. Create Examples as Tests

```python
# POST /artists
#  Parameters:
#    name: Wild Noithing
#    genre: Indie
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""


# POST /artists
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Bad Request - Please provide a name and genre!
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```python
"""
POST /artists
  Parameters:
    name: Wild Noithing
    genre: Indie
  Expected response (200 OK):
  Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""
def test_post_artists_one(web_client):
    post_response = web_client.post('/artists', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == 'Artist added to Database'

    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies\nABBA\nTaylor Swift\nNina Simone\nWild Nothing"


"""
POST /artists
  Parameters:
    name: Wild Noithing
    genre: Indie
  Expected response (200 OK):
  Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""
def test_post_artists_none(web_client):
    post_response = web_client.post('/artists', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == 'Bad Request - Please provide a name and genre!'
```

---
