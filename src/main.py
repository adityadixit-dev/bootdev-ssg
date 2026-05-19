from textnode import TextNode, TextType


def main():
    textnode = TextNode("Some Text here", TextType.LINK, "https://www.boot.dev")
    print(textnode)


main()
