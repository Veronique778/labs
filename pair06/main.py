
import tkinter as tk
from tkinter import messagebox
import student_utils

students = ["Anna", "Ivan", "Olha"]

def make_report():
    value = entry.get().strip()

    if not value.isdecimal() or not 1 <= int(value) <= 20:
        messagebox.showerror("Error", "Enter 1-20")
        return

    report = ""
    for name in students:
        grades = student_utils.generate_grades(int(value))
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        report += f"{name}: {grades} -> {avg:.1f} -> {level}\n"

    print(report)
    result.delete("1.0", tk.END)
    result.insert(tk.END, report)

app = tk.Tk()
app.title("Student Statistics")
app.geometry("500x400")

tk.Label(app, text="Number of grades (1-20):").pack()
entry = tk.Entry(app)
entry.insert(0, "5")
entry.pack()
tk.Button(app, text="Generate report", command=make_report).pack()
result = tk.Text(app, height=12, width=55)
result.pack()

app.mainloop()
