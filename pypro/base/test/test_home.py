from django.test import Client


def test_status_colde(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
