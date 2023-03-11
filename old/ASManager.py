import random
import csv
from typing import  List
from mimesis import Person
from tkinter import *
'''
All code meets the requirements of J. Grass, which he outlined in his book "Data Science from the Ground Up".
The program was created for personal use only.
'''
def generate_password(length: int) -> str:
    """Generates a password with length characters"""
    chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = "".join(random.choice(chars) for _ in range(length))
    return password

def generate_email() -> str:
    """Generates a random email address"""
    person = Person('en')
    email = person.email(domains=['gmail.com'])
    return email

def generate_email_password_pairs(num_pairs: int, password_length: int) -> List[str]:
    """Generates num_pairs random email:password pairs"""
    pairs = []
    for _ in range(num_pairs):
        email = generate_email()
        password = generate_password(password_length)
        pair = f"{email}:{password}"
        pairs.append(pair)
    return pairs

def save_pairs_to_csv(pairs: List[str], filename: str) -> None:
    """Saves email:password pairs to a CSV file"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'email', 'password'])
        for i, pair in enumerate(pairs):
            email, password = pair.split(':')
            writer.writerow([i+1, email, password])

def generate_pairs() -> None:
    """Generates email:password pairs and displays them in the GUI"""
    num_pairs = int(num_pairs_entry.get())
    password_length = int(password_length_entry.get())
    pairs = generate_email_password_pairs(num_pairs, password_length)
    pairs_text.delete(1.0, END)
    for pair in pairs:
        pairs_text.insert(END, pair + '\n')

def clear_fields() -> None:
    """Clears the input fields and the generated pairs"""
    num_pairs_entry.delete(0, END)
    password_length_entry.delete(0, END)
    pairs_text.delete(1.0, END)

def save_pairs() -> None:
    """Generates and saves email:password pairs to a CSV file"""
    num_pairs = int(num_pairs_entry.get())
    password_length = int(password_length_entry.get())
    pairs = generate_email_password_pairs(num_pairs, password_length)
    filename = 'pairs.csv'
    save_pairs_to_csv(pairs, filename)

# Create the main window
root = Tk()
root.title("ASManager")

# Create the input fields
num_pairs_label = Label(root, text="Number of pairs:")
num_pairs_label.grid(row=0, column=0, padx=5, pady=5)
num_pairs_entry = Entry(root)
num_pairs_entry.grid(row=0, column=1, padx=5, pady=5)

password_length_label = Label(root, text="Password length:")
password_length_label.grid(row=1, column=0, padx=5, pady=5)
password_length_entry = Entry(root)
password_length_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the buttons
generate_button = Button(root, text="Generate pairs", command=generate_pairs)
generate_button.grid(row=2, column=0, padx=5, pady=5)

clear_button = Button(root, text="Clear fields", command=clear_fields)
clear_button.grid(row=2, column=1, padx=5, pady=5)

save_button = Button(root, text="Save pairs to CSV", command=save_pairs)
save_button.grid(row=2, column=2, padx=5, pady=5)

pairs_label = Label(root, text="Generated email:password pairs:")
pairs_label.grid(row=3, column=0, padx=5, pady=5, columnspan=3)

pairs_text = Text(root, height=10, width=50)
pairs_text.grid(row=4, column=0, padx=5, pady=5, columnspan=3)

root.mainloop()

