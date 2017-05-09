import sys
import json,ast

from st2actions.runners.pythonrunner import Action

class MyAuthAdmin(Action):

    def run(self, admin_list , admin):
        
    	admin_list = ast.literal_eval(json.dumps(admin_list))	
	adin = admin.encode("utf-8")
        print("current slack user :   ",admin)
        print("admin_list: ", admin_list)
        
        #users_dict=yaml.load(users_list)   
        #print ("users dict: ", users_dict)
        if (admin in admin_list['admins']):
            return (True)
        exit(1)

