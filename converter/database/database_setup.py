import sqlite3
from typing import Dict, Any

class DatabaseSetup:
    """
    Manages database operations for the Utility Application.

    This class provides methods to create a database schema from an SQL file
    and to populate the database with initial data.

    :param db_path: The file path to the SQLite database.
    :param sql_schema_file: The file path to the SQL schema file.

    Author: Sara Moussa
    """

    def __init__(self, db_path: str, sql_schema_file: str) -> None:
        """
        Initialize the DatabaseManager with paths to the database and schema file.

        :param db_path: Path to the database file.
        :param sql_schema_file: Path to the SQL schema file.
        """
        self.db_path = db_path
        self.sql_schema_file = sql_schema_file

    def create_db_schema(self) -> None:
        """
        Creates the database schema from the SQL schema file.

        This method reads the SQL file and executes its script to set up the
        database schema. It handles and reports database and file not found errors.

        :raises sqlite3.DatabaseError: If there's an error with executing the SQL script.
        :raises FileNotFoundError: If the SQL schema file is not found.
        """
        try:
            with sqlite3.connect(self.db_path) as conn, open(self.sql_schema_file) as sql_file:
                conn.executescript(sql_file.read())
            print("Database schema created successfully.")
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")
        except FileNotFoundError as e:
            print(f"SQL file not found: {e}")

    def populate_units_table(self, data: Dict[str, Any]) -> None:
        """
        Populates the Units table with provided data.

        Clears any existing data from the Units table and inserts new records based on
        the provided data dictionary.

        :param data: A dictionary containing unit categories and their respective units
                     and conversion factors.
        :raises sqlite3.DatabaseError: If there's an error with inserting data into the database.
        """
        delete_sql = "DELETE FROM Units;"  # Statement to clear the table to avoid data duplication while testing
        insert_sql = """
            INSERT INTO Units (UnitName, Category, ToBaseFactor, BaseUnit)
            VALUES (?, ?, ?, ?);
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(delete_sql)  # Clear the table before inserting new data
                for category, info in data.items():
                    base_unit = info['base']
                    for unit, factor in info['units'].items():
                        cursor.execute(insert_sql, (unit, category, factor, base_unit))
                conn.commit()  # Ensure changes are committed to the database
                print("Units table populated successfully.")
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")
