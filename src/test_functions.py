import unittest
from enum import Enum
from functions import *
from textnode import *
from leafnode import *
from parentnode import *
from functions import *


class TestFunctions(unittest.TestCase):
    def test1(self):
        out1 = split_nodes_delimiter(
            [
                TextNode("This is a", TextType.TEXT),
                TextNode("This is a text node", TextType.BOLD),
                TextNode("text node", TextType.TEXT),
            ],
            " ",
            TextType.TEXT,
        )
        out2 = [
            'This',
            'is',
            'a',
            TextNode("This is a text node", TextType.BOLD),
            'text',
            'node',
        ]
        self.assertEqual(out1, out2)


