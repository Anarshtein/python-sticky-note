import tkinter as tk  # Import the tkinter module and alias it as tk
from tkinter import Label, simpledialog, messagebox  # Import specific widgets and dialog boxes from tkinter
import os  # Import the os module for file operations
from plyer import notification # Importing the notification class from the plyer module
class StickyNotesApp:
    def __init__(self, root):
        self.root = root  # Store the root window reference
        self.root.title("Sticky Notes App")  # Set the window title
        self.root.geometry("800x400")  # Set the default window size
        self.root.maxsize(1000, 400)  # Set the maximum window size

        # Create a label at the top of the window
        windLabel = Label(root, text='This is sample note app', bg="blue", font=("Arial", 14, "bold"), borderwidth=2, relief="raised", fg="white")
        windLabel.pack(pady=10)  # Add some padding around the label

        self.notes_file = "notes.txt"  # Define the file where notes will be saved
        self.notes = []  # Initialize an empty list to store notes

        # Create the main frame that will hold other widgets
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Add a button to add new notes
        self.add_button = tk.Button(self.main_frame, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=10)  # Add some padding around the button

        # Create a canvas widget
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a vertical scrollbar linked to the canvas
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas
        self.notes_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.notes_frame, anchor="nw")

        # Configure the canvas scroll region
        self.notes_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Load existing notes from the file and display them
        self.load_notes()
        self.show_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):  # Check if the notes file exists
            with open(self.notes_file, "r") as file:  # Open the file in read mode
                self.notes = [line.strip() for line in file.readlines()]  # Read all lines, stripping whitespace

    def save_notes(self):
        with open(self.notes_file, "w") as file:  # Open the file in write mode
            for note in self.notes:  # Iterate through the notes list
                file.write(note + "\n")  # Write each note to the file, followed by a newline

    def add_note(self):
        note_text = simpledialog.askstring("Input", "Enter your note:")  # Prompt the user to enter a note
        if note_text:  # If the user enters a note
            self.notes.append(note_text)  # Add the note to the list
            self.save_notes()  # Save the updated notes list to the file
            
            # Creating a notification with success mesaage and added note as its content 
            notification.notify(
                title = "Note inserted successfully!",
                message= note_text,
                timeout=2
            )
            self.show_notes()  # Refresh the displayed notes

    def delete_note(self, note):
        if messagebox.askyesno("Delete", "Are you sure you want to delete this note?"):  # Confirm deletion
            self.notes.remove(note)  # Remove the note from the list
            self.save_notes()  # Save the updated notes list to the file
            
            # Creating a notification with success mesaage and added note as its content 
            notification.notify(
                title = "Note deleted successfully!",
                message= note,
                timeout=2
            )
            self.show_notes()  # Refresh the displayed notes

    def show_notes(self):
        for widget in self.notes_frame.winfo_children():  # Remove all existing widgets from the notes frame
            widget.destroy()

        for note in self.notes:  # Iterate through the notes list
            note_frame = tk.Frame(self.notes_frame, pady=5)  # Create a frame for each note
            note_frame.pack(fill=tk.X)  # Make the frame fill horizontally

            note_label = tk.Label(note_frame, text=note, wraplength=300, justify=tk.LEFT, borderwidth=2, relief="raised")  # Create a label for the note
            note_label.pack(side=tk.LEFT, padx=10)  # Add some padding around the label

            delete_button = tk.Button(note_frame, text="Delete", command=lambda n=note: self.delete_note(n))  # Create a delete button for the note
            delete_button.pack(side=tk.RIGHT, padx=10)  # Add some padding around the button

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = StickyNotesApp(root)  # Create an instance of the StickyNotesApp class
    root.mainloop()  # Start the Tkinter event loop to keep the window open and responsive
