from app.py import app



def test_index():
    tester = app.test_client()
    response = tester.get("/ping", content_type="html/text")

    assert response.status_code == 200
    assert response.data == "pong!"