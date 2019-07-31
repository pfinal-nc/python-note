# -*- coding: utf-8 -*-
import itchat

if __name__ == "__main__":
    itchat.auto_login()
    friends = itchat.get_friends(update=True)
    print(friends)
    