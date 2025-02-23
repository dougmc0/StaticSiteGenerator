import unittest

from htmlnode import HTMLNode

class TextHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node  = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq2(self):
        node  = HTMLNode(tag="a", value="foo", props={"a":"http://foo"})
        node2 = HTMLNode(tag="a", value="foo", props={"a":"http://foo"})
        self.assertEqual(node, node2)

    def test_ne1(self):
        node  = HTMLNode(tag="a", value="foo",  props={"a":"http://foo"})
        node2 = HTMLNode(tag="a", value="foo2", props={"a":"http://foo"})
        self.assertNotEqual(node, node2)

    def test_ne2(self):
        node  = HTMLNode(tag="a", value="foo", props={"a":"http://foo"})
        node2 = HTMLNode(tag="a", value="foo", props={"a":"http://foo2"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node  = HTMLNode(tag="a", value="foo", props={"a":"http://foo", "b":"bar"})
        out1 = node.props_to_html()
        out2 = 'a="http://foo" b="bar"'
        self.assertEqual(out1, out2)

    # TODO: test children too

if __name__ == "__main__":
    unittest.main()
