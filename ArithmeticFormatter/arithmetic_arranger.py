def arithmetic_arranger(problems, B = None):
    let = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    soln = 0
    str = ""
    opStr = ""
    numspace = " "
    dash = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for i in enumerate(problems):
            if "+" not in i[1] and "-" not in i[1]:
                return "Error: Operator must be '+' or '-'."
            for letters in let:
                if letters in i[1] or letters.upper() in i[1]:
                   return "Error: Numbers must only contain digits."
            if len(i[1].split()[0]) > 4 or len(i[1].split()[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                if len(i[1].split()[0]) < len(i[1].split()[2]):
                    str += "  " + numspace*(len(i[1].split()[2]) - len(i[1].split()[0])) + i[1].split()[0] + "    "
                    opStr += i[1].split()[1] + " " + i[1].split()[2] + "    "
                    dash += "-"*(len(i[1].split()[2]) + 2) + "    "
                else:
                    str += "  " +  i[1].split()[0] + "    "
                    opStr += i[1].split()[1] + " " + numspace*(len(i[1].split()[0]) - len(i[1].split()[2])) + i[1].split()[2] + "    "
                    dash += "-"*(len(i[1].split()[0]) + 2) + "    "
            if i[1].split()[1] == "+":
                soln = int(i[1].split()[0]) + int(i[1].split()[2])
            elif i[1].split()[1] == "-":
                soln = int(i[1].split()[0]) - int(i[1].split()[2])
            ans += numspace*(len('{}'.format(max(int(i[1].split()[0]), int(i[1].split()[2])))) + 2 - len('{}'.format(soln))) + '{}'.format(soln) + "    "
    arranged_problems = str[:-4] + "\n" + opStr[:-4] + "\n" + dash[:-4]
    if B == True:
        arranged_problems = str[:-4] + "\n" + opStr[:-4] + "\n" + dash[:-4] + "\n" + ans[:-4]
    return arranged_problems
