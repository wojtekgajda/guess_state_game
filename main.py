import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')

state_turtle = turtle.Turtle()

data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()

bcg_img = 'blank_states_img.gif'
screen.addshape(bcg_img)
turtle.shape(bcg_img)
state_turtle.hideturtle()
state_turtle.penup()
state_turtle.setheading(90)

guessed_states = []

game_on = True
while game_on:
    print(guessed_states)
    points = len(guessed_states)
    user_answer = screen.textinput(title=f'Score: {points} of 50', prompt='Guess name:').title()

    # USE EXIT to save file with missing statest to learn
    if user_answer == 'Exit':

        missing_states = [state for state in state_list if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if user_answer in state_list and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        state_info = data[data.state == user_answer]
        x = float(state_info.x)
        y = float(state_info.y)
        print(x, y)
        state_turtle.goto(x, y)
        state_turtle.write(f'{user_answer}', font=('Roboto', 14, 'normal'), align='center')

    if points == 50:
        game_on = False
        state_turtle.goto(-150, 250)
        state_turtle.color('green')
        state_turtle.write('WINNER WINNER WINNER', font=('Roboto', 24, 'bold'))

turtle.mainloop()
