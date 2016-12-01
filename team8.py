####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
team_name = 'T8' # Only 10 chars displayed.
strategy_name = 'Double Crosser'
strategy_description = 'Betray if Nessescary'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # if they are on their first move, then collude.
    if not their_history:
        return 'c'

    # if this is either the last or second-to-last turn, defect
    elif len(their_history) > 196:
        return 'b'

    # if the opponent did not defect on any of the first six turns,
    # and we are not in the last 20 turns, cooperate
    elif 6 < len(their_history) < 180:
            if 'b' not in their_history[:7]:
                 return 'c'

    # if the total number of defections by the opponent is 
    # greater than three, always defect
    elif 'b' in their_history > 3:
        return 'b'

    # failsafe: if none of the other conditions are true
    
    return 'c'
