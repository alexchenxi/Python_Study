from employee import Employee


def test_give_default_raise():
    """Test that a default raise of 5000 is given."""
    employee_one = Employee("john", "smith", 60000)
    employee_one.give_raise()
    assert employee_one.annual_salary == 65000


def test_give_custom_raise():
    """Test that a custom raise is given."""
    employee_two = Employee("alex", "great", 60000)
    employee_two.give_raise(10000)
    assert employee_two.annual_salary == 70000
