import os

from copy_static import copy_html_to_dest
from md_to_blocks import extract_title
from md_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_content = f.read()
    with open(template_path) as f:
        template_content = f.read()

    html_string = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    html_file_string = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_string
    )
    copy_html_to_dest(html_file_string, dest_path)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_list = os.listdir(dir_path_content)
    for f_or_d in dir_list:
        curr_path_of_fd = f"{dir_path_content}/{f_or_d}"
        if os.path.isfile(curr_path_of_fd):
            curr_file_path = f"{dir_path_content}/{f_or_d}"
            if f_or_d.split(".")[-1] != "md":
                continue
            dest_fn = ".".join(f_or_d.split(".")[:-1]) + ".html"
            dest_file_path = f"{dest_dir_path}/{dest_fn}"
            generate_page(curr_file_path, template_path, dest_file_path)
        else:
            new_content_dir = f"{dir_path_content}/{f_or_d}"
            new_dest_dir = f"{dest_dir_path}/{f_or_d}"
            generate_pages_recursive(new_content_dir, template_path, new_dest_dir)
