""" All tasks come from www.codewars.com """

"""
TASK: Find the Word Pair!

Given an array of words and a target compound word, your objective is to find the two words which combine into 
the target word, returning both words in the order they appear in the array, and their respective indices in 
the order they combine to form the target word. 

Words in the array you are given may repeat, but there will only be one unique pair that makes the target compound word. 
If there is no match found, return null/nil/None.

Note: Some arrays will be very long and may include duplicates, so keep an eye on efficiency.

Examples:

fn(['super','bow','bowl','tar','get','book','let'], "superbowl")      =>   ['super','bowl',   [0,2]]
fn(['bow','crystal','organic','ally','rain','line'], "crystalline")   =>   ['crystal','line', [1,5]]
fn(['bow','crystal','organic','ally','rain','line'], "rainbow")       =>   ['bow','rain',     [4,0]]
fn(['bow','crystal','organic','ally','rain','line'], "organically")   =>   ['organic','ally', [2,3]]
fn(['top','main','tree','ally','fin','line'], "mainline")             =>   ['main','line',    [1,5]]
fn(['top','main','tree','ally','fin','line'], "treetop")              =>   ['top','tree',     [2,0]]
"""


def compound_match(words, target):

    # list of words that correspond to the beginning of word 'target'
    starting_words = [word for word in set(words) if target.startswith(word)]
    # list of words that correspond to the ending of word 'target'
    ending_words = [word for word in set(words) if target.endswith(word)]

    # verify that both words are identical to the word target
    for start_word in starting_words:
        for end_word in ending_words:
            if start_word + end_word == target:
                # set indexes to the first and second word
                starting_word_index = words.index(start_word)
                ending_word_index = words.index(end_word)
                # set the order of returning words (must be the same order they appear in the array)
                # ending_word_index < starting_word_index == end_word appears before start_word in the 'words' array
                if ending_word_index < starting_word_index:
                    return [end_word, start_word, [starting_word_index, ending_word_index]]
                return [start_word, end_word, [starting_word_index, ending_word_index]]

