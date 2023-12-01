# GET /artists Route Design

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /artists
# Expected response (200 OK)
"""
Pixies, ABBA, Taylor Swift, Nina Simone
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /artists
  Expected response (200 OK):
  "Pixies, ABBA, Taylor Swift, Nina Simone"
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"
```
---
