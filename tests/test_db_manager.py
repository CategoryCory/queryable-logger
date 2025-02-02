import pytest
import sqlite3
from pathlib import Path
from src.database.db_manager import DBManager


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test.db"


@pytest.fixture
def schema_path() -> Path:
    return Path(__file__).parent / "test_db_schema" / "schema.sql"


@pytest.fixture
def test_db_col_info() -> list[tuple]:
    return [
        (0, "id", "INTEGER", 0, None, 1),
        (1, "timestamp", "TEXT", 1, None, 0),
        (2, "level", "TEXT", 1, None, 0),
        (3, "message", "TEXT", 1, None, 0),
        (4, "source", "TEXT", 0, None, 0),
    ]


class TestDBManager:
    """
    Unit tests for the DBManager class.
    """

    def test_db_created(self, db_path: Path, schema_path: Path) -> None:
        """
        Tests that creating an instance of DBManager and calling `initialize_database`
        properly creates the database file.

        :param db_path: The path of the database file.
        :type db_path: Path
        :param schema_path: The path of the schema file.
        :type schema_path: Path
        :return: None
        """
        test_db_manager = DBManager(db_path, schema_path)
        test_db_manager.initialize_database()
        assert db_path.exists()

    def test_db_schema_applied(
        self, db_path: Path, schema_path: Path, test_db_col_info: list[tuple]
    ) -> None:
        """
        Tests that the DBManager applies schema correctly when initialized.

        :param db_path: The path of the database file.
        :type db_path: Path
        :param schema_path: The path of the schema file.
        :type schema_path: Path
        :param test_db_col_info: The expected test database column info.
        :type test_db_col_info: list[tuple]
        :return: None
        """
        test_db_manager = DBManager(db_path, schema_path)
        test_db_manager.initialize_database()
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(test_logs)")
            columns = cursor.fetchall()
            assert len(columns) == len(test_db_col_info)
            for actual, expected in zip(columns, test_db_col_info):
                assert actual == expected
