import sys

from page_generator import generate_page, generate_pages_recursive
from textnode import TextNode
from copycontent import copy_content

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(basepath)
    copy_content("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()