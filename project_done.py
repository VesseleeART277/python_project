import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

##Code by: Vesselee G.Flomo from the IT department @ Apex University, June 10, 2026
saved_data = {}

def update_data():
    # update values  
    first = entry_first_name.get()
    last = entry_last_name.get()
    student_id = entry_id.get()

    # Validation
    if not first or not last or not student_id:
        messagebox.showerror("Error", "Please fill required fields before updating.")
        return None

    # Store updated data
    data = {
        "first_name": first,
        "last_name": last,
        "student_id": student_id
    }

    # show database if it is accurate
    if student_id in saved_data:
        saved_data[student_id].update(data)

    messagebox.showinfo("Success", "Data updated successfully!")
    clear_fields()
    return data

def confirm_exit():
    confirm = messagebox.askyesno("Confirm Exit", "Are you sure you want to cancel and exit?")
    if confirm:
        root.destroy()

### clear fields done by vesselee
def clear_fields():
    # Student
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_gender.set("")
    entry_email_address.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_department.set("")
    entry_address.delete(0, tk.END)
    entry_contact.delete(0, tk.END)

    # Father
    entry_father_first_name.delete(0, tk.END)
    entry_father_last_name.delete(0, tk.END)
    entry_father_address.delete(0, tk.END)
    entry_father_contact.delete(0, tk.END)

    # Mother
    entry_mother_first_name.delete(0, tk.END)
    entry_mother_last_name.delete(0, tk.END)
    entry_mother_address.delete(0, tk.END)
    entry_mother_contact.delete(0, tk.END)

# students info/ details
def submit_details():
    # --real info about student--
    first = entry_first_name.get()
    last = entry_last_name.get()
    gender = entry_gender.get()
    email = entry_email_address.get()
    student_id = entry_id.get()
    department = entry_department.get()
    address = entry_address.get()
    contact = entry_contact.get()

    # find parent info here!
    father_first = entry_father_first_name.get()
    father_last = entry_father_last_name.get()
    father_address = entry_father_address.get()
    father_contact = entry_father_contact.get()

    mother_first = entry_mother_first_name.get()
    mother_last = entry_mother_last_name.get()
    mother_address = entry_mother_address.get()
    mother_contact = entry_mother_contact.get()

    # Validation starts here
    if first == "" or last == "" or student_id == "":
        messagebox.showerror("Error", "Please fill in all required student fields.")
        return

    if father_first == "" or mother_first == "":
        messagebox.showerror("Error", "Please provide parent information.")
        return

    # let us use student ID key
    saved_data[student_id] = {
        "first_name": first,
        "last_name": last,
        "gender": gender,
        "email": email,
        "student_id": student_id,
        "department": department,
        "address": address,
        "contact": contact,
        "father_first": father_first,
        "father_last": father_last,
        "father_address": father_address,
        "father_contact": father_contact,
        "mother_first": mother_first,
        "mother_last": mother_last,
        "mother_address": mother_address,
        "mother_contact": mother_contact
    }

    messagebox.showinfo("Success", "Details submitted successfully!")
    clear_fields()

### searching all data created by Vesselee
def search_data():
    student_id = entry_search.get().strip()
    if student_id == "":
        messagebox.showerror("Error", "Please enter Student ID to search.")
        return

    if student_id not in saved_data:
        messagebox.showwarning("Not Found", "No record found for this Student ID.")
        return

    data = saved_data[student_id]

    # I am clearing this field first
    clear_fields()

    # my student info
    entry_first_name.insert(0, data["first_name"])
    entry_last_name.insert(0, data["last_name"])
    entry_gender.set(data["gender"])
    entry_email_address.insert(0, data["email"])
    entry_id.insert(0, data["student_id"])
    entry_department.set(data["department"])
    entry_address.insert(0, data["address"])
    entry_contact.insert(0, data["contact"])

    # here include father info
    entry_father_first_name.insert(0, data["father_first"])
    entry_father_last_name.insert(0, data["father_last"])
    entry_father_address.insert(0, data["father_address"])
    entry_father_contact.insert(0, data["father_contact"])

    # let us use here for mother Info
    entry_mother_first_name.insert(0, data["mother_first"])
    entry_mother_last_name.insert(0, data["mother_last"])
    entry_mother_address.insert(0, data["mother_address"])
    entry_mother_contact.insert(0, data["mother_contact"])

    messagebox.showinfo("Success", "Record found and loaded successfully!")


### Main Application Window Configuration
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("1280x750")  # Slightly expanded height to cleanly accommodate the warning labels

# --- VALIDATION LOGIC DECLARED  BEFORE WIDGETS ---
def validate_numbers(text):
    # Allows empty string (so backspaces work) or strictly digits
    if text == "" or text.isdigit():
        return True
    else:
        root.bell()  # Triggers fallback alert sound
        return False

# Registering validation command capability##
vcmd = (root.register(validate_numbers), '%P')

banner = tk.Frame(root, bg="orange", height=50)
banner.pack(side="top", fill="x")

heading = tk.Label(banner, text="Student Detail Form", font=("Arial", 35 , "bold"), bg="Blue", fg="white")
heading.pack(pady=15)

# my student form#
form_frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
form_frame.pack(pady=10, fill="x")

# expanding columns dynamically
for i in range(4):
    form_frame.grid_columnconfigure(i, weight=1)

