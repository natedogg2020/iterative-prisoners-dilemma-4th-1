from __future__ import division 
import random

####
# Each team's file must define four tokens:
#     team_name: OG RD
#     strategy_name: Repeat good outcome
#     strategy_description: Repeat the last outcome if it was good
#     move: A function that returns 'c' or 'b'
####

team_name = 'OG RD' # Only 10 chars displayed.
strategy_name = 'Repeat good outcomes'
strategy_description = 'Repeats the outcome if good, otherwise choose a different outcome'
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. '''
    if len(their_history) > 0:
        percent_betray=float(their_history.count('b'))/float(len(their_history))*100 #gives the chance of the other playe betraying depending on how many betrays they have done
    
    if len(their_history) > 0: #This block of code repeats good outcomes
        if 'b' in my_history[-1] and 'c' in their_history[-1]:
            return 'b'
        elif 'c' in my_history[-1] and 'c' in their_history[-1]:
            return 'c'
        elif 'b' in my_history[-1] and 'b' in their_history[-1]:
            return 'b'
    
        else: #if none are good
            if percent_betray > 70: #betray if the opponents chance to bretray is greater than 70%
                return'b'
            else:
                if len(their_history) % 2 == 0: #betray on even rounds
                    return 'b'
                else:
                    return 'c'   #collude on odd rounds
                
    else:
        return 'c'#failsafe if something goes wrong, return collude
        


    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False
a
if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             