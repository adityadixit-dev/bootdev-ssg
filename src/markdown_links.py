import re


def extract_markdown_images(text):
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matched_images = re.findall(image_regex, text)
    return matched_images


def extract_markdown_links(text):
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matched_links = re.findall(link_regex, text)
    return matched_links
