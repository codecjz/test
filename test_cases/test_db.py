import pytest



@pytest.fixture()
def db():
    print('Connection successful')

    yield

    print('Connection closed')