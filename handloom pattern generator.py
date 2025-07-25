import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk
class PatternGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Handloom Pattern Generator")
        self.warp_color = "#000000"
        self.weft_color = "#ffffff"
        self.pattern_type = tk.StringVar(value="Plain")
        self.canvas_size = 400
        self.create_widgets()
    def create_widgets(self):
        tk.Button(self.root, text="Choose Warp Color", command=self.choose_warp_color).pack()
        tk.Button(self.root, text="Choose Weft Color", command=self.choose_weft_color).pack()
        tk.OptionMenu(self.root, self.pattern_type, "Plain", "Twill", "Satin").pack()
        tk.Button(self.root, text="Generate Pattern", command=self.generate_pattern).pack()
        self.canvas = tk.Label(self.root)
        self.canvas.pack()
        tk.Button(self.root, text="Save Pattern", command=self.save_image).pack()
    def choose_warp_color(self):
        color = colorchooser.askcolor(title="Warp Color")[1]
        if color:
            self.warp_color = color
    def choose_weft_color(self):
        color = colorchooser.askcolor(title="Weft Color")[1]
        if color:
            self.weft_color = color
    def generate_pattern(self):
        size = 20  # square size
        rows = cols = self.canvas_size // size
        image = Image.new("RGB", (self.canvas_size, self.canvas_size), "white")
        draw = ImageDraw.Draw(image)
        for i in range(rows):
            for j in range(cols):
                if self.pattern_type.get() == "Plain":
                    color = self.warp_color if (i + j) % 2 == 0 else self.weft_color
                elif self.pattern_type.get() == "Twill":
                    color = self.warp_color if (i + j) % 3 != 0 else self.weft_color
                else:  # Satin
                    color = self.warp_color if (i * j) % 5 != 0 else self.weft_color
                draw.rectangle([j*size, i*size, (j+1)*size, (i+1)*size], fill=color)
        self.pattern_image = image
        tk_image = ImageTk.PhotoImage(image)
        self.canvas.configure(image=tk_image)
        self.canvas.image = tk_image
    def save_image(self):
        if hasattr(self, 'pattern_image'):
            filepath = filedialog.asksaveasfilename(defaultextension=".png")
            if filepath:
                self.pattern_image.save(filepath)
root = tk.Tk()
app = PatternGenerator(root)
root.mainloop() 