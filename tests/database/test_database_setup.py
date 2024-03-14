import sqlite3
import time
import unittest
import os

from converter.data.units import SUPPORTED_UNITS
from converter.database.database_setup import DatabaseSetup

class TestDatabaseSetup(unittest.TestCase):
    """
    This class includes testing the ability to create a database schema from an SQL file, populate
    the Units table with data, and perform various database operations correctly, such as
    insertion, retrieval, updating, and handling rollbacks on errors.

    Author: Sara Moussa
    """

    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    db_path = os.path.join(project_root, 'converter', 'database', 'utilities_app.db')
    sql_schema_file = os.path.join(project_root, 'converter', 'database', 'units_table.sql')

    @classmethod
    def setUp(cls) -> None:
        """Set up the test class by initializing the test database and populating it."""
        # Use the actual paths to the database and schema file.
        cls.db_manager = DatabaseSetup(cls.db_path, cls.sql_schema_file)
        cls.db_manager.create_db_schema()
        cls.db_manager.populate_units_table(SUPPORTED_UNITS)
        print("Test database setup complete.")

    def test_connection(self) -> None:
        """Test if the database connection can be established successfully."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            self.assertIsNotNone(conn)
        finally:
            if conn:
                conn.close()

    def test_create_schema(self) -> None:
        """Test if the database schema is created successfully."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Units';")
        table_name = cursor.fetchone()
        self.assertIsNotNone(table_name, "The 'Units' table does not exist.")
        if table_name:
            self.assertEqual(table_name[0], 'Units')
        conn.close()

    def test_populate_units(self) -> None:
        """Test if the Units table is populated with the correct data."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Units;")
        unit_count = cursor.fetchone()
        self.assertIsNotNone(unit_count, "Unable to retrieve count from 'Units' table.")
        if unit_count:
            expected_count = sum(len(info['units']) for info in SUPPORTED_UNITS.values())
            self.assertEqual(unit_count[0], expected_count,
                             "The 'Units' table does not have the expected number of entries.")
        conn.close()

    def test_retrieve_specific_unit(self) -> None:
        """Test if specific units can be retrieved from the Units table."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT ToBaseFactor FROM Units WHERE UnitName=?", ('mm',))
        factor = cursor.fetchone()
        self.assertIsNotNone(factor, "Unable to retrieve factor for 'mm'.")
        if factor:
            self.assertEqual(factor[0], 0.001)
        conn.close()

    def test_update_unit_factor(self) -> None:
        """Test if a unit's base factor can be updated successfully."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE Units SET ToBaseFactor=? WHERE UnitName=?", (0.002, 'mm'))
        cursor.execute("SELECT ToBaseFactor FROM Units WHERE UnitName=?", ('mm',))
        updated_factor = cursor.fetchone()
        self.assertIsNotNone(updated_factor, "Unable to retrieve updated factor for 'mm'.")
        if updated_factor:
            self.assertEqual(updated_factor[0], 0.002)
        conn.close()

    def test_nonexistent_table(self) -> None:
        """Test the error handling when querying a non-existent table."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with self.assertRaises(sqlite3.OperationalError):
            cursor.execute("SELECT * FROM NonExistentTable;")
        conn.close()

    def test_rollback_on_error(self) -> None:
        """Test if transactions are rolled back on error."""
        conn = sqlite3.connect(self.db_path)
        try:
            with conn:
                conn.execute("INSERT INTO Units (UnitName, Category, ToBaseFactor, BaseUnit) VALUES (?, ?, ?, ?);",
                             ('test', 'length', 1.0, 'm'))
                # Artificially trigger an error
                raise sqlite3.OperationalError("Forced error for testing.")
        except sqlite3.OperationalError:
            conn.rollback()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Units WHERE UnitName='test';")
        self.assertIsNone(cursor.fetchone(), "Transaction was not rolled back on error.")
        conn.close()

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up after tests by removing the test database file."""
        # Wait a moment to ensure the database connection is closed.
        time.sleep(1)

        try:
            os.remove(cls.db_path)
        except PermissionError as e:
            print(f"Failed to delete the database file: {e}")

if __name__ == '__main__':
    unittest.main()
