import os

while True:
    print("Please choose one of these options:")
    print("1: Rename the file normally")
    print("2: Rename multiple files in a sequence")
    choice = int(input())

    if choice == 1:
        print("Please insert the full path for the file to rename:")
        old_path = input()
        extension_list = old_path.split(".")
        extension = "." + str(extension_list[len(extension_list) - 1])
        print("Please insert the new name for the file with the " + extension)
        new_name = input()
        directory_split_list = old_path.rsplit('\\', 1)
        new_path = str(directory_split_list[0]) + "\\" + str(new_name)
        os.rename(old_path, new_path)

    elif choice == 2:
        print("Please insert the file path:")
        file_path = input()
        files_list = os.listdir(file_path)
        print("Choose one of these options:")
        print("1: rename all files in the folder")
        print("2: rename certain files in the folder")
        choice_2 = int(input())
        if choice_2 == 1:

        if choice_2 == 2:

        else:

    else:
        continue
# todo add a while true if choice_2 isn't 1 or 2
# todo add colors
# todo add more comments
# todo add try/except statement for ValueError