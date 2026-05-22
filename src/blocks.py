from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(md_text):
    if md_text.startswith("#") and md_text.lstrip("#").startswith(" "):
        return BlockType.HEADING
    if md_text.startswith("```") and md_text.endswith("```"):
        return BlockType.CODE

    lines = md_text.split("\n")
    is_quote_block = True
    is_unordered_list = True
    is_ordered_list = True
    ol_count = 1
    for l in lines:
        if not l.startswith(">"):
            is_quote_block = False
        if not l.startswith("- "):
            is_unordered_list = False
        if not l.startswith(f"{ol_count}."):
            is_ordered_list = False
        ol_count += 1
    if is_quote_block:
        return BlockType.QUOTE
    if is_unordered_list:
        return BlockType.ULIST
    if is_ordered_list:
        return BlockType.OLIST

    return BlockType.PARAGRAPH
