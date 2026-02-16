#!/usr/bin/env python3

import csv

class Student:
    def __init__(self, student_id, name, math, physics, chemistry, biology):
        self.student_id = student_id
        self.name = name
        self.math = int(math)
        self.physics = int(physics)
        self.chemistry = int(chemistry)
        self.biology = int(biology)

    def average(self):
        return (self.math + self.physics + self.chemistry + self.biology) / 4


def analyze_grades(input_file, output_file):

    students = []

    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["StudentID"],
                    row["Name"],
                    row["Math"],
                    row["Physics"],
                    row["Chemistry"],
                    row["Biology"]
                )
                students.append(student)

    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    if not students:
        print("No student data found.")
        return

    total_students = len(students)

    total_math = sum(s.math for s in students)
    total_physics = sum(s.physics for s in students)
    total_chemistry = sum(s.chemistry for s in students)
    total_biology = sum(s.biology for s in students)

    class_avg_math = total_math / total_students
    class_avg_physics = total_physics / total_students
    class_avg_chemistry = total_chemistry / total_students
    class_avg_biology = total_biology / total_students

    overall_class_avg = (
        class_avg_math +
        class_avg_physics +
        class_avg_chemistry +
        class_avg_biology
    ) / 4

    top_3 = sorted(students, key=lambda s: s.average(), reverse=True)[:3]

    above_90 = [
        s for s in students
        if s.math > 90 or s.physics > 90 or
           s.chemistry > 90 or s.biology > 90
    ]

    highest_math = max(students, key=lambda s: s.math)
    lowest_math = min(students, key=lambda s: s.math)

    highest_physics = max(students, key=lambda s: s.physics)
    lowest_physics = min(students, key=lambda s: s.physics)

    highest_chemistry = max(students, key=lambda s: s.chemistry)
    lowest_chemistry = min(students, key=lambda s: s.chemistry)

    highest_biology = max(students, key=lambda s: s.biology)
    lowest_biology = min(students, key=lambda s: s.biology)

    with open(output_file, 'w') as report:

        report.write("STUDENT PERFORMANCE REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Total Students: {total_students}\n\n")

        report.write("Class Average per Subject:\n")
        report.write(f"Math: {class_avg_math:.2f}\n")
        report.write(f"Physics: {class_avg_physics:.2f}\n")
        report.write(f"Chemistry: {class_avg_chemistry:.2f}\n")
        report.write(f"Biology: {class_avg_biology:.2f}\n\n")

        report.write(f"Overall Class Average: {overall_class_avg:.2f}\n\n")

        report.write("Top 3 Students:\n")
        for s in top_3:
            report.write(f"{s.name} ({s.student_id}) - Avg: {s.average():.2f}\n")
        report.write("\n")

        report.write("Students Scoring Above 90 in Any Subject:\n")
        for s in above_90:
            report.write(f"{s.name} ({s.student_id})\n")
        report.write("\n")

        report.write("Subject-wise Highest and Lowest Scores:\n")

        report.write(f"Math -> Highest: {highest_math.name} ({highest_math.math}), "
                     f"Lowest: {lowest_math.name} ({lowest_math.math})\n")

        report.write(f"Physics -> Highest: {highest_physics.name} ({highest_physics.physics}), "
                     f"Lowest: {lowest_physics.name} ({lowest_physics.physics})\n")

        report.write(f"Chemistry -> Highest: {highest_chemistry.name} ({highest_chemistry.chemistry}), "
                     f"Lowest: {lowest_chemistry.name} ({lowest_chemistry.chemistry})\n")

        report.write(f"Biology -> Highest: {highest_biology.name} ({highest_biology.biology}), "
                     f"Lowest: {lowest_biology.name} ({lowest_biology.biology})\n")

    print("Report generated successfully:", output_file)


if __name__ == "__main__":
    analyze_grades("grades.csv", "report.txt")
