from pprint import pprint
import lichess
import lichess.api
import lichess.format

# GUI
import tkinter

# liste mit allen figuren
# figur: { posx, posy, type }

# T S L D K L S T
# B B B B B B B B
# ...............
# B B B B B B B B
# T S L D K L S T

def neues_feld():
    figuren = []
    
    for i_ in 1, 6:
        for i in range(0, 8):
            figuren.append({'posx': i, 'posy': i_, 'type': 'pawn'})

    for i in 0, 7:
        figuren.append({'posx': i, 'posy': 0, 'type': 'tower'})
        figuren.append({'posx': i, 'posy': 7, 'type': 'tower'})
        
    for i in 1, 6:
        figuren.append({'posx': i, 'posy': 0, 'type': 'knight'})
        figuren.append({'posx': i, 'posy': 7, 'type': 'knight'})

    for i in 2, 5:
        figuren.append({'posx': i, 'posy': 0, 'type': 'bishop'})
        figuren.append({'posx': i, 'posy': 7, 'type': 'bishop'})
        
    for i in 0, 7:
        figuren.append({'posx': 3, 'posy': i, 'type': 'queen'})
        
    for i in 0, 7:
        figuren.append({'posx': 4, 'posy': i, 'type': 'king'})
        

    


    return figuren

# config.py
import config
lichess.api.login(config.USERNAME, config.PASSWORD)

def lichess_stream_events(**kwargs):
    return lichess.api._api_get(
        '/api/stream/event', kwargs, object_type=lichess.format.STREAM_OBJECT)

def accept_challenge(user=None):
    events = lichess_stream_events()
    for event in events:
        pass

pprint(neues_feld())
