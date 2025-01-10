from tkreact import create_root
from tkinter import Tk
from ping3 import ping
from random import randint

def click_button(event):
    print(f"Random integer: {randint(0, 10)}")

def App(root: Tk):
    flappygrant_ping_respond_time = ping("www.flappygrant.com")
    flappygrant_ping_message = "FlappyGrant is offline."

    if (flappygrant_ping_respond_time):
        flappygrant_ping_message = f"FlappyGrant is online and responded in {flappygrant_ping_respond_time} seconds."
    
    return (f"""
        <label _font="Comic Sans MS">{flappygrant_ping_message}</label>
        <label _font="Comic Sans MS" _font_size=2 _font_style=bold>Hello, world!</label>
        <button _on_click=click_button _font_style=italic _anchor=center _fill=none>Click me!</button>
    """, { "click_button": click_button, })

create_root(App, "Hello, World!")
