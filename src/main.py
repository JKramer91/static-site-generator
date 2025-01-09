from textnode import TextNode, TextType
from htmlnode import HTMLNode
def main():
    node = TextNode("This is a test node", TextType.BOLD, "https://www.boot.dev")
    test = HTMLNode("This is a HTML node", "This is its value", None, {
    "href": "https://www.google.com", 
    "target": "_blank",})
    print(test.__repr__())

if __name__ == "__main__":
    main()