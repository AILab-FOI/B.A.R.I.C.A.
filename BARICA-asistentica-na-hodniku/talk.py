#!/usr/bin/env python3

import logging
logging.basicConfig( filename='/home/barica/heard.log', format='%(asctime)s %(message)s', level=logging.INFO )

from transitions import Machine

from chatterbot import ChatBot

import argparse

from pyautogui import press, locateCenterOnScreen, hotkey, click

import sys

from time import sleep, asctime

import pyperclip as cp

import webbrowser

import subprocess

import os

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import _thread

from collections import OrderedDict

from threading import Timer

from resettabletimer import ResettableTimer

from ScrapInformation import *

from selenium import webdriver
# Global driver 
DRIVER = None


from time import asctime
dirname = os.path.dirname( os.path.abspath( __file__ ) )    


from dictionary import *


# Last sentence
LAST_SENTENCE = cp.paste().lower()

# Websocket communication buffer (e.g. messages to be sent)
BUFFER = []

driver_for_shown_schedule = None

import platform
if platform.system() == 'windows':
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
else:
    startupinfo = None

def go_to_x_slide(x):
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, 'build/index.html')
    try:
        DRIVER.get('file://' + filename + '#/step-' + x)
    except:
        print( 'Error moving to slide', x )

def timeout_schedule_close():
    global driver_for_shown_schedule
    if driver_for_shown_schedule != None:
        close_schedule()

def timeout_command():
    m.listen_input()
    cp.copy('refresh_command')
    go_to_x_slide('1')
timer_command = ResettableTimer(45, timeout_command)
timer_command.start()

class NLPController(WebSocket):

    def __init__( self, *args, **kwargs ):
        WebSocket.__init__( self, *args, **kwargs )
        _thread.start_new_thread( self.listen, () )
        

    def listen( self ):
        global BUFFER
        while True:
            try:
                if BUFFER:
                    BUFFER = list( OrderedDict.fromkeys( BUFFER ) )                   
                    cmd = BUFFER.pop()
                    self.sendMessage(str(cmd))
                sleep( 0.5 )
            except Exception as e:
                print(e)
        
    def handleMessage( self ):
        self.sendMessage( self.data )

    def handleClose( self ):
        sys.exit()

class FiniteStateMachine:
    
    states = ['listen', 'yes', 'foi_generally', 'which_classroom', 'classroom', 'which_professor',
              'professor', 'which_kind_of_study', 'which_year_of_study', 'which_group', 'schedule']

    def __init__(self):

        # Initialize the state machine
        self.machine = Machine(model=self, states=FiniteStateMachine.states,
                               initial='listen')
        
        # Add transitions (trigger, source_state, destination_state)
        self.machine.add_transition('barice_input', '*', 'yes')
        
        self.machine.add_transition('foi_input', 'yes', 'foi_generally',
                                    after='foi_generally_output')
        
        self.machine.add_transition('classroom_input', 'yes', 'which_classroom')
        self.machine.add_transition('classroomN_input', 'which_classroom', 'classroom',
                                    after='classroom_output')
        
        self.machine.add_transition('professor_input', 'yes', 'which_professor')
        self.machine.add_transition('professorN_input', 'which_professor', 'professor',
                                    after='professor_output')
        
        self.machine.add_transition('schedule_input', 'yes', 'which_kind_of_study',
                                    after='kind_of_study_output')
        self.machine.add_transition('kind_of_study_input', 'which_kind_of_study',
                                    'which_year_of_study', after='year_of_study_output')
        self.machine.add_transition('year_of_study_input', 'which_year_of_study',
                                    'which_group', after='groupN_output')
        self.machine.add_transition('groupN_input', 'which_group', 'schedule',
                                    after='schedule_output')

        self.machine.add_transition('listen_input', '*', 'listen')

    def foi_generally_output(self):
        go_to_x_slide('2')
        print(d['FOI'][self.CMD])
        global BUFFER
        BUFFER.append('FOI')
        self.listen_input()

    def classroom_output(self):
        self.listen_input()

    def professor_output(self):
        go_to_x_slide('3')
        global BUFFER
        name = str(self.professor).split('#')
        BUFFER.append('PROFESOR ' + name[0])
        self.listen_input()

    def kind_of_study_output(self):
        go_to_x_slide('4')
        print(d['Raspored'][self.CMD])
        global BUFFER
        BUFFER.append('KOJA_VRSTA_STUDIJA')

    def year_of_study_output(self):
        go_to_x_slide('5')
        print(d['Vrsta_studija'][self.CMD])
        global BUFFER
        BUFFER.append('KOJA_GODINA')

    def groupN_output(self):
        global BUFFER, dirname
        there_is_schedule = scrapGroups(str(self.kind_of_study), str(self.year_of_study))
        if there_is_schedule != 'Nema':
            BUFFER.append('GROUPS ' + str(there_is_schedule))
            go_to_x_slide('6')
            print(d['Godina_studija'][self.CMD])
        else:
            go_to_x_slide('7')
            print('Raspored nedostupan')
            BUFFER.append('RASPORED_NE_POSTOJI')
            self.listen_input()

    def schedule_output(self):
        global BUFFER
        global driver_for_shown_schedule
        driver_for_shown_schedule = scrapSchedule(str(self.kind_of_study),
                                       str(self.year_of_study), str(self.group))
        driver_for_shown_schedule.switch_to_window(driver_for_shown_schedule.current_window_handle)
        timer_schedule = Timer(2 * 60, timeout_schedule_close)
        timer_schedule.start()
        press( 'f11' )
        press( [ 'down' ] * 9 )
        done = False
        while not done:
            try:
                x, y = locateCenterOnScreen( os.path.join( dirname, 'images/close.png' ) )
                click( x, y )
                done = True
            except:
                sleep( 1 )
        print(d['Grupa'][self.CMD])
        BUFFER.append('RASPORED')
        self.listen_input()

    
