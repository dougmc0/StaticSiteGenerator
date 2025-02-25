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
        o=[]
        o.append(f"tag: {self.tag}")
        o.append(f"value: {self.value}")
        if self.children == None:
            o.append ("children: no children")
        else:
            for child in self.children:
                o.append(f"child: {child.to_html()}")
              
        props_out = []
        if self.props == None:
            o.append ("props: none")
        else:
            for key, value in self.props.items():
                props_out.append(f"key=\"{value}")
            props_out.sort()
            props: ", ".join(props_out) + "\n"
            o.append(f"props={props}")
        return "\n".join(o)

    
    def to_html(self_):
        raise Exception("NotImplementedError")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        out = []
        for key, value in self.props.items():
            out.append(f"{key}=\"{value}\"")
        out.sort()
        return " ".join(out)
    