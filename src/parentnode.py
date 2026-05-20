from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node must have a tag")
        if self.children is None:
            raise ValueError("Parent Node must have children")
        html_str = ""
        for child_node in self.children:
            html_str += child_node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
