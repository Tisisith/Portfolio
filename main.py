import tkinter as tk

class ReverseClipboardManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Reverse Clipboard Manager")

        self.clipboard = {}
        self.create_widgets()

    def create_widgets(self):
        self.text_entry = tk.Entry(self.master, width=40)
        self.text_entry.grid(row=0, column=0, padx=10, pady=10)

        copy_button = tk.Button(self.master, text="Copy", command=self.copy_text)
        copy_button.grid(row=0, column=1, padx=10, pady=10)

        display_button = tk.Button(self.master, text="Display Clipboard", command=self.display_clipboard)
        display_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.clipboard_display = tk.Text(self.master, height=10, width=40)
        self.clipboard_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def copy_text(self):
        text = self.text_entry.get()
        if text:
            index = len(self.clipboard) + 1
            self.clipboard[index] = text
            self.text_entry.delete(0, tk.END)

    def display_clipboard(self):
        self.clipboard_display.delete(1.0, tk.END)
        if not self.clipboard:
            self.clipboard_display.insert(tk.END, "Clipboard is empty.")
        else:
            self.clipboard_display.insert(tk.END, "Reverse-Numbered Clipboard:\n")
            for index in range(len(self.clipboard), 0, -1):
                self.clipboard_display.insert(tk.END, f"{index}. {self.clipboard[index]}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReverseClipboardManagerApp(root)
    root.mainloop()
