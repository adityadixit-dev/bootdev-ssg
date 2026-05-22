from copy_static import generate_static_folder
from gen_page import generate_page, generate_pages_recursive


def main():
    generate_static_folder()
    generate_pages_recursive("content", "template.html", "public")

    # generate_page("content/index.md", "template.html", "public/index.html")


main()
