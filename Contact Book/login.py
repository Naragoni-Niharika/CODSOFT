import tkinter as tk
from tkinter import messagebox
from ui import ContactBookApp  # Import the Contact Book UI

# Hardcoded username and password (for simplicity)
USER_CREDENTIALS = {"admin": "password123"}

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Contact Book")
        self.root.geometry("400x300")
        self.root.configure(bg="#d0e1f9")  # Light blue background

        # Title Label
        tk.Label(root, text="📘 Contact Book Login", font=("Arial", 14, "bold"), bg="#d0e1f9").pack(pady=10)

        # Username Label & Entry
        tk.Label(root, text="Username:", bg="#d0e1f9", font=("Arial", 12)).pack(pady=5)
        self.username_var = tk.StringVar()
        tk.Entry(root, textvariable=self.username_var, width=30).pack()

        # Password Label & Entry
        tk.Label(root, text="Password:", bg="#d0e1f9", font=("Arial", 12)).pack(pady=5)
        self.password_var = tk.StringVar()
        tk.Entry(root, textvariable=self.password_var, show="*", width=30).pack()

        # Login Button
        tk.Button(root, text="Login", command=self.validate_login, bg="#4CAF50", fg="white", width=15).pack(pady=15)

    def validate_login(self):
        """Validates login credentials and opens the Contact Book if correct."""
        username = self.username_var.get()
        password = self.password_var.get()

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            messagebox.showinfo("Login Successful", "Welcome to Contact Book!")
            self.root.destroy()  # Close the login window

            # Open Contact Book
            root = tk.Tk()
            ContactBookApp(root)
            root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
