from District import *


def voterGenerationAlgorithm(districts, candidatesPerDistrict, choiceVotesForCandidate):
    #districts = a list (1d) of districts
    #candidatesPerDistrict = a list (2d) of lists of candidates, of equal length.
    #choiceVotesForCandidate = a list (3d):
        #1st layer Districts
        #2nd layer Candidates
        #3rd layer number of votes at first, second, third etc. choice.

    #For each district, create the district object using:
        #1) The relevant name,
        #2) The candidate names in that district, (initialize the Candidates as objects)
        #3) OK this one's more complicated:
            #Create a list of Voter objects of length equal to the total number of first-choice votes that exist in the district, with empty lists as their contents
            #For each Voter in that list, append a first choice candidate. If the first candidate has 754 first-choice votes, the first 754
            #Voter objects will have that candidate inserted as their first choice.
            #Do the same for second choice, third choice, etc etc until the end
    #You should now have a list of Districts, each of which has Candidates (whose Voter pools are not yet filled)
    #and Voters (with their choices determined) within.

    #TODO

