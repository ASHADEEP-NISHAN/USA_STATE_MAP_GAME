import turtle
import pandas
font_tuple = ("Arial", 12, "bold")

state_data=pandas.read_csv("50_states.csv")
all_state=state_data.state.tolist()
screen=turtle.Screen()
screen.title("U.S STATE GAME")
screen.bgpic("blank_states_img.gif")
crt_st=0
guessed_state=[]
while len(guessed_state)<50:
    input = screen.textinput(f"{crt_st}/50 states correct", "what is another state name ?").title()
    if input == "Exit":
        missed_state = [i for i in all_state if i not in guessed_state]
        new_data=pandas.DataFrame(missed_state)
        new_data.to_csv("state_to_learn.csv")
        break

    if input in all_state:
        crt_st+=1
        guessed_state.append(input)
        tim=turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        coordinate = state_data[state_data.state == input]
        x_cor = coordinate.x.tolist()
        y_cor = coordinate.y.tolist()
        tim.goto(x_cor[0],y_cor[0])
        tim.pendown()
        tim.write(input)




