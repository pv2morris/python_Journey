grades = []
while True:
    grade_Val = input('Please enter a grade to be calculated or press Enter: ')

    if grade_Val == '':
        break
    try:            
        grades.append(float(grade_Val))
    except ValueError:
        print('Please enter the grade as a decimal value.')

if grades:
    average = sum(grades)/len(grades)
    if average >= 90:
        letter_Grade = 'A'
    elif average >= 80:
        letter_Grade = 'B'
    elif average >= 70:
        letter_Grade = 'C'
    elif average >= 60:
        letter_Grade = 'D'
    else:
        letter_Grade = 'F'
    
    print(f'The average of your grades is: {average:.2f}')
    print(f'Your final letter grade is: {letter_Grade}')
else:
        print('No grades were entered.')