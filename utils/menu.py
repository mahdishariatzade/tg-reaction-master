# import threading
#
#
# class KeyboardThread(threading.Thread):
#
#     def __init__(self, input_cbk=None, name='keyboard-input-thread'):
#         self.input_cbk = input_cbk
#         super(KeyboardThread, self).__init__(name=name)
#         self.start()
#
#     def run(self):
#         while True:
#             self.input_cbk(input())  # waits to get input + Return
#
#
# showcounter = 0  # something to demonstrate the change
#
#
# def my_callback(inp):
#     # evaluate the keyboard input
#     print('You Entered:', inp, ' Counter is at:', showcounter)
#
#
# # start the Keyboard thread
# kthread = KeyboardThread(my_callback)
#
# import time
# while True:
#     time.sleep(1)
#     print(time.time())
#     # the normal program executes without blocking. here just counting up
#     showcounter += 1
#
# # import threading
# #
# # consoleBuffer = []
# # text = None
# #
# #
# # def consoleInput():
# #     while True:
# #         global text
# #         text = input()
# #
# #
# # threading.Thread(target=consoleInput, args=(), daemon=True).start()  # start the thread
# #
# # import time  # just to demonstrate non-blocking parallel processing
# #
# # while True:
# #     time.sleep(2)  # avoid 100% cpu
# #     print(time.time())  # just to demonstrate non-blocking parallel processing
# #     if text:
# #         print(f'"{text}"')
# #         text = None


from threading import Thread
from random import choice
from time import sleep
from queue import Queue, Empty
import curses

commandQueue = Queue()

screen = curses.initscr()
height, width = screen.getmaxyx()
curses.curs_set(0)
screen.keypad(True)
# screen.box()
upperwin = screen.subwin(2, 40, 2, 2)
lowerwin = screen.subwin(5, 2)


def outputThreadFunc():
    outputs = ["So this is another output", "Yet another output", "Is this even working"]  # Just for demo
    while True:
        upperwin.clear()
        upperwin.addstr(f"{choice(outputs)}")
        try:
            inp = commandQueue.get(timeout=0.1)
            if inp == 'exit':
                return
            else:
                upperwin.addch('\n')
                upperwin.addstr('input: ' + inp)
        except Empty:
            pass

        upperwin.refresh()
        sleep(1)


def inputThreadFunc():
    while True:
        global buffer

        lowerwin.addstr("->")

        command = lowerwin.getstr()

        if command:
            command = command.decode("utf-8")
            commandQueue.put(command)
            lowerwin.clear()

            lowerwin.refresh()
            if command == 'exit':
                return


# MAIN CODE
outputThread = Thread(target=outputThreadFunc)
inputThread = Thread(target=inputThreadFunc)
outputThread.start()
inputThread.start()
outputThread.join()
inputThread.join()

screen.keypad(False)
curses.endwin()
print("Exit")
