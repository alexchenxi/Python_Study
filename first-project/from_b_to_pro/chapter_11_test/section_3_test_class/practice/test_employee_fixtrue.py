from employee import Employee
import pytest


@pytest.fixture
def create_employee():
    """Create an employee instance for testing."""
    return Employee("john", "smith", 60000)


def test_give_default_raise(create_employee):
    create_employee.give_raise()
    assert create_employee.annual_salary == 65000


def test_give_custom_raise(create_employee):
    create_employee.give_raise(10000)
    assert create_employee.annual_salary == 70000
