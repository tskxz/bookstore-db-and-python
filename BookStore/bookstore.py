"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

# Import the tkinter library

from tkinter import *
import backend


# View all command
def view_command():
    Box.delete(0, END)
    for row in backend.view():
        Box.insert(END, row)


# Search entry command
def search_command():
    Box.delete(0, END)
    for row in backend.search(title_value.get(), author_value.get(), year_value.get(), ISBN_value.get()):
        Box.insert(END, row)


# Add entry command
def add_command():
    backend.insert(title_value.get(), author_value.get(), year_value.get(), ISBN_value.get())
    Box.delete(0, END)
    Box.insert(END, (title_value.get(), author_value.get(), year_value.get(), ISBN_value.get()))


# Select data
def get_selected_row(event):
    try:
        global selected_tuple
        index = Box.curselection()[0]
        selected_tuple = Box.get(index)
        title_entry.delete(0, END)
        title_entry.insert(END, selected_tuple[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[3])
        ISBN_entry.delete(0, END)
        ISBN_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass


# Delete selected command
def delete_command():
    backend.delete(selected_tuple[0])


# Update selected command
def update_command():
    backend.update(selected_tuple[0], title_value.get(), author_value.get(), year_value.get(), ISBN_value.get())


# Create a window
window = Tk()
window.wm_title("BookStore")
# Title entry
title = Label(window, text="Title")
title.grid(row=0, column=0)
title_value = StringVar()
title_entry = Entry(window, textvariable=title_value)
title_entry.grid(row=0, column=1)

# Author entry
author = Label(window, text="Author")
author.grid(row=0, column=2)
author_value = StringVar()
author_entry = Entry(window, textvariable=author_value)
author_entry.grid(row=0, column=3)

# Year entry
year = Label(window, text="Year")
year.grid(row=1, column=0)
year_value = StringVar()
year_entry = Entry(window, textvariable=year_value)
year_entry.grid(row=1, column=1)

# ISBN entry
ISBN = Label(window, text="ISBN")
ISBN.grid(row=1, column=2)
ISBN_value = StringVar()
ISBN_entry = Entry(window, textvariable=ISBN_value)
ISBN_entry.grid(row=1, column=3)

# List Box
Box = Listbox(window, height=6, width=35)
Box.grid(row=2, column=0, rowspan=6, columnspan=2)

Box.bind('<<ListboxSelect>>', get_selected_row)

# Scroll bar
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2)
Box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=Box.yview)

# Buttons
view_all = Button(window, text="View all", height=1, width=10, command=view_command)
view_all.grid(row=2, column=3)

search_entry = Button(window, text="Search entry", height=1, width=10, command=search_command)
search_entry.grid(row=3, column=3)

add_entry = Button(window, text="Add entry", height=1, width=10, command=add_command)
add_entry.grid(row=4, column=3)

update = Button(window, text="Update selected", height=1, width=10, command=update_command)
update.grid(row=5, column=3)

delete = Button(window, text="Delete selected", height=1, width=10, command=delete_command)
delete.grid(row=6, column=3)

close = Button(window, text="Close", command=window.quit, height=1, width=10)
close.grid(row=7, column=3)

# Put the window
window.mainloop()
