from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.labels_list = []
        self.init_main()

    def init_main(self):
        label_input = Label(text='Please input full name:')
        label_input.place(x=10, y=10)

        entry_firstName = Entry()
        entry_firstName.place(x=10, y=50)

        entry_lastName = Entry()
        entry_lastName.place(x=150, y=50)

        btn_add = Button(text='Add', padx=117, pady=5, command=self.push_user)
        btn_add.place(x=10, y=75)

        btn_pop = Button(text='Pop', padx=117, pady=5, command=self.pop_user)
        btn_pop.place(x=10, y=110)
        # label_warning = Label(text='Warning', fg='red', underline=True).place(x=10, y=25)

    def push_user(self):
        temp_label = Label(text='hbgg')
        temp_label.place(x=300, y=10+18*len(self.labels_list))
        self.labels_list.append(temp_label)

    def pop_user(self):
        if len(self.labels_list) > 0:
            self.labels_list[-1].destroy()
            self.labels_list.pop()



if __name__ == "__main__":
    root = Tk()
    root.geometry('600x800')
    app = Main(root)
    app.place()
    root.mainloop()
