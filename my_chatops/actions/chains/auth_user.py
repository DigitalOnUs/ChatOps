import sys

from st2actions.runners.pythonrunner import Action

class MyAuthUser(Action):
    def run(self, users_list , user):
        print("current slack user :   ",user)
        print("users_list: ", users_list)
        if user == 'jasmeet.kohli':
            return (True)
        return (False)

