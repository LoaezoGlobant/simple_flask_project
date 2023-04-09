import pytest
from app.models import User
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        user = User(username="test_user", email="test@email.com")
        db.session.add(user)
        db.session.commit()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_user_registration(app):
    test_user = "test_user"
    test_email = "test@email.com"
    client = app.test_client()
    response = client.post("/users/", json={
        "username": "test_user",
        "email": "test@email.com"
        })
    assert response.status_code == 201
    assert response.json["message"] == f"User {test_user} with email {test_email} has been successfully created"