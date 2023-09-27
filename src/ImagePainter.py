# 5.  `ImagePainter.py`
#     *   Creates a `Tk` window and a `PhotoImage` object
#     *   The `PhotoImage` object stores the pixels of the image
#     *   This module contains code capable of creating a PNG image file

from tkinter import Tk, Canvas, PhotoImage, mainloop  	         	  
import time  	         	  
import sys


class ImagePainter:
    def __init__(self, fractal, imagename, palette):
        self.fractal = fractal
        self.imagename = imagename
        self.palette = palette

    def paint(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image."""
        size = self.fractal.getPixels()
        # Set up the GUI so that we can paint the fractal image on the screen
        before = time.time()
        window = Tk()
        img = PhotoImage(width=size, height=size)

        # Display the image on the screen
        canvas = Canvas(window, width=size, height=size, bg='#000000')
        canvas.pack()
        canvas.create_image((size/2, size/2), image=img, state="normal")

        for row in range(size, 0, -1):
            for col in range(size):
                x = self.fractal.getMinX() + col * self.fractal.getPixelSize()
                y = self.fractal.getMinY() + row * self.fractal.getPixelSize()
                c = self.fractal.count(complex(x, y))
                img.put(self.palette.getColor(c), (col, size - row))
            window.update()  # display a row of pixels

        # Save the image as a PNG
        after = time.time()
        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{self.imagename}.png")
        print(f"Wrote image {self.imagename}.png")

        # Call tkinter.mainloop so the GUI remains open
        print("Close the image window to exit the program")
        mainloop()
