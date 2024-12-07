# Usiel Figueroa
# Module 10.2 Assignment: GUI To-Do
# CSD325-A311 Advanced Python
# December 02, 2024

# References:
# Love, D. (2018, January 18). Python Tkinker By Example. Github. Retrieved December 2, 2024, from https://github.com/Dvlv/Tkinter-By-Example/blob/master/Tkinter-By-Example.pdf

import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):  # Corrected the method name
        super().__init__()
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview
        )
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("To-Do App v2")
        self.geometry("300x400")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        todo_label = tk.Label(
            self.tasks_frame, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10
        )
        todo_label.bind("<Button-1>", self.remove_task)
        self.tasks.append(todo_label)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [
            {"bg": "lightgrey", "fg": "black"},
            {"bg": "grey", "fg": "white"},
        ]

    def add_task(self, event=None):
        task_text = self.task_create.get("1.0", tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
            self.task_create.delete("1.0", tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"], fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()

