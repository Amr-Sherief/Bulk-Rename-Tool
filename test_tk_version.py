import pytest


@pytest.fixture
def values():
    file_menu = "E:/Python/My Projects/Bulk Rename Tool/my_files/why.txt"
    return file_menu


def test_button_4(values):

    files_split = "-"                     # reassigns the files splitting character
    files_number = 1                      # reassign the files first number to index with the renamed files
    files_name = "example"                # the core name of the file
    extension_list = values.rsplit(".", 1)  # Splits the file path to get the file extension
    extension = "." + extension_list[1]  # Defines the extension of the file
    old_path = extension_list[0] + extension  # Defines the old path for the file remark before renaming
    folder_path = values.rsplit("/", 1)  # Splits th file path to get the folder
    folder_path_1 = folder_path[0] + "/"  # Defines the folder path
    new_path = folder_path_1 + files_name + files_split + str(files_number) + extension
    # defines the new path for the file with the new name
    change = folder_path[1] + " --> " + files_name + files_split + str(files_number) + extension
    # a variable containing text which shows the change in the files names remark after being renamed
    files_number = int(files_number) + 1
    # increments the variable every time the for loop ends to change the index number in every file
    assert extension_list == ["E:/Python/My Projects/Bulk Rename Tool/my_files/why", "txt"]
    assert extension == ".txt"
    assert old_path == "E:/Python/My Projects/Bulk Rename Tool/my_files/why.txt"
    assert folder_path == ["E:/Python/My Projects/Bulk Rename Tool/my_files", "why.txt"]
    assert folder_path_1 == "E:/Python/My Projects/Bulk Rename Tool/my_files/"
    assert new_path == "E:/Python/My Projects/Bulk Rename Tool/my_files/example-1.txt"
    assert change == "why.txt --> example-1.txt"
    assert files_number == 2
