def arithmetic_arranger(list_of_strings, display_answers=False):
    # Limit the number of problems to five
    if len(list_of_strings) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in list_of_strings:
        parts = problem.split(" ")
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first_operand, operator, second_operand = parts

        # Validate operands
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Calculate the answer
        if operator == '+':
            result = int(first_operand) + int(second_operand)
        else:
            result = int(first_operand) - int(second_operand)

        # Format each part
        width = max(len(first_operand), len(second_operand)) + 2
        first_line.append(first_operand.rjust(width))
        second_line.append(operator + second_operand.rjust(width - 1))
        dashes.append("-" * width)
        answers.append(str(result).rjust(width))

    # Assemble the arranged problems
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes)
    )
    if display_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems


# Example Usage
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], display_answers=True))
