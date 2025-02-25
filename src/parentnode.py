from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag == None:
            raise Exception("ValueError: no tag")
        if children == None:
            raise Exception("ValueError: no children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise Exception("ValueError")
        if self.children == None:
            raise Exception("ValueError: no children")
        out = []
        #print(self.children)
        for child in self.children:
            #print("child + " + child.to_html())
            out.append(child.to_html())
        value = "".join(out)       
        if self.tag == None:
            return value
        else:
            props = self.props_to_html()
            if props == "":
                return f"<{self.tag}>{value}</{self.tag}>"
            else:
                return f"<{self.tag} {props}>{value}</{self.tag}>"