import sys
import unittest

from app.db import create_db_and_tables, session
from app.models import Document

sys.path.append('..')



class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        # Setup a test database
        create_db_and_tables()

    def test_create_document(self):
        with session() as db:
            document = Document(content="Test Content", title="Test Title")
            db.add(document)
            db.commit()
            db.refresh(document)
            self.assertIsNotNone(document.id)

    # Add more tests for CRUD operations...


if __name__ == '__main__':
    unittest.main()
