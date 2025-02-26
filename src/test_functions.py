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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![picture](https://imgur.com/2.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("picture", "https://imgur.com/2.png")], matches)
                             
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)Extra",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        #print(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("Extra", TextType.TEXT),
            ],
            new_nodes)
                             

    def test_split_link1(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)Extra",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        #print(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("Extra", TextType.TEXT),
            ],
            new_nodes)
        

    def test_text_to_textnodes(self):
        string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(string)
        print("nides")
        print(nodes)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(nodes, expected)


    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items\n",
            ],)
        
                                
    def test_block_to_block_type(self):
        print("hi")
        block = "Paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        block = "# Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        block = "    code"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
        block = "> quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
        block = "1. ordered\n2. list\n"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
        block = "- unordered\n- list\n"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)