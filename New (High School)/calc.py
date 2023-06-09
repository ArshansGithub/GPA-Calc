GRADES = []
CONVERTED_GRADES = 0

while True:
    prompt = input("Grade (Type x when done): ")
    if "x" not in prompt:
        GRADES.append(prompt)
    else:
        break
for val in GRADES:
    if val.isdigit():
        if float(val) <= 69.99 and float(val) >= 60.00:
           CONVERTED_GRADES += 1
        elif float(val) <= 79.99 and float(val) >= 70.00:
           CONVERTED_GRADES += 2
        elif float(val) <= 89.99 and float(val) >= 80.00:
           CONVERTED_GRADES += 3
        elif float(val) >= 90.00:
            CONVERTED_GRADES += 4
    elif '.' in val:
        if float(val) <= 69.99 and float(val) >= 60.00:
           CONVERTED_GRADES += 1
        elif float(val) <= 79.99 and float(val) >= 70.00:
           CONVERTED_GRADES += 2
        elif float(val) <= 89.99 and float(val) >= 80.00:
           CONVERTED_GRADES += 3
        elif float(val) >= 90.00:
            CONVERTED_GRADES += 4
    else:
        if 'D' in val:
            CONVERTED_GRADES += 1
        elif 'C' in val:
            CONVERTED_GRADES += 2
        elif 'B' in val:
            CONVERTED_GRADES += 3
        elif 'A' in val:
            CONVERTED_GRADES += 4
print("Your GPA: " + str(CONVERTED_GRADES / len(GRADES)))
