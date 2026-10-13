from db import DB

def test_set_and_get():
    db = DB("test.db")
    db.set_name(1, "Илья")
    assert db.get_name(1) == "Илья"

def test_unknown_user():
    db = DB("test.db")
    assert db.get_name(999) is None