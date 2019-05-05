#!/usr/bin/env python3

# Most of the code stolen from:
# https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

import os
import time
import re
from slackclient import SlackClient
#from talk import answer


# instantiate Slack client
token = os.environ.get( 'SLACK_BOT_TOKEN' )
if token:
    slack_client = SlackClient( token )
    # starterbot's user ID in Slack: value is assigned after the bot starts up
    starterbot_id = None
else:
    print( "Warning, no Slack bot token detected, Slack functionality will be disabled! \nDefine Slack bot token with:\nexport SLACK_BOT_TOKEN=<Your token>" )

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

    
def parse_bot_commands( slack_events ):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    global starterbot_id
    for event in slack_events:
        if event[ "type" ] == "message" and not "subtype" in event:
            text = event[ "text" ]
            user_id, message = parse_direct_mention( text )
            if user_id == starterbot_id:
                return message, event[ "channel" ]
    return None, None

def parse_direct_mention( message_text ):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search( MENTION_REGEX, message_text )
    # the first group contains the username, the second group contains the remaining message
    return ( matches.group( 1 ), matches.group( 2 ).strip() ) if matches else ( None, None )

def handle_command( command, channel ):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format( EXAMPLE_COMMAND )

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith( EXAMPLE_COMMAND ):
        response = "Sure...write some more code then I can do that!"

    else:
        response = answer( command )

    # Sends the response back to the channel
    return response or default_response


    
def run( handle_command ):
    global slack_client, starterbot_id
    if slack_client.rtm_connect(with_team_state=False):
        print("B.A.R.I.C.A. Slack Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call( "auth.test" )[ "user_id" ]
        while True:
            command, channel = parse_bot_commands( slack_client.rtm_read() )
            if command:
                response = handle_command( command, channel )
                slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text=response
                )
            time.sleep( RTM_READ_DELAY )
    else:
        print( "Connection failed. Exception traceback printed above." )

if __name__ == '__main__':
    if token:
        run( handle_command )
    else:
        print( "Exiting ..." )
