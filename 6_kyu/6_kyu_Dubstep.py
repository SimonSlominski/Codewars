""" All tasks come from www.codewars.com """

"""
TASK: Dubstep

Input
The input consists of a single non-empty string, consisting only of uppercase English letters, 
the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
=>  WE ARE THE CHAMPIONS MY FRIEND
"""


import re

def song_decoder(song):
    words_in_song = re.sub(' +', ' ', song.replace('WUB', ' '))
    return words_in_song.lstrip().rstrip()

