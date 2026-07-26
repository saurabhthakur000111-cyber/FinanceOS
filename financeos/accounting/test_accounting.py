from financeos.accounting.accounting import Accounting


def test_accounting_creation():
    accounting = Accounting()
    assert accounting is not None
