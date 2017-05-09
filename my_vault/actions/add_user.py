import sys
import yaml

from st2actions.runners.pythonrunner import Action

#from vault.write import VaultWriteAction as vault_write

class MyAuthUser(Action):
    def run(self, users_list , new_user):
        vault_path="secret/demo"
        #print("current slack user :   ",user)
        print("users_list: ", users_list)
        print (type(users_list))
        print("add user: ", new_user) 
        if users_list.has_key('users') :
             print ("has key users")
             users_list['users'] = yaml.load(users_list['users'])
             users_list['users'].append(new_user.encode("utf-8"))
	     users_list['users'] = [ ",".join(users_list['users']).encode("utf-8")]
        else :
             print ("no user key")
             users_list={'users':[new_user]}
	return users_list
        #return vault_write.run(path=vault_path,values=users_list)
      
