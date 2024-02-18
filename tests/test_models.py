import pytest
from crudapp.models import Client, Request, Operator
 
@pytest.fixture
def client(db):
    return Client.objects.create(first_name="John", last_name="Doe", phone="1234567890")
 
@pytest.fixture
def operator(db):
    return Operator.objects.create(first_name="Jane", last_name="Smith")
  
@pytest.fixture
def requests( client, operator,db):
    return Request.objects.create(
        body="This is a test request.",
        client=client,
        processed_by=operator, 
        status='P'
    )
  
@pytest.mark.django_db
def test_create_client( client):
    assert Client.objects.count() == 1
    assert client.first_name == "John"
 
@pytest.mark.django_db
def test_create_operator( operator):
    assert Operator.objects.count() == 1
    assert operator.last_name == "Smith"
 
@pytest.mark.django_db
def test_create_request( requests):
    assert Request.objects.count() == 1
    assert requests.body == "This is a test request."
    assert requests.status == "P"
    assert requests.processed_by.first_name == "Jane" 
