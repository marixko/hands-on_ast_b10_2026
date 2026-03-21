import os
import sys
import json
import matplotlib.pyplot as plt

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def add_children_to_sys_path(directory):
    for root, dirs, _ in os.walk(directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if dir_path not in sys.path and dir_name != '__pycache__':
                sys.path.append(dir_path)


def setup_config(config_file_name):
    root_directory = os.path.abspath(os.getcwd())

    src_path = os.path.join(root_directory, "src")
    config_path = os.path.join(root_directory, "config")
    img_path = os.path.join(root_directory, 'img')
    data_path = os.path.join(root_directory, 'data')
    


    # Prepare config data
    config_data = {
            "root_path": root_directory,
            "codes_path": src_path,
            "data_path": data_path,
            "img_path": img_path
    }

    # Write to config.json
    with open(os.path.join(config_path, config_file_name), 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

     # Add all children directories to sys.path
    add_children_to_sys_path(src_path)

    print(f"Configuration file created at {config_path}/{config_file_name}")



if __name__ == "__main__":
    config_file_name = 'paths.json'

    setup_config(config_file_name)

    # Set plot visual settings
    paper_settings = {
    # Use LaTeX to write all text
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 10,
    'axes.titlesize': 10,
    "font.size": 10,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    # Enable axis grids
    "axes.grid": True,
    "grid.alpha": 0.5}
    plt.rcParams.update(paper_settings)