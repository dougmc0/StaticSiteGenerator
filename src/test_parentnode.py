import unittest

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        text1 = node.to_html()
        text2 = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(text1, text2)

    def test2(self):
        node = ParentNode(
            "p",
            [
                ParentNode("b",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("p", "Normal text2"),
                    ]
                )
            ],
        )
        text1 = node.to_html()
        text2 = '<p><b><b>Bold text</b>Normal text<p>Normal text2</p></b></p>'
        self.assertEqual(text1, text2)


if __name__ == "__main__":
    unittest.main()
