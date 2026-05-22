from split_images_and_links import split_nodes_image, split_nodes_link
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


def text_to_textnodes(text):
    og_text_node = TextNode(text, TextType.TEXT)
    nodes_after_bold = split_nodes_delimiter([og_text_node], "**", TextType.BOLD)
    nodes_after_italic = split_nodes_delimiter(nodes_after_bold, "_", TextType.ITALIC)
    nodes_after_code = split_nodes_delimiter(nodes_after_italic, "`", TextType.CODE)
    nodes_after_links = split_nodes_link(nodes_after_code)
    nodes_after_images = split_nodes_image(nodes_after_links)
    return nodes_after_images
