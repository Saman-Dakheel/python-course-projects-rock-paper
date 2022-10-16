import random as r

auto_select = ['rock', 'paper', 'scissors']
while True:
    your_choice = input('Enter your Choice ( rock , paper , scissors )!! ')
    if your_choice in auto_select:
        auto_selected = r.choice(auto_select)
        print(f'You Choose {your_choice}')
        print(f'Computer Choose {auto_selected}')
    else:
        print('you enter incorrect word')
        break
    if your_choice == auto_selected:
        print('You Both Choose Same (Draw)')
    elif your_choice == 'rock':
        if auto_selected == 'scissors':
            print('You Win !!!')
        else:
            print('You Lose !!!')
    elif your_choice == 'paper':
        if auto_selected == 'rock':
            print('You Win !!!')
        else:
            print('You Lose !!!')
    elif your_choice == 'scissors':
        if auto_selected == 'paper':
            print('You Win !!!')
        else:
            print('You Lose !!!')
    again = input('Do you want play again (y/n)')
    if again == 'n':
        break



# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('white')
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x//100 + 1)
#     t.forward(x)
#     t.left(59)
