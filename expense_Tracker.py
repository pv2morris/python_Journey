expenses = []

while True:
    expense_Val = input('Please enter an expense to be tracked: ')
    if expense_Val == '':
        break
    try:
        expenses.append(float(expense_Val))
    except ValueError:
        print('Please enter your expenses as decimal numbers.')

num_expenses = len(expenses)

if num_expenses > 0: 
    total = sum(expenses)
    average = total / num_expenses
    print(f'Your expense total is: {total:.2f}')
    print(f'Your total number of expenses is: {num_expenses}')
    print(f'Your expense average is: {average:.2f}')
else:
    print('No expenses were entered.')