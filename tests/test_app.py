from app import app


def test_home_endpoint():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "Secure CI/CD Pipeline"
    assert data["status"] == "running"


def test_health_endpoint():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_users_endpoint():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/api/users")

    assert response.status_code == 200

    data = response.get_json()

    assert data["total"] == 3
    assert len(data["users"]) == 3


def test_invalid_endpoint():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/invalid")

    assert response.status_code == 404
