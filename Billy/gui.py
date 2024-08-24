import tkinter as tk
from regex import get_response

# Sends the user input
def send_message(event=None): 
    message = input_field.get()
    if message:
        input_field.delete(0, tk.END)
        display_message("You: ", message, "#A2C8E6")  # Light blue background for user messages
        
        # Get the chatbot's response
        response = get_response(message)
        display_message("Billy: ", response, "#72a1d4") #Default background for chatbot messages
        
# Displays the text as a message
def display_message(sender, message, bg_color):
    messages.config(state=tk.NORMAL)
    tag = "user" if bg_color == "#A2C8E6" else "chatbot"
    messages.insert(tk.END, f"{sender}{message}\n\n", (tag, bg_color))
    messages.config(state=tk.DISABLED)
    messages.see(tk.END)       

root = tk.Tk()
root.title("Billy")
root.geometry("500x400")
root.iconbitmap('billy.ico')

# Frame for the chat
output_frame = tk.Frame(root, bg="#72a1d4")  # Default background color for the chat area
output_frame.pack(fill=tk.BOTH, expand=True)

messages = tk.Text(output_frame, wrap=tk.WORD, bg="#72a1d4", fg="black")
messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
messages.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(output_frame, command=messages.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
messages.config(yscrollcommand=scrollbar.set)

# Define tag configurations for different backgrounds
messages.tag_configure("user", background="#A2C8E6", foreground="black")  # Light blue background for user messages
messages.tag_configure("chatbot", background="#72a1d4", foreground="black")  # Default background for chatbot messages

# Frame for user input
input_frame = tk.Frame(root, bg="#A2C8E6")
input_frame.pack(fill=tk.X, side=tk.BOTTOM)  # Ensure it is at the bottom

input_field = tk.Entry(input_frame, bg="#FFFFFF", fg="black")  
input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Allows user to send message without having to click on the "Send" button
input_field.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Allows user to write without having to click in the input field
input_field.focus()   

root.mainloop()
