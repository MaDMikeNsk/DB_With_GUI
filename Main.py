from tkinter import *
from DB_Engine import DB_Engine


class Main(Frame):
    def __init__(self, hidden_root):
        super().__init__(hidden_root)
        self.labels_list = []
        self.db = DB_Engine()
        self.init_main()
        self.warning = False

    def init_main(self):

        label_input = Label(text='Please input full name:')
        label_input.place(x=10, y=10)

        entry_first_name = Entry()
        entry_first_name.place(x=10, y=50)

        entry_last_name = Entry()
        entry_last_name.place(x=150, y=50)

        # self.name = entry_first_name.get() + entry_last_name.get()

        btn_add = Button(text='Add', padx=117, pady=5, command=lambda: self.add(entry_first_name, entry_last_name))
        btn_add.place(x=10, y=75)

        btn_pop = Button(text='Pop', padx=117, pady=5, command=self.pop)
        btn_pop.place(x=10, y=110)

    def add(self, entry_first, entry_last):
        name = entry_first.get() + ' ' + entry_last.get()
        if name != ' ':
            if self.warning:
                self.label_warning.place_forget()
            temp_label = Label(text=name)
            temp_label.place(x=300, y=10+18*len(self.labels_list))
            self.labels_list.append(temp_label)
            entry_first.delete(0, 'end')
            entry_last.delete(0, 'end')
            print(f"added ok. len = {len(self.labels_list)}")
            # self.view_records()
            """
            user = User(entry_first.get(), entry_last.get())
            self.db.push_user_to_db(user)
            """
        else:
            self.label_warning = Label(text='Please input name', fg='red', underline=True)
            self.label_warning.place(x=10, y=25)
            self.warning = True

    def pop(self):
        if len(self.labels_list) > 0:
            self.labels_list[-1].destroy()
            self.labels_list.pop()
            print(f"pop ok. len = {len(self.labels_list)}")
            # self.view_records()

    def view_records(self):
        i = 0
        for item in self.labels_list:
            item.place(x=300, y=10 + 18 * i)
            i += 1
        # for instance in self.db.session.query(User).order_by(User.id).all():
        #   lbl = Label() name=instance.first_name + ' ' + instance.last_name
        #   lbl.place() nf


if __name__ == "__main__":
    root = Tk()
    root.geometry('600x700')
    app = Main(root)
    app.place()
    root.mainloop()
