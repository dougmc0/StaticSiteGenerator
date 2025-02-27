import re
from enum import Enum
from textnode import *

class BlockType(Enum):
    PARAGRAPH      = "paragraph" 
    HEADING        = "heading"
    CODE           = "code"
    QUOTE          = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST   = "ordered_list"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []
    for node in old_nodes:
        if node.text_type == text_type:
            out += node.text.split(delimiter)
        else:
            out.append(node)
    return out

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print (matches)
    return matches  

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches  

def split_nodes_image(old_nodes):
    out = []
    text = ""
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            for part in extract_markdown_images(node.text):
                split_string = f"![{part[0]}]({part[1]})"
                sections = text.split(split_string, 1)
                #print(f"text = {text}")
                #print(f"part = {part}")
                #print(f"split-string={split_string}")
                #print(f"sections = {sections}")
                #print()
                # if there is something before, add it.
                if sections[0] != "":
                    out.append(TextNode(sections[0], TextType.TEXT))
                # now add the image
                out.append(TextNode(part[0], TextType.IMAGE, part[1]))
                # and now leave the rest for the next iteration
                if len(sections) > 1:
                    text = sections[1]
                else:
                    text = ""
                    break
        else:
            out.append(node)
    # catch anything left over
    if text != "":
        out.append(TextNode(text, TextType.TEXT))
    return out   

def split_nodes_link(old_nodes):
    out = []
    text = ""
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            for part in extract_markdown_links(node.text):
                split_string = f"[{part[0]}]({part[1]})"
                sections = text.split(split_string, 1)
                #print(f"text = {text}")
                #print(f"part = {part}")
                #print(f"split-string={split_string}")
                #print(f"sections = {sections}")
                #print()
                # if there is something before, add it.
                if sections[0] != "":
                    out.append(TextNode(sections[0], TextType.TEXT))
                # now add the image
                out.append(TextNode(part[0], TextType.LINK, part[1]))
                # and now leave the rest for the next iteration
                if len(sections) > 1:
                    text = sections[1]
                else:
                    text = ""
                    break
        else:
            out.append(node)
    # catch anything left over
    if text != "":
        out.append(TextNode(text, TextType.TEXT))
    return out   


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return blocks

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("    "):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH