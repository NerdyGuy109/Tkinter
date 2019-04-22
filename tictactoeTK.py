

import tkinter


def click(tag):
    toggleText(btnList, tag)
    checkForWin(grid)


def createGrid():
    tag = 0
    for row in range(3):
        for column in range(3):
            btn = tkinter.Button(root)
            btn['text'] = tag
            btn['width'] = 15
            btn['height'] = 5
            btn['command'] = lambda tag = tag : click(tag)
            btn.grid(row=row, column=column)
            btnList.append(btn)
            tag += 1
    return btnList

def toggleText(btnList, tag):
    btn = btnList[tag]
    text = btn['text']
    if text == tag:
        btn['text'] = "X"
    elif text == "X":
        btn['text'] = "O"
    else:
        btn['text'] = tag


def checkForWin(btnList):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for win in wins:
        x, y, z = win[0], win[1], win[2]
        btn1 = btnList[x]
        btn2 = btnList[y]
        btn3 = btnList[z]
        if btn1['text'] == btn2['text']:
            if btn1['text'] == btn3['text']:
                print("%s is the Winner" % btn1['text'])

root = tkinter.Tk()

btnList = []
grid = createGrid()

root.mainloop()
