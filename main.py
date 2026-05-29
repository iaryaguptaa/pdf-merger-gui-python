import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter


class PDFMergerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Merger")
        self.geometry("600x360")
        self.files = []

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=80, height=15)
        self.listbox.pack(padx=10, pady=(10, 0))

        btn_frame = tk.Frame(self)
        btn_frame.pack(padx=10, pady=10, fill=tk.X)

        tk.Button(btn_frame, text="Add PDFs", command=self.add_files).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Remove", command=self.remove_selected).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="Move Up", command=self.move_up).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Move Down", command=self.move_down).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="Clear", command=self.clear_list).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Merge", command=self.merge_files).pack(side=tk.RIGHT)

    def add_files(self):
        paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])
        for p in paths:
            if p not in self.files:
                self.files.append(p)
                self.listbox.insert(tk.END, p) # tk.end to clear previous selection

    def remove_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        self.listbox.delete(idx)
        del self.files[idx]

    def move_up(self):
        sel = self.listbox.curselection()
        if not sel or sel[0] == 0:
            return
        idx = sel[0]
        self.files[idx - 1], self.files[idx] = self.files[idx], self.files[idx - 1]
        self._refresh_listbox()
        self.listbox.select_set(idx - 1)

    def move_down(self):
        sel = self.listbox.curselection()
        if not sel or sel[0] == len(self.files) - 1:
            return
        idx = sel[0]
        self.files[idx + 1], self.files[idx] = self.files[idx], self.files[idx + 1]
        self._refresh_listbox()
        self.listbox.select_set(idx + 1)

    def clear_list(self):
        self.files.clear()
        self.listbox.delete(0, tk.END)

    def _refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for p in self.files:
            self.listbox.insert(tk.END, p)

    def merge_files(self):
        if not self.files:
            messagebox.showwarning("No files", "Please add PDF files to merge.")
            return
        out_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="Save merged PDF as")
        if not out_path:
            return

        try:
            writer = PdfWriter()
            for p in self.files:
                writer.append(p)
            writer.write(out_path)
            messagebox.showinfo("Success", f"Merged {len(self.files)} files to:\n{out_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")


if __name__ == "__main__":
    app = PDFMergerGUI()
    app.mainloop()