import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
all_states: pandas.Series = data.state
# guessed_states = []
guessed_states: pandas.Series = pandas.Series(dtype=str)
# print(all_states.values)
# print('Alabama' in all_states)
# guessed_states = guessed_states.repeat(all_states.size)
# print(all_states)
# print(all_states)
# print(guessed_states)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    # if answer_state == "Exit":
    if answer_state is None:
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # new_data = pandas.DataFrame(missing_states)
        new_data = pandas.DataFrame(set(all_states.values) - set(guessed_states.values), columns=['Forgotten States'])
        print(new_data)
        new_data.to_csv("states_to_learn.csv", index=True)
        break
    elif answer_state.title() in all_states.values:
        answer_state = answer_state.title()
        guessed_states = pandas.concat([guessed_states, pandas.Series(answer_state)])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
