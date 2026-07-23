import unittest
from page_generator import extract_title, generate_page, generate_pages_recursive
from textnode import TextNode, TextType, markdown_to_html_node, text_node_to_html_node

class TestPageGenerator(unittest.TestCase):
    def test_eq(self):
        generate_pages_recursive("content", "template.html", "public")

    
                 
if __name__ == "__main__":
    unittest.main()