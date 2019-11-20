from tkinter import *
from DB_Engine import DB_Engine


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.labels_list = []
        self.db = DB_Engine()
        self.init_main()

    def init_main(self):
        frame = Frame(bg='Yellow')
        frame.place(x=10, y=10, width=490, height=490)

        label_input = Label(frame, text='Please input full name:')
        label_input.place(x=10, y=10)

        entry_firstName = Entry(frame)
        entry_firstName.place(x=10, y=50)

        entry_lastName = Entry(frame)
        entry_lastName.place(x=150, y=50)

        # self.name = entry_firstName.get() + entry_lastName.get()

        btn_add = Button(frame, text='Add', padx=117, pady=5, command=lambda: self.add(frame, entry_firstName,
                                                                                     entry_lastName))
        btn_add.place(x=10, y=75)

        btn_pop = Button(frame, text='Pop', padx=117, pady=5, command=self.pop)
        btn_pop.place(x=10, y=110)

    def add(self, frame, entry_first, entry_last):
        name = entry_first.get() + ' ' + entry_last.get()
        if name != ' ':
            temp_label = Label(frame, text=name)
            temp_label.place(x=300, y=10+18*len(self.labels_list))
            self.labels_list.append(temp_label)
            print(f"added ok. len = {len(self.labels_list)}")
            # self.view_records()
            """
            user = User(entry_first.get(), entry_last.get())
            self.db.push_user_to_db(user)
            """
        else:
            label_warning = Label(frame, text='Warning', fg='red', underline=True)
            label_warning.place(x=10, y=25)
            warning = True

    def pop(self):
        if len(self.labels_list) > 0:
            self.labels_list[-1].destroy()
            self.labels_list.pop()
            print(f"pop ok. len = {len(self.labels_list)}")
            # self.view_records()

    def view_records(self, frame):
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
