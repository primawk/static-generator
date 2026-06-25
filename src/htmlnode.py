class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented

        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode:({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(props)
        self.tag = tag
        self.value = value
  
    def to_html(self):
        if self.value == None:
            raise ValueError("value is required.")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{f' {self.props}' if self.props is not None else ''}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return NotImplemented

        return self.tag == other.tag and self.value == other.value and self.props == other.props

    def __repr__(self):
        return f"LeafNode:({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(props)
        self.tag = tag
        self.children = children
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("tag is required.")
        if self.children == None:
            raise ValueError("children is required.")
            
        output_recursion = ""
        for children in self.children:
            output_recursion += children.to_html()
            
        return f"<{self.tag}{f' {self.props}' if self.props is not None else ''}>{output_recursion}</{self.tag}>"




    




    