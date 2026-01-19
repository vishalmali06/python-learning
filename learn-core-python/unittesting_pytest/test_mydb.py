# TO run the test case use this
# pytest -W ignore::pytest.PytestUnknownMarkWarning --capture=no
from fixtures.mydb import MyDB

import pytest


@pytest.fixture(scope="module")
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    curr = conn.cursor()
    yield curr
    curr.close()
    conn.close()
    print("closing DB")

def test_vishals_id(cur):
    cur.execute("select id from employee_db where name='Vishal'")
    row = cur.fetchone()

    assert row[0] == 123


def test_veeras_id(cur):
    cur.execute("select id from employee_db where name='Veera'")
    row = cur.fetchone()

    assert row[0] == 789
