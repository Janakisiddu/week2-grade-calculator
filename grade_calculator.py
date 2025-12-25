# Student Grade Calculator
# Week 2 Project – Control Flow & Data Structures
# Author: Siddardha Janaki

def calculate_grade(average):
    """Determine grade and comment based on average marks"""
    if average >= 90:
        return 'A', "Excellent! Keep up the great work!"
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', "Good. Room for improvement."
    elif average >= 60:
        return 'D', "Needs Improvement. Please study more."
    else:
        return 'F', "Failed. Please seek help from teacher."


def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within a specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=" * 50)
    print("        STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print()

    # Get number of students
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    student_names = []
    student_results = []

    # Collect data
    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} ===")

        name = input("Student name: ").strip()
        while name == "":
            print("Name cannot be empty!")
            name = input("Student name: ").strip()

        student_names.append(name)

        print("Enter marks (0–100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        student_results.append({
            "average": average,
            "grade": grade,
            "comment": comment
        })

    # Display results
    print("\n" + "=" * 50)
    print("            RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':>5} | Comment")
    print("-" * 60)

    for i in range(num_students):
        print(f"{student_names[i]:<20} | {student_results[i]['average']:>5.1f} | "
              f"{student_results[i]['grade']:>5} | {student_results[i]['comment']}")

    # Class statistics
    averages = [result["average"] for result in student_results]
    class_avg = sum(averages) / len(averages)
    max_avg = max(averages)
    min_avg = min(averages)

    print("\n" + "=" * 50)
    print("            CLASS STATISTICS")
    print("=" * 50)
    print(f"Total Students: {num_students}")
    print(f"Class Average: {class_avg:.1f}")
    print(f"Highest Average: {max_avg:.1f} ({student_names[averages.index(max_avg)]})")
    print(f"Lowest Average: {min_avg:.1f} ({student_names[averages.index(min_avg)]})")

    print("\n" + "=" * 50)
    print("Thank you for using the Grade Calculator!")
    print("=" * 50)


if __name__ == "__main__":
    main()
