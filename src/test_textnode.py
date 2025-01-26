import unittest

from textnode import TextNode, TextType

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


if __name__ == "__main__":
    unittest.main()
