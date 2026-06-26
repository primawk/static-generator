import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "hello world")
        node2 = HTMLNode("p", "hello world")
        node3 = HTMLNode("p", "hello world", children=[HTMLNode("span", "child")])  
        node4 = HTMLNode("p", "hello world", children=[HTMLNode("p", "test")])
          
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertNotEqual(node.to_html(), "test")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)          
        self.assertEqual(new_nodes[1], TextNode("bolded phrase", TextType.BOLD))



if __name__ == "__main__":
    unittest.main()


