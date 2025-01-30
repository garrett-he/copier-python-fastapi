async def test_index(client):
    r = client.get(url='/')

    assert r.status_code == 200
    assert r.json() == {'message': 'It works!', 'code': 0}
