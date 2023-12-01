import tkinter as tk
from tkinter import ttk
import pyperclip



english_to_morse = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',

    # Special Characters
    '.': '.-.-.-',  # Period
    ',': '--..--',  # Comma
    '?': '..--..',  # Question mark
    "'": '.----.',  # Single quotation mark (apostrophe)
    '!': '-.-.--',  # Exclamation mark (Note: This is an unofficial code, but is commonly used.)
    '/': '-..-.',   # Forward slash
    '(': '-.--.',   # Open parenthesis (or bracket)
    ')': '-.--.-',  # Close parenthesis (or bracket)
    '&': '.-...',   # Ampersand
    ':': '---...',  # Colon
    ';': '-.-.-.',  # Semicolon
    '=': '-...-',   # Equals sign
    '+': '.-.-.',   # Plus sign
    '-': '-....-',  # Hyphen or minus sign
    '_': '..--.-',  # Underscore
    '"': '.-..-.',  # Double quotation mark
    '$': '...-..-', # Dollar sign (Note: This is also an unofficial code but is sometimes used.)
    '@': '.--.-.',  # At symbol (Note: This is an unofficial code but is often used.)
    
}

# Translate Function
def translate(text):
    text = text.upper()
    morse_string = ""
    for char in text:
        try:
            if char == " ":
                morse_string += "  "
            else:
                morse_string += english_to_morse[char] + " "
        except KeyError:
            print("Sorry, I can't translate this character: " + char)
            morse_string += char + " "
    return morse_string



def on_translate_button_click():
    user_input = entry.get()
    morse_result = translate(user_input)

    #new window for the result
    result_window = tk.Toplevel(window)
    result_window.title("Morse Code Result")

    #colors for the result window
    result_window.configure(bg="#3498db")

    # Create and place widgets in the result window
    result_label = tk.Label(result_window, text=morse_result, font=('Arial', 12), bg="#ecf0f1", padx=20, pady=20)
    result_label.pack(pady=20)

    # "Copy to Clipboard" button
    copy_button = ttk.Button(result_window, text="Copy to Clipboard", command=lambda: copy_to_clipboard(morse_result), style="TButton")
    copy_button.pack(pady=10)



def copy_to_clipboard(text):
    pyperclip.copy(text)

# Create the main window
window = tk.Tk()
window.title("Morse Code Translator App")

# Configure colors
window.configure(bg="#3498db")  # Set the background color

# Create and place widgets in the window
frame_input = tk.Frame(window, bg="#3498db", padx=20, pady=20)
frame_input.pack(pady=20)

label_input = tk.Label(frame_input, text="Enter a random English text:", font=('Arial', 12), bg="#3498db", fg="white")
label_input.grid(row=0, column=0, pady=20)

entry = tk.Entry(frame_input, width=30, font=('Arial', 8))
entry.grid(row=1, column=0, pady=10)

frame_output = tk.Frame(window, bg="#ecf0f1", padx=20, pady=20)
frame_output.pack(pady=20)

style = ttk.Style()
style.configure("TButton", relief=tk.GROOVE, font=('Arial', 12, 'bold'))
style.map("TButton", background=[('active', '#ecf0f1')])  # Change background color on click

translate_button = ttk.Button(frame_output, text="Translate", command=on_translate_button_click, style="TButton")
translate_button.grid(row=0, column=0, pady=10)


# Start the GUI.
window.mainloop()