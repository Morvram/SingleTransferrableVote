#Joshua Mandell
#TODO create test inputs for the voterGenerationAlgorithm so I can test its program-breaking flaws.

from STV_Algorithm import *
from VoterGenerationAlgorithm import *
from District import *


 #districts = a list (1d) of district names
    #numVoters = a list (1d) of the number of voters in each district.
    #candidatesPerDistrict = a list (2d) of lists of candidates, of equal length.
    #choiceVotesForCandidate = a list (3d):
        #1st layer: one list corresponding to each district.
        #2nd layer one list corresponding to each candidate in that district.
        #3rd layer number of votes at first, second, third etc. choice.

districts = ["District 1", "District 2", "District 3"]
numVoters = [100, 100, 100]
candidatesPerDistrict = [
    ["Josh", "George", "Bob"],
    ["Alice", "Samantha", "Georgia"],
    ["Emily", "John", "Tris"]
]
choiceVotesForCandidate = [
    [ #district 1
        [50, 20], #Josh
        [20, 70], #George #NOTE how the 1st-choice voices add up to 100 (the number of voters), and so do the second-
        [30, 10] #Bob #and third-choice votes.
    ],
    [ #district 2
        [50, 20], #Alice
        [20, 70], #Samantha
        [30, 10] #Georgia
    ],
    [ #district 3
        [50, 20], #Emily
        [20, 70], #John
        [30, 10] #Tris
    ]
]

outlist = STV_Algorithm(voterGenerationAlgorithm(districts, numVoters, candidatesPerDistrict, choiceVotesForCandidate))

print(outlist)
for o in outlist:
    print(o.name + " winners:")
    count = 1
    for c in o.winners:
        print("Place " + str(count) + ": " + c.name)
        count += 1