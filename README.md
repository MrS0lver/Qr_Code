# QR Code Generator using Python and Tkinter

This is a simple QR Code generator built using Python, the `qrcode` library, and `Tkinter` for the graphical user interface (GUI). The user can input any text or link, and the application will generate a QR code image that can be saved locally and displayed within the application.

## Features

- **Text Input**: The application provides a user-friendly input field with a placeholder for entering text or a URL.
- **QR Code Generation**: On pressing "Enter" or clicking the "Generate" button, a QR code is created for the input data.
- **Image Display**: The generated QR code is displayed inside the application.
- **Placeholder Text**: The input field includes a placeholder that clears when focused and reappears when unfocused if no input is given.
  
## Technologies Used

- **Python**: The core programming language used.
- **Tkinter**: The Python library for creating the GUI.
- **qrcode**: A library to generate QR codes.
- **Pillow (PIL)**: Used for handling and displaying the generated QR code image in the Tkinter window.

## Prerequisites

Make sure the following libraries are installed:

1. `qrcode`
2. `Pillow`

You can install them using pip:

```bash
pip install qrcode[pil] Pillow
