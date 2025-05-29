def test_api_endpoint(client):
    response = client.get("/api/endpoint")
    assert response.status_code == 200
    assert "data" in response.json()

def test_code_submission(client):
    code = "print('Hello, World!')"
    response = client.post("/api/submit", json={"code": code})
    assert response.status_code == 200
    assert "vulnerabilities" in response.json()

def test_invalid_code_submission(client):
    response = client.post("/api/submit", json={"code": ""})
    assert response.status_code == 400
    assert "error" in response.json()