import tkinter as tk
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Use list comprehensions to generate the random characters
    # revise it 
    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_input.get()
    email = email_input.get()
    pas = password_input.get()
    new_data = {
        web: {
            "email": email,
            "password": pas
        }
    }

    if not web or not email or not pas:
        messagebox.showinfo(title="Ooops", message="Please don't leave anything blank")
    else:
        try:
            with open("passwords.json", "r") as file:
                # read the old data
                data = json.load(file) #it will give output in the form of dict

        except FileNotFoundError:
            with open("passwords.json", "a") as file:
                json.dump(new_data , file , indent=4)
        else:
            # update the old data with new data
            data.update(new_data)
            with open("passwords.json", "a") as file:
                # saving new data
                json.dump(data, file, indent=4)

            # with open("pss_mannager-29/passwords.txt", "a") as txt_file:
                # file.write(f"{web} | {email} | {pas}\n")

        finally:
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
# --------------------------- SEARCH PASSWORD ------------------------ #
def search_butten():
    webiste = website_input.get()
    try:
        with open("pss_mannager-29/passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error" , message="no data file found")
    else:
        if webiste in data:
            email = data[webiste]["email"]
            password = data[webiste]["password"]
            messagebox.showinfo(title="website" , message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="error" , message=f"No data found for {webiste}")
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20 , pady=20)

window.grid_columnconfigure(1, weight=0, minsize=1)
window.grid_columnconfigure(2, weight=0, minsize=1)

website_label = tk.Label(text="Website :")
website_label.grid(row=1 , column=0 , sticky="e")
email_label = tk.Label(text="Username/Email :")
email_label.grid(row=2 , column=0)
password_label = tk.Label(text="Password :")
password_label.grid(row=3 , column=0 , sticky="e")

# Create a frame for password entry and button
password_frame = tk.Frame(window)
password_frame.grid(row=3, column=1, columnspan=2, pady=5, sticky="w")

password_input = tk.Entry(password_frame, width=25)
password_input.pack(side="left")

gen_button = tk.Button(password_frame, text="Generate Password", width=15 , command=generate_pass)
gen_button.pack(side="left")

enter_button = tk.Button(text="Add" , width=36 , command=save)
enter_button.grid(row=4 , column=1 , columnspan=2 , sticky="w")

search_button = tk.Button(text="Search" , width=15 , command=search_butten)
search_button.grid(row=1 , column=2 )

website_input = tk.Entry(width=32)
website_input.grid(row=1 , column=1 , columnspan=2 , pady=5 , sticky="w")
website_input.focus()
email_input = tk.Entry(width=35)
email_input.grid(row=2 , column=1 ,columnspan=2 , pady=5, sticky="w")

canvas = tk.Canvas(width=200 , height=200 , bg="white" , highlightthickness=0)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image=image)
canvas.grid(row= 0 , column=1)

window.mainloop()