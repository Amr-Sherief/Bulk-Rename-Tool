import tkinter as tk

root = tk.Tk()
root.title("Bulk Rename Tool")
root.attributes('-fullscreen', True)

intro = tk.Label(root, text="This is a file renaming program", fg="Blue")
intro.pack()


def firstchoice():

    def button():
        #extension_list = list(str(old_path.get()).rsplit(".", 1))
        #extension = "." + str(extension_list[len(extension_list) - 1])
        #my_label_3 = tk.Label(root, text="Please insert the new name for the file with the " + extension)
        #my_label_3.pack()

    my_label = tk.Label(root, text="Please insert the full path of the file")
    my_label.pack()
    #old_path = tk.Entry(root, bg="black", fg="white", width=80)   # todo make this a dialog box
    #old_path.pack()
    #b = tk.Button(root, text="submit", command=button)
    #b.pack()


frame = tk.Frame(root)
frame.pack(side="top")
first_choice = tk.Button(frame, text="Rename one file", command=firstchoice).pack(side="left")
second_choice = tk.Button(frame, text="Rename multiple files").pack(side="left")

root.mainloop()

# todo add comments
# todo add a dialog box instead of inserting the path of the file