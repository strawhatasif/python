# This program calculates and displays an average test score and letter grade for each student.
# Test scores are entered by the teacher.

# constant for number of test scores entered. can be adjusted in the future, if needed.
NUMBER_OF_TEST_SCORES = 3


def main():
    # this variable contains state for whether the teacher wants to continue entering test scores for students or not.
    another_student = 'y'

    # while there is another student to enter, continue accepting three test scores from teacher
    while 'y'.__eq__(another_student):

        # stores the running total of the test scores entered
        test_scores_total = 0

        # depending on the number of test scores, collect test scores from teacher
        for test_entry in range(NUMBER_OF_TEST_SCORES):
            test_score = process_test_score_entry(test_entry)
            test_scores_total += test_score

        average_test_score = calc_average(test_scores_total)
        print('The test score average is: ' + format(average_test_score, 'd'))
        print('The letter grade is: ' + determine_grade(average_test_score))

        another_student = input('Do you want to enter test scores for another student? (Enter y for yes): ')


# input - number of test entry (int, whole number)
# test scores assumption: whole numbers only!
# if any test scores are less than 0 or greater than 100, display an error message.
# ask the teacher to reenter a valid test score.
def process_test_score_entry(number_of_test_entry):
    # variables for display
    # increment number_of_test_entry by 1 since entries start at 1 and not 0.s
    test_score_prompt = 'Enter test score ' + str(number_of_test_entry + 1) + ': '
    reenter_test_score_prompt = 'Reenter test score ' + str(number_of_test_entry + 1) + ': '
    error_message = 'Invalid entry. Test score must be between 0 and 100.'
    test_score = int(input(test_score_prompt))
    while test_score < 0 or test_score > 100:
        print(error_message)
        test_score = int(input(reenter_test_score_prompt))

    return test_score


# returns - an int which takes the total of test scores entered and divides them by the number of test scores
def calc_average(test_scores_total):
    return int(test_scores_total / NUMBER_OF_TEST_SCORES)


# input - average test score (int, whole number)
# returns - a string which is a letter grade
def determine_grade(average_test_score):
    # based on the average test score range, the appropriate letter grade will be returned
    # default is a "F"
    if 90 <= average_test_score <= 100:
        grade = "A"
    elif 80 <= average_test_score <= 89:
        grade = "B"
    elif 70 <= average_test_score <= 79:
        grade = "C"
    elif 60 <= average_test_score <= 69:
        grade = "D"
    else:
        grade = "F"
    return grade


main()
