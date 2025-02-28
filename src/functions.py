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
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            sections = old_node.text.split(delimiter)
            #print(f"{delimiter} sections = {sections}")
            if len(sections) % 2 == 0:
                raise ValueError(f"bad markdown for {delimiter}: {old_node.text}")
            inside_delimiter = False
            for section in sections:
                if section != "":
                    if inside_delimiter:
                        new_nodes.append(TextNode(section, text_type))
                    else:
                        new_nodes.append(TextNode(section, TextType.TEXT))
                inside_delimiter = not inside_delimiter
    #print ("new_nodes = ", new_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print (matches)
    return matches  

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches  

def split_nodes_image(old_nodes):
    out = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            while text != "":
                images = extract_markdown_images(text)
                if len(images) == 0:
                    out.append(TextNode(text, TextType.TEXT))
                    break
                for part in extract_markdown_images(text):
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
                        #print (f"new text = {text}")
                    else:
                        text = ""
        else:
            out.append(node)
    #print (f"out = {out}")
    return out   



def split_nodes_link(old_nodes):
    out = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            while text != "":
                links = extract_markdown_links(text)
                if len(links) == 0:
                    out.append(TextNode(text, TextType.TEXT))
                    break
                for part in extract_markdown_links(text):
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
                    # now add the link
                    out.append(TextNode(part[0], TextType.LINK, part[1]))
                    # and now leave the rest for the next iteration
                    if len(sections) > 1:
                        text = sections[1]
                        #print (f"new text = {text}")
                    else:
                        text = ""
        else:
            out.append(node)
    #print (f"out = {out}")
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
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    print (f"blocks = {blocks}")
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                nodes += text_to_textnodes(block)
            case BlockType.HEADING:
                nodes.append(LeafNode(f"h{block.count('#')}", block[2:]))
            case BlockType.CODE:
                nodes.append(LeafNode("code", block[4:]))
            case BlockType.QUOTE:
                nodes.append(LeafNode("blockquote", block[2:]))
            case BlockType.UNORDERED_LIST:
                items = block.split("\n")
                items = [item[2:] for item in items]
                items = [text_to_textnodes(item) for item in items]
                nodes.append(LeafNode("ul", "\n".join([f"<li>{item}</li>" for item in items])))
            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                items = [item[3:] for item in items]
                items = [text_to_textnodes(item) for item in items]
                nodes.append(LeafNode("ol", "\n".join([f"<li>{item}</li>" for item in items])))
    return nodes