from page_generator import generate_page, generate_pages_recursive
from textnode import TextNode
from copycontent import copy_content

def main():
    copy_content("static", "public")
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")

main()