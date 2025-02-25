from enum import Enum
from leafnode import *


class TextType(Enum):
    TEXT   = "text" 
    BOLD   = "bold"
    ITALIC = "italic"
    CODE   = "code"
    LINK   = "link"
    IMAGE  = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text      = text
        self.text_type = text_type
        self.url       = url

    def __eq__ (self, p2):
        if ((self.text      == p2.text) and
            (self.text_type == p2.text_type) and
            (self.url       == p2.url)):
            return True
        else:
            return False
    
    def __repr__ (self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("ValueError: unknown text type")
