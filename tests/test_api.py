import pytest

from unittest import mock

from rls.api import Api

from rls.exceptions import (
    BadRequest,
    ResourceNotFound,
    Unauthorized,
    InternalServerError
)

from .utils import API_KEY


def test_api_request():
    api = Api()
    api_url = 'data/platforms'
    response = api.request(url=api_url, api_key=API_KEY, method='get')
    assert response.status_code == 200


@mock.patch('rls.api.request')
def test_api_return_400(mock_request):
    api = Api()
    response = mock.Mock()
    response.status_code = 400

    mock_request.return_value = response
    with pytest.raises(BadRequest):
        response = api.request(url='url', api_key='1234', method='get')


@mock.patch('rls.api.request')
def test_api_return_500(mock_request):
    api = Api()
    response = mock.Mock()
    response.status_code = 500

    mock_request.return_value = response
    with pytest.raises(InternalServerError):
        response = api.request(url='url', api_key='1234', method='get')


@mock.patch('rls.api.request')
def test_api_return_401(mock_request):
    api = Api()
    response = mock.Mock()
    response.status_code = 401

    mock_request.return_value = response
    with pytest.raises(Unauthorized):
        response = api.request(url='url', api_key='1234', method='get')


@mock.patch('rls.api.request')
def test_api_return_404(mock_request):
    api = Api()
    response = mock.Mock()
    response.status_code = 404

    mock_request.return_value = response
    with pytest.raises(ResourceNotFound):
        response = api.request(url='url', api_key='1234', method='get')
