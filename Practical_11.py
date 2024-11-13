import tkinter as tk

def create_login_page():
    root = tk.Tk()
    root.title("Login Page")

    # Create a frame for the login form
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    # Username label and entry
    username_label = tk.Label(frame, text="Username:")
    username_label.grid(row=0, column=0, pady=5)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=0, column=1, pady=5)

    # Password label and entry
    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=1, column=0, pady=5)
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, pady=5)

    # Login button
    login_button = tk.Button(frame, text="Login")
    login_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_login_page()