import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("This is a HTML node", "This is its value", None, {
    "href": "https://www.google.com", 
    "target": "_blank",})
        val =  " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), val)
    
    def test_props_to_html_two(self):
        node = HTMLNode("This is a HTML node", "This is its value", None, {
    "href": "https://www.google.com", 
    "target": "_blank",})
        val =  " href=\"https://www.boot.dev\" target=\"_blank\""
        self.assertNotEqual(node, val)

    def test_repr(self):
        node = HTMLNode("This is a HTML node", "This is its value", None, {
                        "href": "https://www.google.com", 
                        "target": "_blank",})
        val = "HTMLNode(This is a HTML node, This is its value, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(node.__repr__(), val)
    

if __name__ == "__main__":
    unittest.main()