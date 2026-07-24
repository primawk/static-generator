import os

from pathlib import Path

from blocknode import BlockType, block_to_block_type
from textnode import markdown_to_html_node



def extract_title(markdown):
    if block_to_block_type(markdown) != BlockType.HEADING:
        raise Exception("markdown is not a header")
    return markdown.lstrip("#").strip()

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as file:
        from_content = file.read()

    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    node = markdown_to_html_node(from_content)
    html_content = node.to_html()
    title = extract_title(from_content)

    updated_template = (
    template_content
    .replace("{{ Title }}", title)
    .replace("{{ Content }}", html_content)
    .replace('href="/', f'href="{basepath}')    
    .replace('src="/', f'src="{basepath}')    
    )

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(updated_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
        for dir in os.listdir(dir_path_content):
             
            src = os.path.join(dir_path_content, dir)
            dst = os.path.join(dest_dir_path, dir)

            if os.path.isfile(src):
                md_file = Path(dst)

                html_file = md_file.with_suffix(".html")

                generate_page(src, template_path, html_file, basepath)
            else:
                generate_pages_recursive(src, template_path, dst, basepath)