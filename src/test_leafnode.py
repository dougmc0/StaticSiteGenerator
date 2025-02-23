import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq1(self):
        node  = LeafNode(value='')
        node2 = LeafNode(value='')
        self.assertEqual(node, node2)

    def test_eq2(self):
        node  = LeafNode(tag="a", value="foo", props={"a":"http://foo"})
        node2 = LeafNode(tag="a", value="foo", props={"a":"http://foo"})
        self.assertEqual(node, node2)

    def test_ne1(self):
        node  = LeafNode(tag="a", value="foo",  props={"a":"http://foo"})
        node2 = LeafNode(tag="a", value="foo2", props={"a":"http://foo"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node  = LeafNode(tag="a", value="foo", props={"a":"http://foo", "b":"bar"})
        out1 = node.props_to_html()
        out2 = 'a="http://foo" b="bar"'
        self.assertEqual(out1, out2)

    def test_to_html1(self):
        node  = LeafNode(tag="a", value="foo", props={"href":"http://foo", "b":"bar"})
        out1 = node.to_html()
        out2 = '<a b="bar" href="http://foo">foo</a>'
        self.assertEqual(out1, out2)

    def test_to_html2(self):
        node  = LeafNode(tag="a", value="foo")
        out1 = node.to_html()
        out2 = '<a>foo</a>'
        self.assertEqual(out1, out2)



if __name__ == "__main__":
    unittest.main()