def main_branch(SENTENCE):
    global BUFFER
    CMD = chatbot.get_response( SENTENCE )
    m.CMD = CMD
    if CMD in d['Izvoli']:
        m.barice_input()
        print(d['Izvoli'][CMD])        
        BUFFER.append('IZVOLI')
    elif CMD in d['FOI']:
        m.foi_input()
    elif CMD in d['Dvorana']:
        m.classroom_input()
        print(d['Dvorana'][CMD])
        BUFFER.append('KOJA_DVORANA')
    elif CMD in d['Profesor']:
        m.professor_input()
        print(d['Profesor'][CMD])
        BUFFER.append('KOJI_PROFESOR')
    elif CMD in d['Raspored']:
        m.schedule_input()       
    else: BUFFER.append('PONOVI')

def classroom_branch(SENTENCE):
    CMD = chatbotClassroom.get_response( SENTENCE )
    if CMD in d['Izvoli']:
        m.barice_input()
        print(d['Izvoli'][CMD])
        BUFFER.append('IZVOLI')
    elif CMD in d['Dvorane']:
        m.classroomN_input()
        print(d['Dvorane'][CMD])
        BUFFER.append('DVORANA ' + str(CMD))
    else: BUFFER.append('PONOVI')
    
def professor_branch(SENTENCE):
    CMD = chatbotProfessor.get_response( SENTENCE )
    m.CMD = CMD
    if CMD in d['Izvoli']:
        m.barice_input()
        print(d['Izvoli'][CMD])
        BUFFER.append('IZVOLI')
    elif CMD in d['Profesori']:
        m.professor = CMD
        m.professorN_input()
    else: BUFFER.append('PONOVI')

def schedule_branch(SENTENCE):
    CMD = chatbotSchedule.get_response( SENTENCE )
    m.CMD = CMD
    if CMD in d['Izvoli']:
        m.barice_input()
        print(d['Izvoli'][CMD])
        BUFFER.append('IZVOLI')
    elif CMD in d['Vrsta_studija']:
        m.kind_of_study = CMD
        m.kind_of_study_input()
    elif CMD in d['Godina_studija']:
        m.year_of_study = CMD
        m.year_of_study_input()
    elif CMD in d['Grupa']:
        print(CMD)
        m.group = CMD
        m.groupN_input()
    else: BUFFER.append('PONOVI')

def processing_input():
    global LAST_SENTENCE
    SENTENCE = LAST_SENTENCE
    
    """if SENTENCE == 'izlaz':
        DRIVER.quit()
        os._exit(1)"""
        
    if m.state == 'listen' or  m.state == 'yes': main_branch(SENTENCE)
        
    elif m.state == 'which_classroom': classroom_branch(SENTENCE)

    elif m.state == 'which_professor': professor_branch(SENTENCE)                          

    elif m.state == 'which_kind_of_study' or m.state == 'which_year_of_study' or m.state == 'which_group':
        schedule_branch(SENTENCE)

    else: BUFFER.append('PONOVI')

def close_schedule():
    global driver_for_shown_schedule
    driver_for_shown_schedule.close()
    driver_for_shown_schedule = None

    
