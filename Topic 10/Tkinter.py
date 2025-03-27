#!/usr/bin/env python3

"""
Title: Tkinter.py - Show a Tkinter GUI Dialog Box
Author: Alan MacDonald
Date: 27/03/2025

This program demonstrates use of the Tkinter GUI library.

Observations:
    I relied on the following sources for information on left aligning
    the controls, and setting the width of the text boxes:

    https://stackoverflow.com/questions/73159989/align-radio-buttons-horizontally-in-python-using-tkinter?rq=3
    https://python-list.python.narkive.com/iAJ6ZkR0/tkinter-text-width

"""

# ============================================ #
# //             Module imports             // #
# ============================================ #


from tkinter import (
    BOTH,
    Button,
    Checkbutton,
    Entry,
    Frame,
    IntVar,
    Label,
    Tk,
    Radiobutton,
    X
)
# -------------------------------------------- #
# //               Main function            // #
# -------------------------------------------- #


class TkinterApp:
    """
    This is the main GUI class.
    """

    def __init__(self, master):
        self.master = master
        master.title("Tkinter in Python3")

        # Set size of application window
        master.geometry("700x400")
        # ------------------------------------------------------ #
        Label(master, font=3, height=0).pack(fill=X)

        # ------------------------------------------------------ #
        # Window label
        self.label = Label(
            master,
            text="Python3 course questionnaire",
            fg="red",
            font="Helvetica 14 bold",
        )
        self.label.pack()

        # ------------------------------------------------------ #
        Label(master, font=3, height=0).pack(fill=X)

        # ------------------------------------------------------ #
        # Student Name text box
        self.entry_box = Entry(master)
        self.entry_box.insert(20, "Student name")
        self.entry_box.pack()

        # Left align label frame.
        self.enjoy_label_frame = Frame()
        self.enjoy_label_frame.pack(fill=BOTH)

        # ------------------------------------------------------ #
        # Are you enjoying the course label
        self.label = Label(
            self.enjoy_label_frame,
            text="Are you enjoying this course?",
            font="Helvetica 12 bold",
            justify="left",
        )
        self.label.pack(side="left")

        # ------------------------------------------------------ #
        # Radio Buttons section

        # Radio buttons frame.
        self.radio_buttons_frame = Frame()
        self.radio_buttons_frame.pack(fill=BOTH)

        self.rb_choices = [
            ("It is very good", 1),
            ("It is somewhat good", 2),
            ("Neutral", 3),
            ("It is not very good", 4),
            ("It is not at all good", 5),
        ]

        self.rb_var = IntVar()

        for lang, val in self.rb_choices:
            self.rb = Radiobutton(
                self.radio_buttons_frame,
                text=lang,
                variable=self.rb_var,
                value=val
            )
            self.rb.pack(side="left")

        # ------------------------------------------------------ #
        Label(master, font=3, height=0).pack(fill=X)

        # ------------------------------------------------------ #
        # The sections most interesting to me are label

        # Left align label frame.
        self.interesting_label_frame = Frame()
        self.interesting_label_frame.pack(fill=BOTH)

        self.label = Label(
            self.interesting_label_frame,
            text="The sections most interesting to me are:",
            font="Helvetica 12 bold",
            justify="left",
        )
        self.label.pack(side="left")

        # ------------------------------------------------------ #
        # Interest checkboxes section

        # Checkbox buttons frame.
        self.checkbox_buttons_frame = Frame()
        self.checkbox_buttons_frame.pack(fill=BOTH)

        self.cb_list = [
            "Basics",
            "Iterations",
            "Functions",
            "RE",
            "Files & Db",
            "Networking",
            "OOP",
            "Graphics",
            "Web",
        ]

        self.cb_IntVar = []

        for row, value in enumerate(self.cb_list):
            self.cb_IntVar.append(IntVar())
            self.cb = Checkbutton(
                self.checkbox_buttons_frame,
                text=value,
                variable=self.cb_IntVar[-1]
            )
            self.cb.pack(side="left")

        # ------------------------------------------------------ #
        Label(master, font=3, height=0).pack(fill=X)

        # ------------------------------------------------------ #
        # Would you recommend this course to others label

        # Left align label frame.
        self.recommend_label_frame = Frame()
        self.recommend_label_frame.pack(fill=BOTH)

        self.label = Label(
            self.recommend_label_frame,
            text="Would you recommend this course to others?",
            font="Helvetica 12 bold",
            justify="left",
        )
        self.label.pack(side="left")

        # ------------------------------------------------------ #
        # Recommendation Radio Buttons section

        # Left align label frame.
        self.rec_radio_label_frame = Frame()
        self.rec_radio_label_frame.pack(fill=BOTH)

        self.rec_rb_choices = [("Yes", 1), ("No", 2)]

        self.rec_rb_var = IntVar()

        for lang, val in self.rec_rb_choices:
            self.rb = Radiobutton(
                self.rec_radio_label_frame,
                text=lang,
                variable=self.rec_rb_var,
                value=val,
            )
            self.rb.pack(side="left")

        # ------------------------------------------------------ #
        Label(master, font=3, height=0).pack(fill=X)

        # ------------------------------------------------------ #
        # Additional comments text box

        # Left align label frame.
        self.comments_label_frame = Frame()
        self.comments_label_frame.pack(fill=BOTH)

        self.comments_entry_box = Entry(self.comments_label_frame)
        self.comments_entry_box.insert(200, "Have you additional comments")
        self.comments_entry_box.pack(side="left", fill=BOTH, expand=True)

        # ------------------------------------------------------ #
        # Submit Button
        self.submit_button = Button(
            master, text="Submit", command=self.print_all_choices
        )
        self.submit_button.pack()

        # ------------------------------------------------------ #
        # Quit the window
        self.close_button = Button(
            master,
            text="Quit",
            bg="green",
            fg="white",
            relief="raised",
            bd=2,
            activebackground="red",
            command=master.quit,
        )
        self.close_button.pack()

    # ------------------------------------------------------ #
    # Action functions

    def eb_print_choices(self):
        eb_text = self.entry_box.get()
        print(f"Student Name           : {eb_text}")

    def rb_print_choice(self):
        pos = self.rb_var.get() - 1
        print(f"Enjoying the course    : {self.rb_choices[pos][0]}")

    def cb_print_choice(self):
        choice_list = []
        for count, var in enumerate(self.cb_IntVar):
            if var.get():
                choice_list.append(self.cb_list[count])
        print(f"Sections of interest   : {choice_list}")

    def rec_rb_print_choice(self):
        pos = self.rec_rb_var.get() - 1
        print(f"Recommend this course  : {self.rec_rb_choices[pos][0]}")

    def comments_print_choice(self):
        comments_text = self.comments_entry_box.get()
        print(f"Additional comments    : {comments_text}")

    def print_all_choices(self):
        print("")
        self.eb_print_choices()
        self.rb_print_choice()
        self.cb_print_choice()
        self.rec_rb_print_choice()
        self.comments_print_choice()


# ========================================== #
# //          Global environment          // #
# ========================================== #


# Call main function
if __name__ == "__main__":
    tk = Tk()
    TkinterApp(tk)
    tk.mainloop()

# END
