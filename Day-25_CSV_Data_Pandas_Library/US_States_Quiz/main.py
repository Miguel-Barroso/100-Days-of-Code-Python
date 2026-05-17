import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
# Once image (which must be .gif) has been added to the screen object, it can be used with a turtle object
turtle.shape(image)

# How Angela got hold of the x and y coordinates of the states on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor())

# Get hold of the list of states
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


# print(type(states_list))

# Get hold of state's index
def get_state_index(answer):
    index = 0
    for state in states_list:
        if state == answer:
            return index
        index += 1


# Get hold of the coordinates for a given state
def get_state_coordinates(answer):
    state_row = data[data.state == answer]
    state_xcor = state_row.x[state_index]
    state_ycor = state_row.y[state_index]
    coordinates = (state_xcor, state_ycor)
    return coordinates


def write_answer(answer):
    timmy = turtle.Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(state_coordinates)  # Could also have been (state_row.x.item(), state_row.y.item(), check the solution
    timmy.write(answer)


list_of_correct_guesses = []

while len(list_of_correct_guesses) < 50:
    screen.title(f"U.S. States Game {len(list_of_correct_guesses)}/50")
    # Ask for user input
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    # Exit the game if asked to
    if answer_state == "Exit":
        print(f"List of correct guesses: {list_of_correct_guesses}")
        states_to_learn = [item for item in states_list if item not in list_of_correct_guesses]
        # for every_state in list_of_correct_guesses:
        #     print(f"Current state: {every_state}")
        #     states_list.remove(every_state)
        # print(f"You need to study: {len(states_list)} states:")
        # print(states_list)
        print(f"States left to learn: {states_to_learn}")
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break

    # Check to see if the state exists
    if answer_state in states_list:
        print(f"Your answer: '{answer_state}', is a state")
        state_index = get_state_index(answer_state)
        # print(state_index)
        state_coordinates = get_state_coordinates(answer_state)
        # print(state_coordinates)
        write_answer(answer_state)
        list_of_correct_guesses.append(answer_state)
    else:
        print(f"Your answer: '{answer_state}', does not exist")

# screen.exitonclick()
# turtle.mainloop()  # Keeps the screen open, similar to the commented line above, though not needed anymore
