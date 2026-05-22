import sys

from copy_static import generate_static_folder
from gen_page import generate_pages_recursive


def main():
    basepath = "/"
    BUILD_DIR = "docs"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    generate_static_folder(BUILD_DIR)
    generate_pages_recursive("content", "template.html", "docs", basepath)

    # generate_page("content/index.md", "template.html", "public/index.html")


main()
