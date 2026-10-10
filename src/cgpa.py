def calculate_cgpa(grade_points):
    if not grade_points:
        raise ValueError("Grade points cannot be empty")

    if any(point < 0 or point > 10 for point in grade_points):
        raise ValueError("Grade points must be between 0 and 10")

    return round(sum(grade_points) / len(grade_points), 2)


def performance_category(cgpa):
    if cgpa >= 8:
        return "Excellent"
    elif cgpa >= 6:
        return "Good"
    elif cgpa >= 5:
        return "Average"
    else:
        return "Needs Improvement"
