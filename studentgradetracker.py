import tkinter as tk
from tkinter import messagebox

class StudentGradeTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Grade Tracker")

        self.subjects = {}
        self.create_widgets()

    def create_widgets(self):
        self.subject_label = tk.Label(self.master, text="Subject:")
        self.subject_label.grid(row=0, column=0, padx=5, pady=5)

        self.subject_entry = tk.Entry(self.master)
        self.subject_entry.grid(row=0, column=1, padx=5, pady=5)

        self.grade_label = tk.Label(self.master, text="Grade:")
        self.grade_label.grid(row=1, column=0, padx=5, pady=5)

        self.grade_entry = tk.Entry(self.master)
        self.grade_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.master, text="Add Grade", command=self.add_grade)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.calculate_button = tk.Button(self.master, text="Calculate Average", command=self.calculate_average)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_grade(self):
        subject = self.subject_entry.get()
        grade = self.grade_entry.get()

        if subject and grade:
            try:
                grade = float(grade)
                if subject in self.subjects:
                    self.subjects[subject].append(grade)
                else:
                    self.subjects[subject] = [grade]
                messagebox.showinfo("Success", "Grade added successfully!")
                self.subject_entry.delete(0, tk.END)
                self.grade_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Grade must be a number!")
        else:
            messagebox.showerror("Error", "Please enter both subject and grade!")

    def calculate_average(self):
        if self.subjects:
            total_grades = 0
            total_subjects = 0
            for subject, grades in self.subjects.items():
                total_grades += sum(grades)
                total_subjects += len(grades)
            average_grade = total_grades / total_subjects
            self.result_label.config(text=f"Average Grade: {average_grade:.2f}")
        else:
            self.result_label.config(text="No grades added yet!")

def main():
    root = tk.Tk()
    app = StudentGradeTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
