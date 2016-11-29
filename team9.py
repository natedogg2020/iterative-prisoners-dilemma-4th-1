####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Lauren&Carly' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'

def betrayed(their_history):
    '''Checks if we were betrayed'''
    
    thHis = their_history
    
    if thHis[-3:] == 'bbb':
        return True
    else: 
        return False
        
def colPerc(their_history):
    '''What percentage of their history is collusion'''
    
    thHis = their_history
    
    tot = len(thHis)
    colN = 0
    colP = 0.0
    for move in thHis:
        if move == 'c': 
            colN += 1
    colP = float(colN)/tot
    return colP
    
def betPerc(their_history):
    '''What percentage of their history is betrayal'''
    
    thHis = their_history
    
    tot = len(thHis)
    betN = 0
    betP = 0.0
    for move in thHis:
        if move == 'b': 
            betN += 1
    betP = betN/tot
    return betP
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    mHis = my_history
    thHis = their_history
    mScore = my_score
    thScore = their_score

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'. 
    
    if mHis == '':
        return 'c'
   
    if thHis[-3:] == 'bbb':
        return 'b'
    
    if colP >= 0.9 and thHis[-2:] == 'cc':
        return 'b'
    
    if betP >= 0.9 and thHis[-1] == 'b':
        return 'b'
    
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print type(real_result)
        print("move(" +", ".join(["'"+my_history+"'", "'"+their_history+"'",
            str(my_score), 
            str(their_score)])+") returned " + "'" + 
            real_result + "'" + " and should have returned '" + 
            result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
            print 'Test Passed'
    
     # Test 2: If betrayed 3 times, betray back
    if test_move(my_history='cbb', 
                their_history='bbb', 
                my_score=0, 
                their_score=0, 
                result='b'):
          print 'Test Passed'  
 
   # Test 3: If offered collusion twice after betrayal, collude
    if test_move(my_history='bbb', 
                their_history='bbbcccc',
                my_score=0,
                their_score=0,
                result='b'):
        print 'Test Passed'
    # Test 4: If they collude 90% of the time, betray them
    if test_move(my_history= 'ccc', 
                their_history= 'cccccccccb', 
                my_score=0,
                their_score=0,
                result='b'):
        print 'Test Passed'