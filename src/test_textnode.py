import unittest

from textnode import *
from leafnode import *
from parentnode import * 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne1(self):
        node  = TextNode("This is a text node 1", TextType.BOLD)
        node2 = TextNode("This is a text node 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url1(self):
        node  = TextNode("This is a text node 1", TextType.BOLD, "http")
        node2 = TextNode("This is a text node 2", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_url2(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_text_node_to_html_node1(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode(None, "This is a text node"))

    def test_text_node_to_html_node2(self):
        node = TextNode("alt-text", TextType.IMAGE, "http://foo.bar/img.png")
        node_html = text_node_to_html_node(node).to_html()
        expected_html = '<img alt="alt-text" src="http://foo.bar/img.png"></img>'
        self.assertEqual(node_html, expected_html)
    

    


if __name__ == "__main__":
    unittest.main()
