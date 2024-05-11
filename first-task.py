import os
import shutil
import sys

def copy_files_recursively(source_dir, target_dir):
    try:
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            if os.path.isdir(source_item):
                copy_files_recursively(source_item, target_dir)
            elif os.path.isfile(source_item):
                ext = os.path.splitext(item)[1].lower()
                if ext == '':
                    ext = 'no_extension'
                extension_dir = os.path.join(target_dir, ext)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)
                shutil.copy(source_item, extension_dir)
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_dir> [<target_dir>]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"
    
    if not os.path.exists(source_dir):
        print("The source directory does not exist.")
        sys.exit(1)
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    copy_files_recursively(source_dir, target_dir)
    print(f"Files have been copied to {target_dir}")

if __name__ == "__main__":
    main()
