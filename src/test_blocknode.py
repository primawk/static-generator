import unittest
from blocknode import markdown_to_blocks, block_to_block_type, BlockType
from textnode import markdown_to_html_node

class TestBlockNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        md_heading = "###### This is a heading"
        md_paragraph =  """
                        This is **bolded** paragraph
                        text in a p
                        tag here

                        This is another paragraph with _italic_ text and `code` here

                        """
        md_unordered = """
                        - This is the first list item in a list block
                        - This is a list item
                        - This is another list item
                        """     
        md_code = """
                  ```
                  def greet():
                  print("Hello, world!")
    
                    greet()
                  ```
                  """
        
        md_quote = """
                    > This is a block quote.
                    >
                    > It can span multiple lines.
                    >
                    > It can even contain **bold**, *italic*, and `inline code`.
                    """
        
        md_ordered = """
                        1. This is the first list item in a list block
                        2. This is a list item
                        3. This is another list item
                     """

        block_type_heading = block_to_block_type(md_heading)
        block_type_paragraph = block_to_block_type(md_paragraph)
        block_type_unordered = block_to_block_type(md_unordered)
        block_type_code = block_to_block_type(md_code)
        block_type_quote = block_to_block_type(md_quote)
        block_type_ordered = block_to_block_type(md_ordered)

        self.assertEqual(BlockType.HEADING, block_type_heading)
        self.assertEqual(BlockType.PARAGRAPH, block_type_paragraph)
        self.assertEqual(BlockType.UNORDERED, block_type_unordered)
        self.assertEqual(BlockType.CODE, block_type_code)
        self.assertEqual(BlockType.QUOTE, block_type_quote)
        self.assertEqual(BlockType.ORDERED, block_type_ordered)

    def test_paragraphs(self):
        md = """
            # Boot.dev

            This is **bolded** paragraph

            This is another paragraph with _italic_ text
            
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Boot.dev</h1><p>This is <b>bolded</b> paragraph</p><p>This is another paragraph with <i>italic</i> text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()