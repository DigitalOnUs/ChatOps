import sys

from st2actions.runners.pythonrunner import Action

class MyAuthUser(Action):
    def run(self, message):
        print(message)

        if message == 'working':
            return (True, message)
        return (False, message)

