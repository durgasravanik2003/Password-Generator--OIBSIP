import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password(minlen, maxlen, minuchars, minlchars, minnumbers, minschars):
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure minimum characters from each category
    password = [
        random.choice(uppercase) for _ in range(minuchars)
    ] + [
        random.choice(lowercase) for _ in range(minlchars)
    ] + [
        random.choice(digits) for _ in range(minnumbers)
    ] + [
        random.choice(special_characters) for _ in range(minschars)
    ]

    # Fill the rest of the password length with random characters from all sets
    remaining_length = random.randint(minlen, maxlen) - len(password)
    all_characters = uppercase + lowercase + digits + special_characters
    password += [random.choice(all_characters) for _ in range(remaining_length)]
    
    # Shuffle the password list to avoid a predictable pattern
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Function to handle password generation
def handle_generate():
    try:
        # Get the values entered by the user
        minlen = int(entry_minlen.get())
        maxlen = int(entry_maxlen.get())
        minuchars = int(entry_minuchars.get())
        minlchars = int(entry_minlchars.get())
        minnumbers = int(entry_minnumbers.get())
        minschars = int(entry_minschars.get())

        if minlen < 6 or maxlen < minlen:
            messagebox.showerror("Input Error", "Ensure minimum length is 6 and max is greater than min.")
            return

        password = generate_password(minlen, maxlen, minuchars, minlchars, minnumbers, minschars)
        password_label.config(text=f"Your password is: {password}")

        # Ask the user if they're satisfied with the password
        if not messagebox.askyesno("Password Generator", "Is this password OK?"):
            handle_generate()  # Rerun if not satisfied
        else:
            root.quit()  # Exit the program if satisfied

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for all fields.")

# Create the GUI
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x500")  # Increased height for more space

# Create a frame with a cream-colored background
frame = tk.Frame(root, bg="light yellow", padx=20, pady=20, relief="groove", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Labels and Entries for inputs inside the frame
tk.Label(frame, text="Min Length:", bg="light yellow").grid(row=0, column=0, sticky="w", pady=5)
entry_minlen = tk.Entry(frame)
entry_minlen.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Max Length:", bg="light yellow").grid(row=1, column=0, sticky="w", pady=5)
entry_maxlen = tk.Entry(frame)
entry_maxlen.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Min Uppercase:", bg="light yellow").grid(row=2, column=0, sticky="w", pady=5)
entry_minuchars = tk.Entry(frame)
entry_minuchars.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Min Lowercase:", bg="light yellow").grid(row=3, column=0, sticky="w", pady=5)
entry_minlchars = tk.Entry(frame)
entry_minlchars.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Min Numbers:", bg="light yellow").grid(row=4, column=0, sticky="w", pady=5)
entry_minnumbers = tk.Entry(frame)
entry_minnumbers.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Min Special Chars:", bg="light yellow").grid(row=5, column=0, sticky="w", pady=5)
entry_minschars = tk.Entry(frame)
entry_minschars.grid(row=5, column=1, pady=5)

# Generate button inside the frame
tk.Button(frame, text="Generate Password", command=handle_generate).grid(row=6, column=0, columnspan=2, pady=10)

# Label to display the generated password
password_label = tk.Label(frame, text="", bg="light yellow", fg="blue", font=("Helvetica", 12))
password_label.grid(row=7, column=0, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
