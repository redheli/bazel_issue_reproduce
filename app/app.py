
import ctypes

x11 = ctypes.cdll.LoadLibrary("libX11.so")

x11.XInitThreads()

# import customtkinter as ctk
import tkinter as tk

app = tk.Tk()
button = tk.Button(app, text="Press me")
button.pack()
app.mainloop()

# def main():

#     # customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
#     # customtkinter.set_default_color_theme(
#         # "blue"
#     # )  # Themes: blue (default), dark-blue, green

#     app = tk.Tk()  # create CTk window like you do with the Tk window
#     app.geometry("800x600")  # Adjusted to match the tkinter example

#     canvas_height = 400  # Fixed height for the canvas

#     # # Configure the grid
#     # app.grid_rowconfigure(0, weight=0)  # This row will not expand
#     # app.grid_rowconfigure(1, weight=1)  # Other rows can expand
#     # app.grid_columnconfigure(0, weight=1)  # Allow the column to expand


#     def button_function():
#         print("button pressed")


#     # # Integrating the tkinter canvas and labels
#     canvas = tk.Canvas(app, width=600, height=600)
#     # canvas.grid(row=0, column=1, sticky="nsew")

#     # label_1 = tk.Label(app, text="from here", anchor=tk.W)
#     # label_1.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
#     # label_1_window = canvas.create_window(280, 0, anchor=tk.NW, window=label_1)
#     # label_2 = tk.Label(app, text="to there", anchor=tk.W)
#     # label_2.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
#     # label_2_window = canvas.create_window(280, 310, anchor=tk.NW, window=label_2)
#     # # canvas.pack()
#     # canvas.grid(row=0, column=1, sticky="nsew")
#     # canvas.create_line(300, 40, 300, 300, arrow=tk.LAST, width=5, fill="blue")


#     def on_canvas_click(event):
#         # Line coordinates
#         x1, y1, x2, y2 = 300, 40, 300, 300
#         # Tolerance radius
#         tolerance = 5

#         # Check if the click is within tolerance of the line
#         if (
#             x1 - tolerance <= event.x <= x2 + tolerance
#             and y1 - tolerance <= event.y <= y2 + tolerance
#         ):
#             line_click_callback()


#     def draw_line_with_arrow(canvas_width):
#         padding = 20
#         line_sx = canvas_width / 2
#         line_sy = padding
#         line_ex = canvas_width / 2
#         line_ey = canvas_height - padding
#         # Integrating the tkinter canvas and labels
#         label_1 = tk.Label(app, text="from here", anchor=tk.W)
#         label_1.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
#         label_1_window = canvas.create_window(
#             line_sx - 20, line_sy, anchor=tk.NW, window=label_1
#         )
#         label_2 = tk.Label(app, text="to there", anchor=tk.W)
#         label_2.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
#         label_2_window = canvas.create_window(
#             line_ex - 20, line_ey, anchor=tk.NW, window=label_2
#         )
#         canvas.create_line(
#             line_sx, line_sy, line_ex, line_ey, arrow=tk.LAST, width=5, fill="blue"
#         )


#     def line_click_callback():
#         print("Line was clicked")


#     TOPLEVEL_STR = "."


#     def on_window_resize(event):
#         print(f"Window name: {event.widget} widthxheight: {event.width}x{event.height}")
#         if str(event.widget) != TOPLEVEL_STR:
#             return
#         # Calculate new width as 80% of the window's width
#         new_width = int(event.width * 0.8)
#         # Update the canvas width
#         canvas.config(width=new_width)
#         # Redraw the line with an arrow to fit the new canvas size
#         canvas.delete("all")  # Clear the canvas
#         draw_line_with_arrow(new_width)  # Redraw the line

#     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#     # Assuming 'canvas' is your Canvas widget
#     canvas.bind("<Button-1>", on_canvas_click)


#     # Use CTkButton instead of tkinter Button
#     button = tk.Button(app, text="Press me", command=button_function)
#     # button.place(
#     #     x=300, y=50, anchor=tk.CENTER
#     # # )  # Adjusted position to make room for canvas
#     button.grid(row=0, column=0, sticky="new", padx=10, pady=10)

#     # Bind the resize event to the on_window_resize function
#     # app.bind("<Configure>", on_window_resize)


#     app.mainloop()


    
# if __name__ == "__main__":
#     main()