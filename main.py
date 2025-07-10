""" Sorts the vocab files I add through obsidian into alphabetical folders """

import os

def main():
    
    # Change the working directory to the notes folder
    cwd = "/home/anuj/Documents/Notes/German/"
    os.chdir(cwd)

    # Store every content in a list
    contents = os.listdir(cwd)
    print(f"Initial : {contents}")

    # Remove all the files/folders that are not ".md" from it
    # List comprehension...
    contents = [c for c in contents if ".md" in c]

    for content in contents:
        initial = content[0:1].upper() 
        curr_path = cwd + content
        target = os.path.join(cwd, "Vocabulary/")

        # ord() gives ASCII value of a character
        val = ord(initial);
        
        # Deal with the special characters
        if initial == 'Ä':
            path = os.path.join("Vocabulary/A-C/", content)
            des = os.path.join(cwd, path)
            os.rename(curr_path, des)
            continue
        elif initial == 'Ö':
            path = os.path.join("Vocabulary/M-O/", content)
            des = os.path.join(cwd, path)
            os.rename(curr_path, des)
            continue
        elif initial == 'Ü' or initial == 'ß':
            path = os.path.join("Vocabulary/S-U/", content)
            des = os.path.join(cwd, path)
            os.rename(curr_path, des)
            continue
        elif ord('A') <= val and val <= ord('X'):
            # Because the names for Y-Z folders are different
            x = ord('A') 
            y = ord('C')
            while(x <= ord('X')):
                block = chr(x) + "-" + chr(y)
                path = os.path.join(target, block, content)
                if x <= val and y >= val:
                    os.rename(curr_path, path)
                    break
                # Because each folder contains 3 characters 
                x = x + 3
                y = y + 3
        else:
            path = cwd + "Vocabulary/Y-Z/" + content
            os.rename(curr_path, path)


main()