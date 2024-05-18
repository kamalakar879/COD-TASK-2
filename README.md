NAME:GADALE KAMALAKAR NARASIMHA
ID:CT08PP142
DOMAIN:PYTHON PROGRAMMING
DURATION:“10TH MAY 2024 to 10TH JUNE 2024”
MENTOR:SRAVANI GOUNI

##Description
This code implements a Student Grade Tracker application using the tkinter library in Python, providing a graphical user interface for tracking and calculating the average grade for different subjects. The application allows users to input grades for various subjects and calculate the average grade across all subjects entered. Here's a detailed breakdown of the code:

#### Class: StudentGradeTracker

1. **Initialization (`__init__` method)**:
    - The class is initialized with the main application window (`master`).
    - The window title is set to "Student Grade Tracker".
    - An empty dictionary `self.subjects` is created to store subjects and their respective grades.
    - The `create_widgets` method is called to set up the UI components.

2. **Creating Widgets (`create_widgets` method)**:
    - **Labels and Entries**:
        - `self.subject_label` and `self.grade_label` are labels for subject and grade input fields.
        - `self.subject_entry` and `self.grade_entry` are entry widgets for user input of subject names and grades.
    - **Buttons**:
        - `self.add_button` is a button to add the grade for a subject. It calls the `add_grade` method when clicked.
        - `self.calculate_button` is a button to calculate the average grade. It calls the `calculate_average` method when clicked.
    - **Result Label**:
        - `self.result_label` is used to display the calculated average grade.

3. **Adding Grades (`add_grade` method)**:
    - This method retrieves the subject and grade from the entry widgets.
    - It validates the input to ensure both fields are filled and the grade is a number.
    - If valid, it adds the grade to the `self.subjects` dictionary under the appropriate subject.
    - The method uses `messagebox.showinfo` to display a success message upon successful addition and clears the input fields.
    - If the input is invalid, appropriate error messages are displayed using `messagebox.showerror`.

4. **Calculating Average Grade (`calculate_average` method)**:
    - This method calculates the average grade across all subjects.
    - It iterates through the `self.subjects` dictionary to sum all grades and counts the total number of grades.
    - It computes the average grade and updates `self.result_label` to display the result.
    - If no grades have been added yet, it sets the result label to inform the user.

#### Main Function

- The `main` function initializes the main application window and creates an instance of `StudentGradeTracker`.
- The main loop `root.mainloop()` starts the application.

### Conclusion

This Student Grade Tracker application is a simple yet effective tool for managing and calculating grades for different subjects. It showcases how to build an interactive GUI application using `tkinter` in Python. The application provides user-friendly input validation and feedback mechanisms, ensuring a smooth user experience. It demonstrates the use of classes to encapsulate functionality and maintain state, making the code modular and easier to manage. This project serves as a practical example of how to create desktop applications with Python.
