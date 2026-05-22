import unittest

from src.md_to_blocks import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_with_h1(self):
        self.assertEqual("Hello", extract_title("# Hello"))

    def test_with_multiple_headings(self):
        md = "## Not his\n\n# TRUE\n\n## Heading 3"
        self.assertEqual("TRUE", extract_title(md))
