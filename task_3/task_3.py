import sys
from pathlib import Path
from colorama import Fore, Style

def traverse(path, depth=0):
    folder_path = Path(path)

    try:
        sorted_items = sorted(folder_path.iterdir(), key=lambda x: x.is_file())

        indent = '  ' * depth

        for item in sorted_items:
            if item.is_file():
                print(f"{Fore.GREEN}{indent}{item.name}{Style.RESET_ALL}")
            elif item.is_dir():
                print(f"{Fore.LIGHTBLUE_EX}{indent}{item.name}/{Style.RESET_ALL}")
                traverse(f'{path}/{item.name}', depth + 1)
    except Exception as e:
        print(e)

def main():
    path = sys.argv[1]
    traverse(path)

if __name__ == "__main__":
    main()