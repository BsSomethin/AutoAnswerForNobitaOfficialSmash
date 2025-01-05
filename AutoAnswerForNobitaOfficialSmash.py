# Ported by brostos to api 8
# Tool used to make porting easier
"""python 3.9 |  for a beutiful game  - BombSquad OwO"""
# modded by Bsomthin.
# have fun

# thnx to FireFighter1037 閵嗏偓and IM_NOT_PRANAV#7874
            
# -*- coding: utf-8 -*-
# Ported by brostos to api 8
# ba_meta require api 8

import threading
import time
from typing import Callable, TypeVar
from bascenev1 import get_foreground_host_activity, get_foreground_host_session, get_game_roster, get_chat_messages, chatmessage as cmsg
from bauiv1 import set_party_icon_always_visible, screenmessage as smsg
import babase
from bauiv1lib.gather.publictab import PublicGatherTab
import bauiv1 as bui
import bascenev1 as bs
from bauiv1lib import mainmenu

                    
                                               
                               



# Our cmd which enables the mode usually. when it is not.
px = '/'

# main class


class _Ans:

    def _auto_ans():
        try:
            messages = get_chat_messages()
            if len(messages) > 1:
                lastmsg = messages[len(messages)-1]

                m = lastmsg.split(' ')[1]
                if m.startswith(''):
                    return _Ans._ans()
                else:
                    pass
        except:
            pass

    def _ans():
        messages = get_chat_messages()
        if len(messages) > 1:
            lastmsg = messages[len(messages)-1]

            m = lastmsg.split(' ')[1]  # question starting word
            n = lastmsg.split(' ')[2:]  # other words
            
            def maths():
                a=n[1] 
                b=n[3].split('?')
                c=b
                d=c[0]
                f=int(a)
                e=int(d)
                if n[2]=='+':
                     added=f+e
                     ad=str(added)
                     cmsg(ad)
                elif n[2]=='x':
                    multiplyed=f*e
                    multi=str(multiplyed)
                    cmsg(multi)
                else:
                        return None    
            if m == px:
                 cmsg(px+'help for help')
            elif m =='hi':
                    cmsg('hey bro')
            elif m == 'Who':
                if n[0]=='modded' and n[1] == 'the' and n[2]=='server?':
                    cmsg('Nobita')
                elif n[0]=='is'and n[1]=='the' and n[2]=='owner' and n[3]=='of' and n[4]== 'Server?':
                    cmsg('Nobita')
                elif n[0] == 'Is' and n[1]=='The' and n[2]=='leader' and n[3]=='of' and n[4]=='SYCOO?':
                    cmsg('Nobita') 
                elif n[0]=='Is' and n[1]=='The' and n[2]=='Popular' and n[3]=='Manager' and n[4]=='Of' and n[5]=='This' and n[6]=='Server?':
                    cmsg('khyati')
                else:
                    return None
            elif m =="If":
                if n[0]=="you" and n[1]=="don't"  and n[2]=="keep" and n[3] == "me,"  and n[4]=="I'll" and n[5]=="break." and n[6] =="What" and n[7]=="am" and n[8]=="I?":
                    cmsg('promise')
                else:
                    return None
            elif m == 'What':
                if n[0]=='do' and n[1]=='you' and n[2]=='call' and n[3]=='a' and n[4]=='bear' and n[5]=='without' and n[6]=='ears?':
                    cmsg('b')
                elif n[0]=='is' and n[1]=='easy' and n[2]=='to' and n[3] =='get' and n[4]=='into' and n[5]=='but' and n[6] == 'hard' and n[7]=='to' and n[8]=='get' and n[9]=='out' and n[10]=='of?':
                    cmsg('trouble')
                elif n[0]=='language' and n[1]=='does' and n[2]=='bombsquad' and n[3]=='run' and n[4]=='on?':
                    cmsg('python')    
                elif n[0]=='is':
                	maths()
                elif lastmsg=='How are you?':
                    cmsg('good')    
                else:
                    return None
            else:
                return None       

class NewMainMenuWindow(mainmenu.MainMenuWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Display chat icon, but if user open/close gather it may disappear
        bui.set_party_icon_always_visible(True)

# bs.timer(0.05, _update, repeat=True)


def same():
    _Ans._auto_ans()
# ba_meta export babase.Plugin


class autoChaterByBsSomethin(babase.Plugin):
    timer = bs.AppTimer(0.5, same, repeat=True)

    def on_app_running(self):
        mainmenu.MainMenuWindow = NewMainMenuWindow
    
