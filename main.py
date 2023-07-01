import tkinter as tk
from tkinter import messagebox
import subprocess
import signal

def show_message(message):
    messagebox.showinfo("Informasi", message)
def run_server():
    global server_process
    server_process = subprocess.Popen(["python", "webserver.py"])
    show_message("Aplikasi server berjalan!")
def stop_server():
    global server_process
    if server_process:
        server_process.terminate()
        show_message("Aplikasi server dihentikan!")
    else:
        show_message("Aplikasi server belum berjalan.")
window = tk.Tk()
window.title("PyWebServer")
window.geometry("300x200")
server_button = tk.Button(window, text="Jalankan Server", command=run_server)
server_button.pack()
stop_button = tk.Button(window, text="Stop Server", command=stop_server)
stop_button.pack()

window.mainloop()
