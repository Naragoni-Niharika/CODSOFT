import tkinter as tk
from tkinter import messagebox, filedialog
import csv
from database import add_contact, view_contacts, search_contact, update_contact, delete_contact

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x500")
        self.root.configure(bg="#d0e1f9")  # Light blue background

        # Labels and Entry Fields
        tk.Label(root, text="Name", bg="#d0e1f9", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_var = tk.StringVar()
        tk.Entry(root, textvariable=self.name_var, width=40).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Phone", bg="#d0e1f9", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_var = tk.StringVar()
        tk.Entry(root, textvariable=self.phone_var, width=40).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Email", bg="#d0e1f9", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_var = tk.StringVar()
        tk.Entry(root, textvariable=self.email_var, width=40).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Address", bg="#d0e1f9", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.address_var = tk.StringVar()
        tk.Entry(root, textvariable=self.address_var, width=40).grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#d0e1f9")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Add Contact", command=self.add_contact, bg="#4CAF50", fg="white", width=12).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="View Contacts", command=self.view_contacts, bg="#2196F3", fg="white", width=12).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Search", command=self.search_contact, bg="#FF9800", fg="white", width=12).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Export to CSV", command=self.export_contacts, bg="#795548", fg="white", width=12).grid(row=0, column=3, padx=5)

        # Contact List
        self.contact_list = tk.Listbox(root, width=60, height=10)
        self.contact_list.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.contact_list.bind("<<ListboxSelect>>", self.select_contact)

        # Update and Delete Buttons
        tk.Button(root, text="Update", command=self.update_contact, bg="#673AB7", fg="white", width=12).grid(row=6, column=0, pady=5)
        tk.Button(root, text="Delete", command=self.delete_contact, bg="#F44336", fg="white", width=12).grid(row=6, column=1, pady=5)

        self.selected_contact = None

    def add_contact(self):
        """Add a new contact and clear input fields."""
        name, phone, email, address = self.name_var.get(), self.phone_var.get(), self.email_var.get(), self.address_var.get()
        if name and phone:
            add_contact(name, phone, email, address)
            messagebox.showinfo("Success", "Contact added successfully")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Name and Phone are required!")

    def view_contacts(self):
        """Display all contacts in the listbox."""
        self.contact_list.delete(0, tk.END)
        contacts = view_contacts()
        for contact in contacts:
            self.contact_list.insert(tk.END, f"{contact[0]} - {contact[1]} ({contact[2]})")

    def search_contact(self):
        """Search contacts by name or phone."""
        term = self.name_var.get()
        self.contact_list.delete(0, tk.END)
        contacts = search_contact(term)
        for contact in contacts:
            self.contact_list.insert(tk.END, f"{contact[0]} - {contact[1]} ({contact[2]})")

    def select_contact(self, event):
        """Store selected contact for updating or deleting."""
        selected = self.contact_list.curselection()
        if selected:
            index = selected[0]
            contact_info = self.contact_list.get(index).split(" - ")
            self.selected_contact = int(contact_info[0])

    def update_contact(self):
        """Update selected contact details."""
        if self.selected_contact:
            update_contact(self.selected_contact, self.name_var.get(), self.phone_var.get(), self.email_var.get(), self.address_var.get())
            messagebox.showinfo("Success", "Contact updated successfully")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Select a contact first!")

    def delete_contact(self):
        """Delete selected contact."""
        if self.selected_contact:
            delete_contact(self.selected_contact)
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Select a contact first!")

    def export_contacts(self):
        """Export all contacts to a CSV file."""
        contacts = view_contacts()
        if not contacts:
            messagebox.showerror("Error", "No contacts to export!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Phone", "Email", "Address"])
                writer.writerows(contacts)
            messagebox.showinfo("Success", "Contacts exported successfully!")

    def clear_fields(self):
        """Clear input fields after adding, updating, or deleting a contact."""
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.view_contacts()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

