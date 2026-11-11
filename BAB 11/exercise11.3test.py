#Employee — Test File

import pytest
from employee import Employee


# ---- Tests WITHOUT fixture ----

def test_give_default_raise_no_fixture():
    """Test that an employee receives the default $5,000 raise."""
    employee = Employee("John", "Doe", 50_000)
    employee.give_raise()
    assert employee.annual_salary == 55_000


def test_give_custom_raise_no_fixture():
    """Test that an employee can receive a custom raise."""
    employee = Employee("John", "Doe", 50_000)
    employee.give_raise(10_000)
    assert employee.annual_salary == 60_000



@pytest.fixture
def default_employee():
    """Create an Employee instance for use in tests."""
    return Employee("John", "Doe", 50_000)


def test_give_default_raise(default_employee):
    """Test default raise using a fixture."""
    default_employee.give_raise()
    assert default_employee.annual_salary == 55_000


def test_give_custom_raise(default_employee):
    """Test custom raise using a fixture."""
    default_employee.give_raise(10_000)
    assert default_employee.annual_salary == 60_000


def test_give_zero_raise(default_employee):
    """Test that salary stays the same when raise is 0."""
    default_employee.give_raise(0)
    assert default_employee.annual_salary == 50_000
