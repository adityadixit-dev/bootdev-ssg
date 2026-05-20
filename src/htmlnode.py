class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,  # Node without a Tag is just raw text
        value: str | None = None,  # Node without value will have children
        children: (
            list[HTMLNode] | None
        ) = None,  # A node without children is expected to have a value
        props: (
            dict[str, str] | None
        ) = None,  # Node without props wont have any attributes
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        str_to_ret = ""
        for k, v in self.props.items():
            str_to_ret += f' {k}="{v}"'
        return str_to_ret

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
