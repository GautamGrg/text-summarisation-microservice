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


def test_create_summaries_invalid_json(test_app):
    """
    pass
    """
    response = test_app.post(url="/summaries/", json={})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": {},
                "loc": ["body", "url"],
                "msg": "Field required",
                "type": "missing",
            }
        ]
    }


def test_read_summary(test_app_with_db):
    response = test_app_with_db.post(url="/summaries/", json={"url": "https://foo.bar"})

    response_with_id = test_app_with_db.get(f"/summaries/{response.json()["id"]}")
    assert response_with_id.status_code == 200
    assert response_with_id.json()["id"] == response.json()["id"]
    assert response_with_id.json()["url"] == "https://foo.bar"


def test_read_summary_inncorrect_id(test_app_with_db):
    response = test_app_with_db.get("/summaries/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


def test_read_all_summaries(test_app_with_db):
    response_post = test_app_with_db.post(
        "/summaries/", json={"url": "https://foo.bar"}
    )
    response_get = test_app_with_db.get("/summaries/")
    assert response_get.status_code == 200

    response_list = response_get.json()
    assert (
        len(
            list(
                filter(
                    lambda d: d["id"] == response_post.json()["id"],
                    response_list,
                )
            )
        )
        == 1
    )
