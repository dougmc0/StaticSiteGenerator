from enum import Enum

class TextType(Enum):
    TEXT_NORMAL = "normal" 
    TEXT_BOLD   = "bold"
    TEXT_ITALIC = "italic"
    TEXT_CODE   = "code"
    LINKS       = "link"
    IMAGES      = "images"

class TextNode:
    def __init__(self, text, text_type, url="None"):
        self.text      = text
        self.text_type = text_type
        self.url       = url

    def __eq___ (self, p2):
        if ((self.text == self.text) and (self.text_type == self.text_type) and (self.url == p2.url)):
            return True
        else:
            return False
    
    def __repr__ (self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
