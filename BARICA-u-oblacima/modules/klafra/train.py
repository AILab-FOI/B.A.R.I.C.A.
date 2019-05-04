#!/usr/bin/env python3

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def train( bot ):

    chatbot = ListTrainer( bot )
    bot.set_trainer( ListTrainer )
    chatbot = bot

    fl = open( 'data/train_filtered.txt', 'r' )
    data = fl.readlines()
    data = [ i[ :-1 ] for i in data ]

    chatbot.train( data )


if __name__ == '__main__':
    from talk import chatbot
    train( chatbot )
