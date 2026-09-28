import pytest
from bank import BankAccount

@pytest.fixture
def funded_account():
    """Fixture providing a BankAccount instance initialized with 1000 balance."""
    return BankAccount(1000)