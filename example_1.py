
from sneakers.ttk import *

def ex0():
    with window(geometry=(500, 200)):

        @button("Create a popup box")
        def makePopupBox():
            showInfo(message = "You clicked the button")


def ex1():
    with window("sneakers window"):

        label("Label", font="Verdana 18 bold underline")

        with flow():

            with stack(padx=10):
                message("Below is a combination of a stack and two flows, forming a grid", width=140, borderwidth=1)

                @button("Yes / No / cancel")
                def yes_no_cancel():
                    response = askYesNoCancel(message = "What do?")
                    if response is True:
                        showInfo(message = "You pressed yes")
                    elif response is False:
                        showWarning(message = "You pressed no")
                    elif response is None:
                        showError(message = "You pressed cancel")

if __name__ == '__main__':
    ex0()
    # ex1()
