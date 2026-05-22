def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    lines_without_empty_blocks = list(map(lambda x: x.strip("\n"), lines))
    filtered_lines = list(filter(lambda x: x != "", lines_without_empty_blocks))
    stripped_lines = list(map(lambda x: x.strip(), filtered_lines))
    return stripped_lines


def extract_title(markdown):
    md_blocks = markdown_to_blocks(markdown)
    for blk in md_blocks:
        if blk.startswith("# "):
            return blk.lstrip("# ")

    raise Exception("No h1 header found")
