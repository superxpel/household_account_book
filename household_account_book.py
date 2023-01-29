import tkinter as tk
import csv
from tkinter import messagebox

def save_data():
    date = entry_date.get()
    category = entry_category.get()
    amount = entry_amount.get()
    description = entry_description.get()

    with open('household_account_book.csv', 'a', encoding='cp949', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['날짜', '분류', '금액', '내용'])
        writer.writerow([date, category, amount, description])
    
    messagebox.showinfo('Information', 'Data saved successfully!')
    entry_date.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_description.delete(0, tk.END)

app = tk.Tk()
app.title('Household Account Book')

label_date = tk.Label(text='날짜:')
label_date.grid(row=0, column=0, padx=5, pady=5)

entry_date = tk.Entry(width=20)
entry_date.grid(row=0, column=1, padx=5, pady=5)

label_category = tk.Label(text='분류:')
label_category.grid(row=1, column=0, padx=5, pady=5)

entry_category = tk.Entry(width=20)
entry_category.grid(row=1, column=1, padx=5, pady=5)

label_amount = tk.Label(text='금액:')
label_amount.grid(row=2, column=0, padx=5, pady=5)

entry_amount = tk.Entry(width=20)
entry_amount.grid(row=2, column=1, padx=5, pady=5)

label_description = tk.Label(text='내용:')
label_description.grid(row=3, column=0, padx=5, pady=5)

entry_description = tk.Entry(width=20)
entry_description.grid(row=3, column=1, padx=5, pady=5)

button_save = tk.Button(text='Save', command=save_data)
button_save.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
