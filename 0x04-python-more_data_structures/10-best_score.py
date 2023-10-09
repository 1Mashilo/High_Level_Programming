def get_student_with_highest_score(scores_dict):
    """
    Return the student with the highest score from a dictionary.

    Args:
        scores_dict (dict): A dictionary with student-score pairs.

    Returns:
        str: The student with the highest score, or None if the dictionary is empty.
    """
    if not scores_dict:
        return None

    max_student = max(scores_dict, key=scores_dict.get)
    return max_student

# Test case 
# Define a sample dictionary with student-score pairs
scores_dict = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eve': 88
}

# Call the function to find the student with the highest score
highest_scoring_student = get_student_with_highest_score(scores_dict)

# Print the result
if highest_scoring_student is not None:
    print(f"The student with the highest score is {highest_scoring_student}")
else:
    print("No scores found in the dictionary.")
