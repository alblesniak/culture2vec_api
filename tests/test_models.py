import sys
import unittest

from app.models import Document

sys.path.append('..')


class TestModels(unittest.TestCase):

    def test_document_model(self):
        document = Document(content="Test Content", title="Test Title")
        self.assertEqual(document.content, "Test Content")
        self.assertEqual(document.title, "Test Title")

    # Add more tests for other models...


if __name__ == '__main__':
    unittest.main()
