import os
import sys

def main():
    directory = input("What name do you want your directory ? ")
    parent_dir = input("What's the path (C:/xxxx/xxxx/) ? ")
    child_dir = input("Do you want any child directories y/n ?")

    if child_dir.upper() == "Y" or child_dir.upper() == "YES":
        count = input("How many ? ")
        child_count = "CV"
        
    elif child_dir.upper() == "N" or child_dir.upper() == "NO":
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
    else:
        print("Invalid input. Ending script.")
        sys.exit()


def printing():
    print("Done!")


main()
printing()



