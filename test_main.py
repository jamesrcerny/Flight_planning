"""Flight planning app."""
import customtkinter as ctk

root = ctk.CTk()

#Page title and size
root.title("Testing Page")
root.geometry("500x500")

#Secondary page title
page_title = ctk.CTkLabel(root, text = "Test Page", font = ("Arial", 30))
page_title.pack(anchor = ctk.NW, padx = 10, pady = 10)

#Dynamic instance of object
dyna_content = ctk.CTkFrame(root)
dyna_content.pack(fill="both", expand=True, padx=20, pady=20)

#Standard button style
Entry_style = {
    "width": 200,
    "height": 45,
    "corner_radius": 10,
    "text_color": "black",
    "font": ("Arial", 18, "bold")
}
Button_style = {
    "width": 200,
    "height": 45,
    "corner_radius": 10,
    "fg_color": "#1f6aa5",
    "hover_color": "#144870",
    "text_color": "white",
    "font": ("Arial", 18, "bold")
}

#loop that handles multiple buttons
for i in range(5):
    ctk.CTkEntry(
        dyna_content,
        placeholder_text=f"Option {i+1}",
        **Entry_style
    ).pack(pady=5)
#command=lambda x=i: handle_click(x)

def 

def functions():
    if index =   
def handle_click(index):
    """Handle different callouts"""
    print(f"You clicked button {index+1}")

root.mainloop()
