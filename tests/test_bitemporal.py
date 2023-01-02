import pytest

from example_app.models import Employee


@pytest.fixture
def employee() -> Employee:
    return Employee.objects.create(name='John Doe')


@pytest.mark.django_db
def test_simple(employee: Employee):
    pass
