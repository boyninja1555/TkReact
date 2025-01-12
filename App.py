from tkreact import create_root, Label, Button, Container
from tkinter import Tk

def App(root: Tk):
    root.state("zoomed")
    
    def handle_click():
        root.title("Button Clicked!")

    return (
        Container(padx=100, pady=100)(
            Label(text="This text is 1rem", font=("Arial", 1 * 16))(),
            Label(text="This is 2rem text", font=("Arial", 2 * 16, "bold"))(),
            Button(text="Click Me!", command=handle_click)(),
        ),
    )

create_root(App, "The Title")
