# Student Grade Analyzer Using Python

PASS_MARK = 40.0  # Minimum mark required per subject to pass


def get_valid_mark(subject_name):
    """Prompt the user for a valid mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"  Enter marks for {subject_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("  Invalid input. Please enter a value between 0 and 100.")
        except ValueError:
            print("  Invalid input. Please enter a numeric value.")


def calculate_grade(average, passed_all_subjects):
    """Determine letter grade based on average marks and pass status."""
    if not passed_all_subjects:
        return "F"
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"


def analyze_student(name, subjects):
    """Collect marks for a student and return their performance dictionary."""
    marks = {}
    print(f"\nEntering marks for {name}:")
    for subject in subjects:
        marks[subject] = get_valid_mark(subject)

    total_marks = sum(marks.values())
    average_marks = total_marks / len(subjects)
    passed_all = all(score >= PASS_MARK for score in marks.values())
    status = "PASS" if passed_all else "FAIL"
    grade = calculate_grade(average_marks, passed_all)

    return {
        "name": name,
        "marks": marks,
        "total": total_marks,
        "average": average_marks,
        "grade": grade,
        "status": status,
    }


def display_report(students, subjects):
    """Display individual student reports and overall class summary."""
    print("\n" + "=" * 60)
    print("                STUDENT PERFORMANCE REPORT")
    print("=" * 60)

    for student in students:
        print(f"\nStudent Name : {student['name']}")
        print("-" * 40)
        for subject in subjects:
            score = student["marks"][subject]
            sub_status = "Pass" if score >= PASS_MARK else "Fail"
            print(f"  {subject:<15}: {score:>6.2f} ({sub_status})")
        print("-" * 40)
        print(f"  Total Marks    : {student['total']:.2f} / {len(subjects) * 100}")
        print(f"  Average Marks  : {student['average']:.2f}%")
        print(f"  Grade          : {student['grade']}")
        print(f"  Result Status  : {student['status']}")

    # Class Summary
    class_averages = [s["average"] for s in students]
    passed_count = sum(1 for s in students if s["status"] == "PASS")
    top_student = max(students, key=lambda s: s["average"])

    print("\n" + "=" * 60)
    print("                    CLASS SUMMARY")
    print("=" * 60)
    print(f"  Total Students : {len(students)}")
    print(f"  Passed         : {passed_count}")
    print(f"  Failed         : {len(students) - passed_count}")
    print(f"  Class Average  : {sum(class_averages) / len(students):.2f}%")
    print(f"  Top Performer  : {top_student['name']} ({top_student['average']:.2f}%)")
    print("=" * 60)


def main():
    print("=== Student Grade Analyzer ===")

    # Input subjects
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = []
    for i in range(num_subjects):
        sub_name = input(f"Enter name of subject {i + 1}: ").strip()
        subjects.append(sub_name)

    # Input students
    num_students = int(input("\nEnter the number of students: "))
    students = []
    for i in range(num_students):
        name = input(f"\nEnter name of student {i + 1}: ").strip()
        student_data = analyze_student(name, subjects)
        students.append(student_data)

    # Display full report
    display_report(students, subjects)


if __name__ == "__main__":
    main()