class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag      = tag
        self.value    = value
        self.children = children
        self.props    = props

    def __eq__ (self, p2):
        if ((self.tag      == p2.tag) and
            (self.value    == p2.value) and
            (self.children == p2.children) and
            (self.props    == p2.props)):
            return True
        else:
            return False
    
    def __repr__ (self):
        print(__repr_helper("tag", self.tag))
        print(__repr_helper("value", self.value))
        print(__repr_helper("children", self.children))
        print(__repr_helper("props", self.props))
        #return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def __repr_helper__ (name, dict):
        out = []
        for key, value in dict.items():
            out.append(f"key=\"{value}")
        out.sort()
        return name + ": " + " ".join(out)
    
    def to_html(self_):
        raise Exception("NotImplementedError")
    
    def props_to_html(self):
        out = []
        for key, value in self.props.items():
            out.append(f"{key}=\"{value}\"")
        out.sort()
        return " ".join(out)
    