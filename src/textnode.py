from enum import Enum
from htmlnode import LeafNode
import re

class TextType(Enum):
    TEXT ="text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, "href")
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {src: text_node.url, alt: text_node.text})
    raise Exception("unknown text node")

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result = []
    for node in old_nodes:  
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        if delimiter not in node.text:
            result.append(node)
            continue
            
        splitted_value = node.text.split(delimiter)

        for i in range(len(splitted_value)):
                if i % 2 == 0:
                    result.append(TextNode(splitted_value[i], TextType.TEXT))
                else:
                    result.append(TextNode(splitted_value[i], text_type))
    return result

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
            
        text = node.text
        extracted_value = extract_markdown_images(text)

        if len(extracted_value) == 0:
            result.append(node)
            continue
        
        for i in range(len(extracted_value)):
            image_markdown = f"![{extracted_value[i][0]}]({extracted_value[i][1]})"

            before, after = text.split(image_markdown, maxsplit=1)

            text = after
            if len(before) > 0:
                result.append(TextNode(before, TextType.TEXT))

            result.append(TextNode(extracted_value[i][0], TextType.IMAGE, extracted_value[i][1]))

        if len(text) > 0:
             result.append(TextNode(text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
            
        text = node.text
        extracted_value = extract_markdown_images(text)

        if len(extracted_value) == 0:
            result.append(node)
            continue
        
        for i in range(len(extracted_value)):
            image_markdown = f"![{extracted_value[i][0]}]({extracted_value[i][1]})"

            before, after = text.split(image_markdown, maxsplit=1)

            text = after
            if len(before) > 0:
                result.append(TextNode(before, TextType.TEXT))

            result.append(TextNode(extracted_value[i][0], TextType.LINK, extracted_value[i][1]))

        if len(text) > 0:
             result.append(TextNode(text, TextType.TEXT))
    return result
    
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    result_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    result_italic = split_nodes_delimiter(result_bold, "_", TextType.ITALIC)
    result_code = split_nodes_delimiter(result_italic, "`", TextType.CODE)
    result_image = split_nodes_image(result_code)





    






        
        


    

        
        

        

    

    







