import tkinter as tk

class CrosshairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crosshair App")
        self.root.geometry('100x100+100+100')  # Μικρό παράθυρο
        self.root.configure(bg='magenta')  # Ρυθμίσεις διαφάνειας
        self.root.overrideredirect(True)  # Αφαιρούμε τα παράθυρα του συστήματος
        self.root.attributes("-topmost", True)  # Το παράθυρο είναι πάντα πάνω

        self.canvas = tk.Canvas(self.root, width=100, height=100, bg='magenta', bd=0, highlightthickness=0)
        self.canvas.pack()

        # Δημιουργία του crosshair
        self.canvas.create_line(50, 0, 50, 100, fill="black", width=2)  # Κάθετη γραμμή
        self.canvas.create_line(0, 50, 100, 50, fill="black", width=2)  # Οριζόντια γραμμή

if __name__ == "__main__":
    root = tk.Tk()
    app = CrosshairApp(root)
    root.mainloop()
