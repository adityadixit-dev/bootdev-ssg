import os
import shutil


def generate_static_folder(build_dir="public"):
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.mkdir(build_dir)

    STATIC_FOLDER = "static"

    if not os.path.exists(STATIC_FOLDER):
        raise Exception("No Static Folder")

    copy_dir_rec(STATIC_FOLDER, build_dir)


def copy_dir_rec(input_dir, output_dir):
    dir_list = os.listdir(input_dir)
    for f_or_d in dir_list:
        curr_path_of_fd = f"{input_dir}/{f_or_d}"
        if os.path.isfile(curr_path_of_fd):
            curr_file_path = f"{input_dir}/{f_or_d}"
            new_file_path = f"{output_dir}/{f_or_d}"
            print(f"Copying {curr_file_path} to {new_file_path} ")
            shutil.copy(curr_file_path, new_file_path)
        else:
            new_op_dir = f"{output_dir}/{f_or_d}"
            if not os.path.exists(new_op_dir):
                os.mkdir(new_op_dir)
            copy_dir_rec(curr_path_of_fd, new_op_dir)


def copy_html_to_dest(html_string, dest_path):
    dest_split = dest_path.split("/")
    dest_filename = dest_split[-1]
    dest_directory = "/".join(dest_split[:-1])
    os.makedirs(dest_directory, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_string)
