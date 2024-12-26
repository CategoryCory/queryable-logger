import logging
import sqlite3
from pathlib import Path


class DBManager:
    def __init__(self, db_path: Path, schema_path: Path) -> None:
        self.db_path = db_path
        self.schema_path = schema_path
        self.logger = logging.getLogger(__name__)

    def initialize_database(self) -> None:
        """Ensure the database file exists and the schema is applied"""
        if not self.db_path.exists():
            self.logger.info(
                f"Database file not found. Creating database file: {self.db_path.name}"
            )
            self._create_database()
        self.logger.info(f"Applying schema to {self.db_path.name}")
        self._apply_schema()

    def _create_database(self) -> None:
        """Create the database file"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT SQLITE_VERSION()")
            version = cursor.fetchone()[0]
            self.logger.info(
                f"Database {self.db_path.name} created using SQLite version {version}."
            )

    def _apply_schema(self) -> None:
        """Apply schema from the schema.sql file to the database"""
        with sqlite3.connect(self.db_path) as conn:
            with open(self.schema_path, "r") as schema:
                conn.executescript(schema.read())
                self.logger.info("Schema applied successfully")

    def get_connection(self) -> sqlite3.Connection:
        """Provide a connection to the database"""
        return sqlite3.connect(self.db_path)
