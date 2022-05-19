from time import sleep
from collatz import *
from timerClass import *
import PySimpleGUI as pg
import ShitShuffler



def MainOne():
    t = Timer()
    t.start()
    test = [0,1]
    for i in range(50):
        test.append(test[i]+test[i+1])
    print(test)
    printLBL( " test", 0.5)
    t.stop()
    print(t.getElapsed())

def MainTwo():
    ShitShuffler.Run()

def MainThree():
    
    lay = [[pg.Text('Length of list | repeat')], 
           [pg.InputText(size=(10,1), key='input'), pg.InputText(size=(10,1), key='repeat')],
           [pg.Button('Submit')],
           [pg.Text('test', key = '-OUTPUT-')]]
    win = pg.Window('Collatz', layout=lay)
    while True:
        event, values = win.read()
        
        if event == 'Submit':
            win['-OUTPUT-'].update(str(
                ShitShuffler.RunFunc(values['input'], values['repeat'])) + " failed")
        elif event == pg.WIN_CLOSED:
            break

        

    

    #pg.Window('Test', lay, margins=(100,100)).read()
def MainFour():
    lay = [[pg.InputText('test', key='input')],
    [pg.Text(key='output', text='test')], [pg.Button('Submit')]]
    win = pg.Window('bruh', layout=lay)
    while True:
        event, values = win.read()
        if event == pg.WIN_CLOSED:
            break
        elif event == 'Submit':
            win['output'].update(values['input'])
    win.close()





MainFour()
