import re

class HTMLElement:
    def __init__(self, tag, attributes, children):
        self.tag = tag
        self.attributes = attributes
        self.children = children

    def render(self, indent=0):
        indent_str = ' ' * indent
        output = f"{indent_str}<{self.tag}"
        for key, value in self.attributes.items():
            output += f' {key}="{value}"'
        output += '>'
        for child in self.children:
            output += '\n' + child.render(indent + 2)
        output += f"\n{indent_str}</{self.tag}>"
        return output

def parse_html(html):
    stack = []
    root = HTMLElement('root', {}, [])
    current = root

    # Regular expression to match HTML tags
    tag_pattern = re.compile(r'<(/?)(\w+)([^>]*)>')

    # Split the HTML into tokens
    tokens = re.split(r'(\s*<[^>]*>\s*)', html)

    for token in tokens:
        token = token.strip()
        if token.startswith('</'):
            # Closing tag
            match = tag_pattern.match(token)
            if match:
                _, tag, _ = match.groups()
                if stack:
                    stack.pop()
                    current = stack[-1] if stack else root
        elif token.startswith('<'):
            # Opening tag
            match = tag_pattern.match(token)
            if match:
                _, tag, attrs = match.groups()
                attrs_dict = dict(re.findall(r'(\w+)=["\'](.+?)["\']', attrs))
                new_element = HTMLElement(tag, attrs_dict, [])
                current.children.append(new_element)
                stack.append(current)
                current = new_element
        else:
            # Text content
            if current:
                current.children.append(HTMLElement('text', {}, [token]))

    return root

def render_html(html):
    root = parse_html(html)
    return root.render()
