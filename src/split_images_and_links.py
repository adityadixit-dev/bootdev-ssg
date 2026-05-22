from markdown_links import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links_in_node = extract_markdown_links(node.text)

        if len(links_in_node) < 1:
            if node.text != "":
                new_nodes.append(node)
            continue

        og_text = node.text

        for l in links_in_node:
            sections = og_text.split(f"[{l[0]}]({l[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(l[0], TextType.LINK, l[1]))
            og_text = sections[1]
        if og_text != "":
            new_nodes.append(TextNode(og_text, TextType.TEXT))
    return new_nodes


def split_nodes_image(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images_in_node = extract_markdown_images(node.text)
        if len(images_in_node) < 1:
            if node.text != "":
                new_nodes.append(node)
            continue

        og_text = node.text

        for l in images_in_node:
            sections = og_text.split(f"![{l[0]}]({l[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(l[0], TextType.IMAGE, l[1]))
            og_text = sections[1]
        if og_text != "":
            new_nodes.append(TextNode(og_text, TextType.TEXT))
    return new_nodes
