"""
main.py
A desktop Temperature Converter built with Python and Tkinter.
Supports Celsius, Fahrenheit, and Kelvin with input validation,
a swap-units button, and a running conversion history.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from converter import convert, UNIT_SYMBOLS, InvalidTemperatureError

UNITS = ["Celsius", "Fahrenheit", "Kelvin"]

BG_COLOR = "#eaf6ff"        # sky-blue background
CARD_COLOR = "#ffffff"
ACCENT_COLOR = "#2f80ed"
TEXT_COLOR = "#1a1a1a"
FONT_MAIN = ("Segoe UI", 11)
FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_RESULT = ("Segoe UI", 14, "bold")


class TemperatureConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("460x520")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)

        self._build_widgets()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------
    def _build_widgets(self):
        title = tk.Label(
            self, text="🌡 Temperature Converter",
            font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR
        )
        title.pack(pady=(20, 10))

        card = tk.Frame(self, bg=CARD_COLOR, bd=0, highlightthickness=0)
        card.pack(padx=20, pady=10, fill="both")

        # --- Input value ---
        tk.Label(card, text="Enter temperature:", font=FONT_MAIN,
                 bg=CARD_COLOR, fg=TEXT_COLOR).grid(
            row=0, column=0, columnspan=3, sticky="w", padx=15, pady=(15, 5)
        )
        self.value_entry = tk.Entry(card, font=FONT_MAIN, width=20)
        self.value_entry.grid(row=1, column=0, columnspan=3, padx=15, sticky="we")
        self.value_entry.bind("<Return>", lambda e: self.on_convert())

        # --- From / To unit selectors ---
        tk.Label(card, text="From:", font=FONT_MAIN, bg=CARD_COLOR,
                 fg=TEXT_COLOR).grid(row=2, column=0, padx=15, pady=(15, 5), sticky="w")
        tk.Label(card, text="To:", font=FONT_MAIN, bg=CARD_COLOR,
                 fg=TEXT_COLOR).grid(row=2, column=2, padx=15, pady=(15, 5), sticky="w")

        self.from_unit = tk.StringVar(value="Celsius")
        self.to_unit = tk.StringVar(value="Fahrenheit")

        from_menu = ttk.Combobox(card, textvariable=self.from_unit,
                                  values=UNITS, state="readonly", width=10)
        from_menu.grid(row=3, column=0, padx=15, sticky="w")

        swap_btn = tk.Button(card, text="⇄", font=("Segoe UI", 12, "bold"),
                              command=self.on_swap, bg=ACCENT_COLOR, fg="white",
                              relief="flat", width=3, cursor="hand2")
        swap_btn.grid(row=3, column=1, padx=5)

        to_menu = ttk.Combobox(card, textvariable=self.to_unit,
                                values=UNITS, state="readonly", width=10)
        to_menu.grid(row=3, column=2, padx=15, sticky="e")

        # --- Buttons ---
        btn_frame = tk.Frame(card, bg=CARD_COLOR)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=20)

        convert_btn = tk.Button(
            btn_frame, text="Convert", font=("Segoe UI", 11, "bold"),
            bg=ACCENT_COLOR, fg="white", relief="flat", padx=20, pady=6,
            cursor="hand2", command=self.on_convert
        )
        convert_btn.grid(row=0, column=0, padx=5)

        clear_btn = tk.Button(
            btn_frame, text="Clear", font=("Segoe UI", 11), bg="#e0e0e0",
            fg=TEXT_COLOR, relief="flat", padx=20, pady=6, cursor="hand2",
            command=self.on_clear
        )
        clear_btn.grid(row=0, column=1, padx=5)

        # --- Result ---
        self.result_var = tk.StringVar(value="Result will appear here")
        result_label = tk.Label(card, textvariable=self.result_var,
                                 font=FONT_RESULT, bg=CARD_COLOR, fg=ACCENT_COLOR)
        result_label.grid(row=5, column=0, columnspan=3, pady=(0, 15))

        # --- History ---
        tk.Label(self, text="History", font=("Segoe UI", 12, "bold"),
                 bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w", padx=25, pady=(10, 0))

        history_frame = tk.Frame(self, bg=BG_COLOR)
        history_frame.pack(padx=20, pady=(5, 15), fill="both", expand=True)

        self.history_list = tk.Listbox(history_frame, font=("Segoe UI", 10),
                                        height=8, bd=0, highlightthickness=1)
        self.history_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(history_frame, command=self.history_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.history_list.config(yscrollcommand=scrollbar.set)

        for col in range(3):
            card.grid_columnconfigure(col, weight=1)

    # ------------------------------------------------------------------
    # Event handlers
    # ------------------------------------------------------------------
    def on_convert(self):
        raw = self.value_entry.get().strip()
        from_u = self.from_unit.get()
        to_u = self.to_unit.get()

        if not raw:
            messagebox.showerror("Input Error", "Please enter a temperature value.")
            return

        try:
            value = float(raw)
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please enter a valid number (e.g. 36.6)."
            )
            return

        try:
            result = convert(value, from_u, to_u)
        except InvalidTemperatureError as e:
            messagebox.showerror("Invalid Temperature", str(e))
            return

        from_sym = UNIT_SYMBOLS[from_u]
        to_sym = UNIT_SYMBOLS[to_u]
        result_text = f"{value:g}{from_sym} = {result:.2f}{to_sym}"
        self.result_var.set(result_text)

        self.history_list.insert(0, result_text)

    def on_swap(self):
        f, t = self.from_unit.get(), self.to_unit.get()
        self.from_unit.set(t)
        self.to_unit.set(f)

    def on_clear(self):
        self.value_entry.delete(0, tk.END)
        self.result_var.set("Result will appear here")


if __name__ == "__main__":
    app = TemperatureConverterApp()
    app.mainloop()
