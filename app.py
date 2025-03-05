# import tkinter as tk
from six.moves import tkinter as tk # type: ignore
from tkinter import filedialog, messagebox
from tkinter import ttk

from utils import extract_pdf_metadata, edit_pdf_metadata

root = tk.Tk()
root.title("Metadata Checker")
root.geometry("500x400")


file_path = ''


def select_file():
    global file_path, message_var
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("PDF Files", "*.pdf")])
    pdf_metadata = extract_pdf_metadata(file_path)
    message_var.set("File: " + file_path + "\n" + pdf_metadata + "\n\n Incorrect metadata?")

    open_form_button = tk.Button(root, text="Edit metadata", command=open_modal_form)
    open_form_button.pack(pady=40)

def open_modal_form():
    # Create a modal dialog window
    global file_path, message_var
    modal = tk.Toplevel(root)
    modal.title("Edit Metadata")
    modal.geometry("500x300")
    modal.grab_set()  # Make it modal (disables interaction with main window)
    
    # Form fields
    tk.Label(modal, text="Author:").pack(pady=5)
    name_entry = tk.Entry(modal)
    name_entry.pack(pady=5)
    
    tk.Label(modal, text="Title:").pack(pady=5)
    email_entry = tk.Entry(modal)
    email_entry.pack(pady=5)
    
    # Submit button
    def submit_form():
        author = name_entry.get()
        title = email_entry.get()

        print(author, title)
        
        if author and title:
            messagebox.showinfo("Form Submitted", f"Author: {author}\nTitle: {title}")
            pdf_metadata = edit_pdf_metadata(file_path, author, title)
            message_var.set("File: " + file_path + "\n" + pdf_metadata + "\n\n Incorrect metadata?")
            modal.destroy()  # Close the modal after submission
        else:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
    
    submit_button = tk.Button(modal, text="Submit", command=submit_form)
    submit_button.pack(pady=15)
    
    # Optional: Close button
    close_button = tk.Button(modal, text="Cancel", command=modal.destroy, padx=10, pady=5)
    close_button.pack()


select_button = tk.Button(root, text="Select File to see metadata", command=select_file, padx=10, pady=5)
select_button.pack(pady=10)

message_var = tk.StringVar()
message_var.set("")
message = tk.Message(root, textvariable=message_var, width=300, font=("Arial", 12))
message.pack(padx=20, pady=20) 

# 


root.mainloop()