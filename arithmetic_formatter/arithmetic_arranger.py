import re


def arithmetic_arranger(input_list, result=None):
        clean_list = []
        digits = []
        first_num = []
        sec_num = []
        operators = []
        len_first_num = []
        len_sec_num = []
        out_put_result = []

        # loop over the input list
        for i in input_list:
                digits.append(i.split()[0])
                digits.append(i.split()[2])
                operators.append(i.split()[1])  # get the operator sign

        # Check out if the length of the input list is less than or equal to 5
        if len(input_list) > 5:
                return "Error: Too many problems."

        # Check out if the operators are only '+' and '-'
        elif any(i for i in operators if (re.search("[^+-]", i))):
                return "Error: Operator must be '+' or '-'."

        # Each number (operand) should only contain digits
        elif any(i for i in digits if (re.search('[^0-9]', str(i)))):
                return "Error: Numbers must only contain digits."

        # Each number sould have a max of four digits in width
        elif any(i for i in digits if (len(str(i)) > 4)):
                return "Error: Numbers cannot be more than four digits."

        else:
                operators.clear()
                digits.clear()

                # input_list cleaning
                for i in input_list:
                        clean_list.append(i.split())

                # clean_list processing
                for i in clean_list:
                        first_num.append(int(i[0]))  # convert string to integer value
                        sec_num.append(int(i[2]))  # convert string to integer value
                        operators.append(i[1])  # get the operator sign
                        len_first_num.append(len(i[0]))  # get the length of the first number
                        len_sec_num.append(len(i[2]))  # get the length of the second number

                # set variables
                empty_space = ' '
                sort_out_list = ''

                # out put processing
                if result == True:
                        for i in range(len(operators)):

                                # check out for operator signs
                                if operators[i] == '+':
                                        out_put_result.append(str(first_num[i] + sec_num[i]))

                                else:
                                        out_put_result.append(str(first_num[i] - sec_num[i]))

                # set lenght of upper operand (number) - First line
                for i in range(len(first_num)):
                        width_first_num = max(len(str(first_num[i])), len(str(sec_num[i]))) + 2
                        sort_out_list += 4 * empty_space + str(first_num[i]).rjust(width_first_num)
                sort_out_list = sort_out_list.rstrip()  # copy
                sort_out_list += "\n"

                # set lenght of bottom operand (number) - Second line
                for i in range(len(sec_num)):
                        width_sec_num = max(len(str(first_num[i])), len(str(sec_num[i]))) + 1
                        sort_out_list += 4 * empty_space + (str(operators[i]) + (str(sec_num[i])).rjust(width_sec_num))
                sort_out_list = sort_out_list.rstrip()  # copy
                sort_out_list += "\n"

                # set the number of 'dash' signs - Third line
                for i in range(len(sec_num)):
                        dash_sign_len = max(len(str(first_num[i])), len(str(sec_num[i]))) + 2
                        sort_out_list += 4 * empty_space + '-' * dash_sign_len
                sort_out_list = sort_out_list.rstrip()

                # arranger and arithmetic out put
                if result:
                        sort_out_list += "\n"
                        for i in range(len(out_put_result)):
                                width_result = max(len(str(first_num[i])), len(str(sec_num[i]))) + 2
                                sort_out_list += 4 * empty_space + str(out_put_result[i]).rjust(width_result)
                        sort_out_list = sort_out_list.rstrip()

                # Empty the lists
                clean_list.clear()
                first_num.clear()
                sec_num.clear()
                len_first_num.clear()
                len_sec_num.clear()

        return print(sort_out_list, end='\n\n')
