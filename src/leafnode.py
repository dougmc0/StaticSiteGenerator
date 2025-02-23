from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value == None:
            raise Exception("ValueError")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise Exception("ValueError")
        if self.tag == None:
            return self.value
        else:
            props = self.props_to_html()
            if props == "":
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag} {props}>{self.value}</{self.tag}>"