from tkinter import Tk as tkTk, Label as tkLabel, Button as tkButton, Frame as tkFrame

class Element:
    def __init__(self, tag, **props):
        """Directly create a TkReact element from a Tkinter class"""
        self.tag = tag
        self.props = props
        self.children = []

    def __call__(self, *children):
        """Allow adding children to the element."""
        self.children = children
        return self

    def render(self, parent):
        """Render the widget and its children."""
        widget = self.tag(parent, **self.props)

        if isinstance(widget, tkFrame):
            for child in self.children:
                child.render(widget)

            if self.props.get("direction") == "horizontal":
                widget.pack(anchor="w", side="left", padx=5, pady=5)
            else:
                widget.pack(anchor="w", fill="x", padx=5, pady=5)
        else:
            widget.pack(anchor="w", fill="x", padx=5, pady=5)

        return widget

def create_root(app, title):
    """Creates the root Tkinter window and runs the app."""
    root = tkTk()
    root.title(title)
    root.geometry("850x480")

    components = app(root)

    for component in components:
        component.render(root)

    root.mainloop()

def Label(**props): 
    """Create a Label component."""
    return Element(tkLabel, **props)

def Button(**props): 
    """Create a Button component."""
    return Element(tkButton, **props)

def Container(**props):
    """Create a container (Frame) that can hold child elements in a layout."""
    return Element(tkFrame, **props)
