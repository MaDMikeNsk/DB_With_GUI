import tkinter as tk
from tkinter import ttk
from User import User
from DB_Engine import DB_Engine


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.warning = False
        self.db = db
        self.view_records()

    def init_main(self):
        # Label <First Name:>
        label_first_name = tk.Label(text='First name:')
        label_first_name.place(x=10, y=10)

        # Entry <first_name>
        entry_first_name = tk.Entry()
        entry_first_name.place(x=75, y=10)

        # Label <Last Name:>
        label_last_name = tk.Label(text='Last name:')
        label_last_name.place(x=210, y=10)

        # Entry <last_name>
        entry_last_name = tk.Entry()
        entry_last_name.place(x=275, y=10)

        # Button <Add User>
        btn_add_user = tk.Button(text='Add User', command=lambda: self.add_user(entry_first_name, entry_last_name),
                                 bg='#d7d8e0', padx=40, pady=10)
        btn_add_user.place(x=10, y=50)

        # Button <Delete User>
        btn_delete_user = tk.Button(text='Delete User', bg='#d7d8e0', command=self.delete_user,
                                    padx=40, pady=10)
        btn_delete_user.place(x=180, y=50)

        # Label <Warning>
        self.label_warning = tk.Label(text='Warning! Please input name', fg='red', underline=True)

        # Frame with table of users
        self.frame = tk.Frame()
        self.frame.place(x=10, y=110)

        # Table for visualization data
        self.tree = ttk.Treeview(self.frame, columns=('ID', 'first_name', 'last_name'),
                                 height=15, show='headings', selectmode='browse')
        self.tree.pack(side='left')
        self.tree.column("ID", width=35, anchor=tk.CENTER)
        self.tree.column("first_name", width=220, anchor=tk.CENTER)
        self.tree.column("last_name", width=220, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("first_name", text='First Name')
        self.tree.heading("last_name", text='Last Name')
        self.tree.pack()

    def add_user(self, entry_first, entry_last):
        name = entry_first.get() + ' ' + entry_last.get()
        if name != ' ':
            if self.warning:
                self.label_warning.place_forget()

            # Creating user and record him to database 'users.db'
            user = User(entry_first.get(), entry_last.get())
            self.db.insert_user(user)
            # Clean entry
            entry_first.delete(0, 'end')
            entry_last.delete(0, 'end')
            self.view_records()
        else:
            # Place Label <Warning>
            self.label_warning.place(x=10, y=30)
            self.warning = True

    def delete_user(self):
        for item in self.tree.selection():
            user_id = self.tree.item(item)['values'][0]
            self.db.delete_user(user_id)
        self.view_records()

    def view_records(self):
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=(user.id, user.first_name, user.last_name))
         for user in self.db.session.query(User).filter().all()]


if __name__ == "__main__":
    root = tk.Tk()
    db = DB_Engine()
    app = Main(root)
    app.pack()
    root.title("Таблица пользователей")
    root.geometry("500x500")
    root.resizable(False, False)
    root.mainloop()
