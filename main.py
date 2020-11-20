import os


print("Please one of these options:")
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
