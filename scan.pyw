import qrcode
from tkinter import *
from PIL import Image, ImageTk

class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600")  # Adjusted height for spacing
        self.root.title("Qrcode Generator")

        # Create entry box with default "read-only" placeholder text
        self.inp = Entry(self.root, font="consolas 16", fg='grey')
        self.inp.pack(pady=20)
        self.inp.insert(0, "Enter link or text here")  # Insert placeholder text

        # Bind events to clear and restore the placeholder text
        self.inp.bind("<FocusIn>", self.clear_placeholder)
        self.inp.bind("<FocusOut>", self.add_placeholder)

        # Bind Enter key to generate QR code
        self.root.bind('<Return>', self.generate_qr)

        # Create label to display the "Here's your QR code" text
        self.result_label = Label(self.root, text="", font="Arial 14 bold")
        self.result_label.pack(pady=10)  # Space before showing the QR code

        # Create label to display the QR code image
        self.qr_label = Label(self.root)
        self.qr_label.pack(pady=20)

        # Generate Button
        self.btn = Button(self.root, text="Generate", font="Arial 12", relief="ridge", command=self.generate_qr)
        self.btn.pack(side=BOTTOM, fill=BOTH)

    def clear_placeholder(self, event):
        if self.inp.get() == "Enter link or text here":
            self.inp.delete(0, END)  # Clear the placeholder text
            self.inp.config(fg='black')  # Change text color to black

    def add_placeholder(self, event):
        if not self.inp.get():  # If the entry is empty
            self.inp.insert(0, "Enter link or text here")  # Restore the placeholder text
            self.inp.config(fg='grey')  # Change text color to grey

    def generate_qr(self, event=None):
        # Get the input text from the entry box
        text = self.inp.get()

        if text and text != "Enter link or text here":
            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")

            # Save the QR code image as a file
            img.save("qrcode_image.png")

            # Open the image and convert it for displaying in tkinter
            img = Image.open("qrcode_image.png")
            img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Resize to fit the UI
            self.qr_img = ImageTk.PhotoImage(img)

            # Update the label with the generated QR code image
            self.qr_label.config(image=self.qr_img)

            # Add the "Here's your QR code" text
            self.result_label.config(text="Here's your QR code:", fg='blue')

win = Tk()
obj = Main(win)
win.mainloop()
