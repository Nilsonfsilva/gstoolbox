import pytest
import requests
from unittest.mock import patch

# Mock Response Class
class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

# Mock the search_repo function
def search_repo(platform, username, token):
    if platform == 'github':
        API_URL = f"https://api.github.com/users/{username}/repos"
    elif platform == 'gitlab':
        API_URL = f"https://gitlab.com/api/v4/users/{username}/projects"
    elif platform == 'salsa':
        API_URL = f"https://salsa.debian.org/api/v4/users/{username}/projects"
    else:
        raise ValueError("Invalid platform")

    response = requests.get(API_URL, headers={'Authorization': f'token {token}'})
    
    if response.status_code == 200:
        return [f"{repo['id']} {repo['name']}" for repo in response.json()]
    else:
        raise SystemExit(f"Error: {response.json().get('message', 'Unknown error')}")

# Test for valid repositories from GitHub
def test_search_repo_github(mocker):
    mock_response = [
        {"id": 1, "name": "repo1"},
        {"id": 2, "name": "repo2"},
    ]
    mocker.patch('requests.get', return_value=MockResponse(200, mock_response))  # Mockar requests

    output = search_repo('github', 'valid_username', 'valid_token')
    assert output == ["1 repo1", "2 repo2"]

# Test for GitHub authentication error
def test_search_repo_github_auth_error(mocker):
    mock_response = {"message": "Bad credentials"}
    mocker.patch('requests.get', return_value=MockResponse(401, mock_response))

    with pytest.raises(SystemExit):
        search_repo('github', 'invalid_username', 'invalid_token')

# Test for valid repositories from GitLab
def test_search_repo_gitlab(mocker):
    mock_response = [
        {"id": 1, "name": "repo1"},
        {"id": 2, "name": "repo2"},
    ]
    mocker.patch('requests.get', return_value=MockResponse(200, mock_response))  # Mockar requests

    output = search_repo('gitlab', 'valid_username', 'valid_token')
    assert output == ["1 repo1", "2 repo2"]

# Test for GitLab authentication error
def test_search_repo_gitlab_auth_error(mocker):
    mock_response = {"message": "Bad credentials"}
    mocker.patch('requests.get', return_value=MockResponse(401, mock_response))

    with pytest.raises(SystemExit):
        search_repo('gitlab', 'invalid_username', 'invalid_token')

# Test for valid repositories from Salsa
def test_search_repo_salsa(mocker):
    mock_response = [
        {"id": 1, "name": "repo1"},
        {"id": 2, "name": "repo2"},
    ]
    mocker.patch('requests.get', return_value=MockResponse(200, mock_response))  # Mockar requests

    output = search_repo('salsa', 'valid_username', 'valid_token')
    assert output == ["1 repo1", "2 repo2"]

# Test for Salsa authentication error
def test_search_repo_salsa_auth_error(mocker):
    mock_response = {"message": "Bad credentials"}
    mocker.patch('requests.get', return_value=MockResponse(401, mock_response))

    with pytest.raises(SystemExit):
        search_repo('salsa', 'invalid_username', 'invalid_token')

# Test for invalid platform
def test_search_repo_invalid_platform():
    with pytest.raises(ValueError):
        search_repo('invalid_platform', 'username', 'token')
