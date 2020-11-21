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
        break

    elif choice == 2:
        print("Please insert the file path:")
        file_path = input()
        files_list = os.listdir(file_path)
        print("Choose one of these options:")
        print("1: rename all files in the folder")
        print("2: rename certain files in the folder")
        choice_2 = int(input())
        if choice_2 == 1:

            files = os.listdir(file_path)

            print("Please insert the new name for the files with no numbers")
            name = str(input())

            print("Please insert the number to start with")
            number = int(input())

            print("Please insert the character between " + name + " " + str(number))
            splitter = str(input())

            for file in files:
                extension_list = file.rsplit(".", 1)
                extension = "." + extension_list[len(extension_list) - 1]
                new_name = name + splitter + str(number) + extension
                new_path = file_path + "\\" + new_name
                old_path = file_path + "\\" + file
                os.rename(old_path, new_path)
                number = number + 1
                if file == files[len(files) - 1]:
                    print("Done!")

            break

        elif choice_2 == 2:

            files = os.listdir(file_path)

            number = 1

            for file in files:
                print(str(number) + "- " + file)
                number = number + 1
            break
    else:
        continue
# todo add a while true if choice_2 isn't 1 or 2
# todo add colors
# todo add more comments
# todo add try/except statement for ValueError
# todo add FileNotFoundError
