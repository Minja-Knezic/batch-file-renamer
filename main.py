import os

def batch_rename(directory, prefix="", suffix="", replace=None, extension=None, rename_dirs=False):
    """
    Rename files and optionally directories in the specified directory with optional prefix, suffix, or replacement.

    Args:
        directory (str): Path to the directory containing files and directories.
        prefix (str): Text to add as a prefix to the name.
        suffix (str): Text to add as a suffix to the name.
        replace (tuple): Tuple containing text to replace (old, new).
        extension (str): If specified, only files with this extension will be renamed.
        rename_dirs (bool): If True, directories will also be renamed.
    """
    try:
        items = os.listdir(directory)
        for item_name in items:
            item_path = os.path.join(directory, item_name)
            
            # Handle directories
            if os.path.isdir(item_path):
                if rename_dirs:
                    new_name = item_name
                    if replace:
                        new_name = new_name.replace(replace[0], replace[1])
                    new_name = f"{prefix}{new_name}{suffix}"
                    new_path = os.path.join(directory, new_name)
                    os.rename(item_path, new_path)
                    print(f"Renamed directory: {item_name} -> {new_name}")
                continue
            
            # Handle files
            if extension and not item_name.endswith(extension):
                continue
            
            # Extract file name and extension
            name, ext = os.path.splitext(item_name)
            
            # Apply transformations
            new_name = name
            if replace:
                new_name = new_name.replace(replace[0], replace[1])
            new_name = f"{prefix}{new_name}{suffix}{ext}"
            
            # Rename the file
            new_path = os.path.join(directory, new_name)
            os.rename(item_path, new_path)
            print(f"Renamed file: {item_name} -> {new_name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get user inputs
    directory = input("Enter the directory path: ").strip()
    prefix = input("Enter prefix (or leave blank): ").strip()
    suffix = input("Enter suffix (or leave blank): ").strip()
    replace_old = input("Text to replace (or leave blank): ").strip()
    replace_new = input("Replacement text (or leave blank): ").strip() if replace_old else None
    extension = input("Filter by file extension (e.g., .txt) or leave blank for all: ").strip()
    rename_dirs = input("Do you want to rename directories as well? (yes/no): ").strip().lower() == "yes"
    
    # Call the renaming function
    batch_rename(
        directory,
        prefix=prefix,
        suffix=suffix,
        replace=(replace_old, replace_new) if replace_old else None,
        extension=extension,
        rename_dirs=rename_dirs
    )
