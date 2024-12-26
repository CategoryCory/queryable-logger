import logging
import sys
from database.db_manager import DBManager
from pathlib import Path


def setup_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        datefmt="%d/%m/%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def main() -> None:
    setup_logging()

    db_path = Path("logs.db")
    schema_path = Path("database/schema.sql")

    db = DBManager(db_path=db_path, schema_path=schema_path)
    db.initialize_database()


if __name__ == "__main__":
    main()
