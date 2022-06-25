from tkinter import *


def iCalc(source, side):
    store_obj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


def button(source, side, text, command=None):
    store_obj = Button(source, text=text, command=command)
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('CalculatorPY_GUI by. coderpy4')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg='powder blue').pack(side=TOP, expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda store_obj=display, q=ichar: store_obj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            function_num = iCalc(self, TOP)
            for iEquals in numButton:
                button(function_num, LEFT, iEquals, lambda store_obj=display, q=iEquals: store_obj.set(store_obj.get() + q))

        equal_button = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btn_equals = button(equal_button, LEFT, iEquals)
                btn_equals.bind('<ButtonRelease-1>', lambda e, s=self, store_obj=display: s.calc(store_obj), '+')

            else:
                btn_equals = button(equal_button, LEFT, iEquals, lambda store_obj=display, s=' %s ' % iEquals: store_obj.set(store_obj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    app().mainloop()
    l = Label(text="What is 24 * 5 ? ")
