def test_mainpage(client):
    response = client.get('/')

    assert response.status_code == 200
