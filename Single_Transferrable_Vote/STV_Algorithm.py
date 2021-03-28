from voterGenerationAlgorithm import *
from District import *

#Takes: A list of District objects, each of which contains: a list of candidates, a list of Voter objects,
# and the number of representatives to be elected from the District in question.
# Voter objects each contain that voter's 1st, 2nd, and 3rd choices.

#Returns: A list of districts <outDistrict>, each of which 

class outDistrict:
    def __init__(self, name, winners):
        self.name = name #the name of the district
        self.winners = winners #a list of the winning candidates from that district

def STV_Algorithm(districts): #returns a list of outDistrict objects!
    #Create a list of districts
    #For each district:
        #Resolve that district individually and add the result to the list
    #Return the completed list
    
    #TEST
    outlist = []
    for dist in districts:
        outlist.append(resolve_district(dist))
    return outlist


def resolve_district(d): #Returns an outDistrict object! 
    #Resolve the district d by doing the following steps:
    #First, count all the first place votes. Each District contains Voters which contain a first, second, and third choice.
    #determine the vote threshold by dividing the total number of voters by the repsToElect number of the District.
    #For each Voter in the district, add a vote to that voter's first choice candidate (keep track using a dictionary) UNLESS:
        #Their first choice candidate already has reached the threshold, in which case you transfer to their second choice,
        # or third choice, and so on.
    #[LOOP] Check if all seats have been filled, now that each Voter's vote has been assigned to one candidate. 
        #If they have, return the district.
        #If they have not, eliminate the last place candidate from the running. For each Voter in that Candidate's voters list, transfer that voter to 
        #Their next choice candidate's pool instead (assuming taht candidate hasn't already won a seat).
    
    voteThreshold = length(d.voters) / repsToElect
    for c in d.candidates:
        c.votesNeeded = voteThreshold #set that candidate's votesNeeded to the vote threshold.

    #Count all the first-place votes
    for voter in d.voters:
        voter.resolveVote()

    # [LOOP UNTIL EVERY CANDIDATE HAS WON A SEAT AND WE END UP RETURNING OUTDISTRICT] Check if all seats have been filled, now that each voter's vote has been assigned to one candidate.
        #If they have, return the outDistrict as a list of winning candidates.

        #If they have not, sort d.candidates by the votesGained. Then eliminate the last place candidate from the running and,
        # for each Voter in that candidate's Voters list, increment choice by 1 and resolveVoter again
    out = outDistrict(d.name, [])
    while True:
        for can in d.candidates:
            if (length(can.voters) > can.votesNeeded) and (can not in out.winners):
                out.winners.append(can)

        if length(out.winners) == repsToElect:
            return out #end function!
        #Sort d.candidates by votesGained
        d.candidates.sort(key=lambda x: x.count, reverse=True)
        dropout = d.candidates[length(d.candidates-1)]
        d.candidates.remove(dropout)
        for v in dropout.voters:
            v.choice += 1
            v.resolveVote()

        #Just as a failsafe:
        if length(d.candidates) == repsToElect:
            out.winners = d.candidates