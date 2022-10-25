import time
import PyPDF2
from tkinter import *
from tkinter import filedialog

root = Tk()


def dest(yes):
    yes.pack_forget()


def done():
    yes = Label(root, text="Thanks for using our application", font=('Helvetica', 15))
    yes.pack()
    yes.after(3000, root.quit)


def merge_files():
    root.file_1 = filedialog.askopenfilename(title="Choose the first pdf file",
                                             filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    root.file_2 = filedialog.askopenfilename(title="Choose the first pdf file",
                                             filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdfs = PyPDF2.PdfFileMerger()
    pdfs.append(open(root.file_1, 'rb'))
    pdfs.append(open(root.file_2, 'rb'))
    pdfs.write(open('merged_pdf.pdf', 'wb'))
    yes = Label(root, text="Your file has been created successfully", font=('Helvetica', 15))
    yes.pack()


def extract_page():
    page_num = click.get()
    root.file_1 = filedialog.askopenfilename(title="Choose the file you want to extract a page from",
                                             filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    reader = PyPDF2.PdfFileReader(open(root.file_1, 'rb'))
    file_name = root.file_1.replace('.pdf', '')
    new_pdf = PyPDF2.PdfFileWriter()
    num_pages = reader.numPages
    new_pdf.addPage(reader.getPage(int(page_num) - 1))
    new_pdf.write(open(f"{file_name}-{page_num}.pdf", 'wb'))
    yes = Label(root, text="Your file has been created successfully", font=('Helvetica', 15))
    yes.pack()


def separate_file():
    root.file = filedialog.askopenfilename(title="Choose the file you want to extract a page from",
                                           filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    reader = PyPDF2.PdfFileReader(open(root.file, 'rb'))
    file_name = root.file.replace('.pdf', '')
    for i in range(0, reader.numPages):
        new_pdf = PyPDF2.PdfFileWriter()
        new_pdf.addPage(reader.getPage(i))
        new_pdf.write(open(f"{file_name}-{i + 1}.pdf", 'wb'))
    yes = Label(root, text="Your files have been created successfully", font=('Helvetica', 15))
    yes.pack()


root.title("PDF Separate and Merge Application")
root.iconbitmap('icon.ico')

Button1 = Button(root, text="Merge two pdf files", padx=118, pady=40, bg="#222831", font=('Helvetica', 25, "bold"),
                 fg="#FFFFFF",
                 command=merge_files)
Button2 = Button(root, text="Extract a page from a pdf file", padx=42, pady=40, bg="#064663",
                 font=('Helvetica', 25, "bold"), fg="#FFFFFF",
                 command=extract_page)
Button3 = Button(root, text="Split a pdf file into separate pages", pady=40, bg="#00ADB5", fg="#FFFFFF",
                 font=('Helvetica', 25, "bold"), command=separate_file)
Button4 = Button(root, text="Exit", bg="#DEEEEA", padx=236, pady=40, font=('Helvetica', 25, "bold"), fg="#000000",
                 command=done)
click = Entry(root, width=25, borderwidth=5, font=('Helvetica', 15))

message = Label(root, text="Enter page number to extract", font=('Helvetica', 20, "bold"))

Button1.pack()
Button2.pack()
message.pack()
click.pack(padx=5, pady=10)
Button3.pack()
Button4.pack()

root.mainloop()