def listen():
    global LAST_SENTENCE
    sleep( 0.5 )
    l = cp.paste().lower()
    if l != LAST_SENTENCE:
        if l != 'refresh_command':
            global timer_command
            timer_command.reset()
            global driver_for_shown_schedule
            if driver_for_shown_schedule != None: close_schedule()
            x = LAST_SENTENCE
            LAST_SENTENCE = l
            print( 'Heard:', l )
            logging.info( str( l ) )
            processing_input()
            
def start_presentation():
    dirname = os.path.dirname(os.path.abspath(__file__))
    p = subprocess.Popen(['hovercraft', os.path.join(dirname, 'presentation', 'prezentacija.rst'), 'build'],
                         startupinfo=startupinfo)
    sleep( 1 )
    go_to_x_slide( '1' )
    press( 'f11' )
    hotkey( 'ctrl', '+' )
    done = False
    while not done:
        try:
            sleep( 1 )
            x, y = locateCenterOnScreen( os.path.join( dirname, 'images/start-movie.png' ) )
            click( x, y )
            x, y = locateCenterOnScreen( os.path.join( dirname, 'images/close.png' ) )
            click( x, y )
            done = True
        except:
            pass

def start_text_to_speech():
    start_minimized( '/usr/bin/google-chrome', '--password-store=basic --window-position=0,0 --window-size=1,1 "https://voicenotebook.com/?autostart=1&chkinteg=1&chkbufer=1&pagelang=hr-HR"' )
    #p = subprocess.Popen( [ 'google-chrome', '--password-store=basic', 'https://voicenotebook.com/?autostart=1&chkinteg=1&chkbufer=1&pagelang=hr-HR' ], startupinfo=startupinfo )
    sleep( 1 )

def start_remote_login():
    start_minimized( '/usr/bin/teamviewer' )

def start_minimized( command, args='' ):
    
    command_check = command.split("/")[-1]

    subprocess.Popen( ["/bin/bash", "-c", command + ' ' + args], startupinfo=startupinfo )

    t = 1
    while t < 30:
        try:
            w_list = [l.split() for l in subprocess.check_output(["wmctrl", "-lp"]).decode("utf-8").splitlines()]
            proc = subprocess.check_output(["pgrep", "-f", command_check]).decode("utf-8").strip().split()
            match = sum([[l[0] for l in w_list if p in l] for p in proc], [])
            subprocess.Popen(["xdotool", "windowminimize", match[0]])
            break
        except (IndexError, subprocess.CalledProcessError):
            pass
        t += 1
        sleep(1)
    
    

m = FiniteStateMachine()
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( "--train", const=True, nargs='?', type=bool, help="Specify if the agent shoud be trained. If not specified agent will be started in default (listening) mode.")
    args = parser.parse_args()

    TRAIN = bool( args.train )

    la = [
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.75,
            'default_response': 'Ponovi unos molim.'
        }
    ]

    chatbot = ChatBot(
        'BARICA_HR',
        read_only=not TRAIN,
        logic_adapters=la,
        database=os.path.join( dirname, 'db.sqlite3' ) )
    chatbotClassroom = ChatBot(
        'BARICA_HR_CLASSROOM',
        read_only=not TRAIN,
        logic_adapters=la,
        database=os.path.join( dirname, 'dbC.sqlite3' ) )
    chatbotProfessor = ChatBot(
        'BARICA_HR_PROFESSOR',
        read_only=not TRAIN,
        logic_adapters=la,
        database=os.path.join( dirname, 'dbP.sqlite3' ) )
    chatbotSchedule= ChatBot(
        'BARICA_HR_SCHEDULE',
        read_only=not TRAIN,
        logic_adapters=la,
        database=os.path.join( dirname, 'dbS.sqlite3' ) )

    if TRAIN:
            from train import *
            from trainClassroom import *
            from trainProfessor import *
            from trainSchedule import *
            train( chatbot )
            trainClassroom( chatbotClassroom )
            trainProfessor( chatbotProfessor )
            trainSchedule ( chatbotSchedule )
            scrapProfessorsForPresentation()
            sys.exit()

    start_remote_login()
    start_text_to_speech()

    d = dictionary()
    print( 'Done scraping!' )
    
    server = SimpleWebSocketServer( '', 8009, NLPController )
    _thread.start_new_thread( server.serveforever, () )
            

    # Change to execute in the another browser
    DRIVER = webdriver.Chrome()
    sleep( 1 )
    start_presentation()
    
    while True:
        
        try:
            listen()
        except Exception:
            pass
            BUFFER.append('PONOVI')
