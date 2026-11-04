# project/tests/test_summaries.py


def test_create_summary(test_app_with_db):
    """
    From our test fixture, we're using the TestClient to
    POST - expecting response to return 201 and write to our
    test DB
    """
    response = test_app_with_db.post(
        url="/summaries/",
        json={
            "url": "https://foo.bar",
        },
    )
    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"
