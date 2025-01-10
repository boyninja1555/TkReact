import tkinter as tk
from bs4 import BeautifulSoup
from tkreact.default_styles import FONT, BASE_FONT_SIZE, TEXT_ALIGN

STR_TK_BINDINGS = {
    "label": tk.Label,
    "button": tk.Button,
}

def create_root(entry: callable, title: str, **tk_args):
    """
    Renders the root element and starts the Tkinter event loop.
    
    Args:
        entry (callable): The root function of the application, which generates the UI elements.
            Args:
                root (tk.Tk): The root window of your application.
            
            Returns:
                tuple:
                    str: A string (or multi-line string) containing your app's HTML.
                    dict: A dict containing key-value pairs mapping strings to functions.
        
        title (str): Title of the Tkinter application window.
        tk_args (dict): Additional properties to pass to Tkinter root creation.
    """
    tk_root = tk.Tk(**tk_args)
    tk_root.title(title)
    tk_root.geometry("850x480")
    tk_root.state("zoomed")

    tk_elementtree = entry(tk_root)[0]
    tk_resources = entry(tk_root)[1]
    soup = BeautifulSoup(tk_elementtree, "html.parser")

    for tag, tk_class in STR_TK_BINDINGS.items():
        elements = soup.find_all(tag)

        for element in elements:
            widget_anchor = element.attrs.get("_anchor", TEXT_ALIGN)
            widget_fill = element.attrs.get("_fill", "x")
            widget_on_click = element.attrs.get("_on_click", "")
            widget_font = [FONT, BASE_FONT_SIZE, "normal"]
            
            if "_font" in element.attrs:
                widget_font[0] = element.attrs["_font"]
            
            if "_font_size" in element.attrs:
                widget_font[1] = int(element.attrs["_font_size"]) * BASE_FONT_SIZE
            
            if "_font_style" in element.attrs:
                widget_font[2] = element.attrs["_font_style"]

            tkinter_attrs = {key: value for key, value in element.attrs.items() if not key.startswith("_")}

            widget = tk_class(tk_root, text=element.text, font=tuple(widget_font), anchor=widget_anchor, **tkinter_attrs)
            widget.pack(side="top", fill=widget_fill)
            
            if widget_on_click:
                widget.bind("<Button-1>", lambda event: tk_resources[widget_on_click](event))

    tk_root.mainloop()

def use_state(initial_value):
    """
    Implements a simple state management hook similar to React's useState.

    Args:
        initial_value (Any): The initial value of the state.

    Returns:
        tuple: A tuple containing the getter function and the setter function for the state.
    """
    state = [initial_value]

    def get_state():
        """Getter function for the state."""
        return state[0]

    def set_state(new_value):
        """Setter function for the state."""
        state[0] = new_value

    return get_state, set_state
