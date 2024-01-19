import pytest

import lib.cuckoo.core.database
from lib.cuckoo.core.database import Database, init_database, reset_database


@pytest.fixture
def db():
    reset_database()
    try:
        init_database(dsn="sqlite://")
        retval = Database()
        retval.engine.echo = True
        yield retval
    finally:
        reset_database()


@pytest.fixture
def tmp_cuckoo_root(monkeypatch, tmp_path):
    monkeypatch.setattr(lib.cuckoo.core.database, "CUCKOO_ROOT", str(tmp_path))
