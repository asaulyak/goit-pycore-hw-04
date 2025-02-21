from pathlib import Path
from colorama import Fore, Style

def traverse(path, depth=0):
    folder_path = Path(path)

    sorted_items = sorted(folder_path.iterdir(), key=lambda x: x.is_file())

    indent = '  ' * depth

    for item in sorted_items:
        if item.is_file():
            # Render a file with green text
            print(f"{Fore.GREEN}{indent}{item.name}{Style.RESET_ALL}")
        elif item.is_dir():
            # Render a folder with blue text
            print(f"{Fore.LIGHTBLUE_EX}{indent}{item.name}/{Style.RESET_ALL}")
            traverse(f'{path}/{item.name}', depth + 1)