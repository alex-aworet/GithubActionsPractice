# test_app.py

import pytest
from flask import Flask
from hello_world import app, generate_html, greet

@pytest.fixture
def client():
    # Configure the Flask test client
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_greet_returns_expected_message():
    expected = 'Welcome to CI/CD 101 using GitHub Actions!'
    assert greet() == expected


def test_generate_html_contains_message():
    message = "Welcome to CI/CD 101 using GitHub Actions!"
    html = generate_html(message)

    # basic checks
    assert "<html>" in html
    assert "</html>" in html
    assert message in html


def test_generate_html_contains_image_tag():
    html = generate_html("anything")
    assert '<image height="540" width="1200"' in html
    assert "GitHub_Actions_Featured_Image.jpg" in html


def test_greeting_route_status_code(client):
    response = client.get("/greeting")
    assert response.status_code == 200


def test_greeting_route_content(client):
    response = client.get("/greeting")
    data = response.get_data(as_text=True)

    # Response should contain the greeting message
    assert 'Welcome to CI/CD 101 using GitHub Actions!' in data

    # Should be wrapped in some HTML
    assert "<html>" in data
    assert "</html>" in data
    assert "<div style='text-align:center;font-size:80px;'>" in data