# Title
tk.Label(form_frame, text="Student Information", font=("Arial", 24, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

# First Name
tk.Label(form_frame, text="First Name", bg="blue", fg="white").grid(row=1, column=0, padx=2, pady=5, sticky="e")
entry_first_name = tk.Entry(form_frame, width=28)
entry_first_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Last Name
tk.Label(form_frame, text="Last Name", bg="blue", fg="white").grid(row=1, column=2, padx=10, pady=5, sticky="e")
entry_last_name = tk.Entry(form_frame, width=28)
entry_last_name.grid(row=1, column=3, padx=10, pady=5, sticky="w")

# Gender
tk.Label(form_frame, text="Gender", bg="blue", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_gender = ttk.Combobox(form_frame, values=["Male", "Female"], width=26, state="readonly")
entry_gender.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Email address
tk.Label(form_frame, text="Email Address", bg="blue", fg="white").grid(row=2, column=2, padx=10, pady=5, sticky="e")
entry_email_address = tk.Entry(form_frame, width=28)
entry_email_address.grid(row=2, column=3, padx=10, pady=5, sticky="w")

# Label & Student ID Widget with active text interception
tk.Label(form_frame, text="Student ID", bg="blue", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="e")

# A composite frame layout ensures the warning sits clean next to the Entry box without breaking grid columns
id_container = tk.Frame(form_frame)
id_container.grid(row=3, column=1, padx=10, pady=5, sticky="w")

entry_id = tk.Entry(id_container, width=20, validate="key", validatecommand=vcmd)
entry_id.pack(side="left")

# Red Explicit warning sign label requested for the numbers-only field
lbl_warning = tk.Label(id_container, text=" (*) Numbers Only", fg="red", font=("Arial", 10, "bold"))
lbl_warning.pack(side="left", padx=2)

# Department
tk.Label(form_frame, text="Department", bg="blue", fg="white").grid(row=3, column=2, padx=10, pady=5, sticky="e")
entry_department = ttk.Combobox(form_frame, values=["Civil Engineering", "Accountant", "Computer Science", "Nursing"],
                                width=26, state="readonly")
entry_department.grid(row=3, column=3, padx=10, pady=5, sticky="w")

# home address
tk.Label(form_frame, text="Address", bg="blue", fg="white").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_address = tk.Entry(form_frame, width=28)
entry_address.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# All contact info
tk.Label(form_frame, text="Contact", bg="blue", fg="white").grid(row=4, column=2, padx=10, pady=5, sticky="e")
entry_contact = tk.Entry(form_frame, width=28)
entry_contact.grid(row=4, column=3, padx=10, pady=5, sticky="w")

# my parent
form_frame1 = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
form_frame1.pack(pady=10, fill="x")

for i in range(4):
    form_frame1.grid_columnconfigure(i, weight=1)

tk.Label(form_frame1, text="Parent Information", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

# Father Info
tk.Label(form_frame1, text="Father's First Name", bg="blue", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_father_first_name = tk.Entry(form_frame1, width=28)
entry_father_first_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Label(form_frame1, text="Father's Last Name", bg="blue", fg="white").grid(row=1, column=2, padx=10, pady=5, sticky="e")
entry_father_last_name = tk.Entry(form_frame1, width=28)
entry_father_last_name.grid(row=1, column=3, padx=10, pady=5, sticky="w")

tk.Label(form_frame1, text="Address", bg="blue", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_father_address = tk.Entry(form_frame1, width=28)
entry_father_address.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(form_frame1, text="Contact", bg="blue", fg="white").grid(row=2, column=2, padx=10, pady=5, sticky="e")
entry_father_contact = tk.Entry(form_frame1, width=28)
entry_father_contact.grid(row=2, column=3, padx=10, pady=5, sticky="w")

# Mother info
tk.Label(form_frame1, text="Mother's First Name", bg="blue", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_mother_first_name = tk.Entry(form_frame1, width=28)
entry_mother_first_name.grid(row=3, column=1, padx=10, pady=5, sticky="w")

tk.Label(form_frame1, text="Mother's Last Name", bg="blue", fg="white").grid(row=3, column=2, padx=10, pady=5, sticky="e")
entry_mother_last_name = tk.Entry(form_frame1, width=28)
entry_mother_last_name.grid(row=3, column=3, padx=10, pady=5, sticky="w")

tk.Label(form_frame1, text="Address", bg="blue", fg="white").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_mother_address = tk.Entry(form_frame1, width=28)
entry_mother_address.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Label(form_frame1, text="Contact", bg="blue", fg="white").grid(row=4, column=2, padx=10, pady=5, sticky="e")
entry_mother_contact = tk.Entry(form_frame1, width=28)
entry_mother_contact.grid(row=4, column=3, padx=10, pady=5, sticky="w")

# Search form section
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search by Student ID:", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=5)

# Added validation checking to the search bar as well to protect search querying
entry_search = tk.Entry(search_frame, width=25, font=("Arial", 11), validate="key", validatecommand=vcmd)
entry_search.grid(row=0, column=1, padx=5)

tk.Button(search_frame, text="Search", width=12, bg="white", command=search_data).grid(row=0, column=2, padx=5)

# Button control layout section
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Submit", width=15, bg="green", fg="white", command=submit_details).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Update", width=15, bg="blue", fg="white", command=update_data).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Cancel", width=15, bg="red", fg="white", command=confirm_exit).grid(row=0, column=2, padx=10)

# Run app
root.mainloop()