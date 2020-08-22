import os
import glob


def get_output_dir(input_dir, output_dir):
    output_dir_name = os.path.join(input_dir, output_dir)

    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name)

    return output_dir_name


def get_output_file_path(input_dir, output_dir, file_name):
    output_dir_name = os.path.join(input_dir, output_dir)

    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name)

    return os.path.join(output_dir_name, file_name)


def get_input_files(input_folder):
    input_files = glob.glob(os.path.join(input_folder, '*.tcx'))
    if not input_files:
        quit('No Files found in Folder: ' + input_folder)
    else:
        return input_files


def get_input_dir():
    user_input_dir = input('TCX Input Folder: ')
    check_user_input_dir(user_input_dir)
    return os.path.abspath(user_input_dir)


def check_user_input_dir(input_dir):
    if not os.path.isdir(input_dir):
        print("Directory does not exist")
        get_input_dir()
    else:
        print("Directory is valid - proceeding...")


def get_template_path(template_name):
    return os.path.join(os.path.dirname(__file__), template_name)
