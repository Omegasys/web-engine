# DOM tree
class Node:
    def __init__(self, tag, attributes=None, children=None):
        self.tag = tag
        self.attributes = attributes or {}
        self.children = children or []
        self.computed_style = {}

#paese CSS
import re

class CSSRule:
    def __init__(self, selector, declarations):
        self.selector = selector
        self.declarations = declarations

def parse_css(css_text):
    rules = []
    pattern = re.compile(r'([^{]+){([^}]+)}')
    for match in pattern.finditer(css_text):
        selector = match.group(1).strip()
        declarations_text = match.group(2).strip()
        declarations = {}
        for decl in declarations_text.split(';'):
            if ':' in decl:
                prop, value = decl.split(':', 1)
                declarations[prop.strip()] = value.strip()
        rules.append(CSSRule(selector, declarations))
    return rules


#match selectors
def match(node, selector):
    return node.tag == selector


#apply styles
def apply_styles(node, css_rules):
    for rule in css_rules:
        if match(node, rule.selector):
            node.computed_style.update(rule.declarations)
    for child in node.children:
        apply_styles(child, css_rules)



#render/test
html_tree = Node('div', children=[
    Node('p', children=[]),
    Node('span', children=[])
])

css_text = """
div { color: red; }
p { font-size: 16px; }
"""

css_rules = parse_css(css_text)
apply_styles(html_tree, css_rules)

print(html_tree.computed_style)  # {'color': 'red'}
print(html_tree.children[0].computed_style)  # {'font-size': '16px'}
