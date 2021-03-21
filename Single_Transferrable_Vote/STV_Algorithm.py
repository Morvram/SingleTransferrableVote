from voterGenerationAlgorithm import *

#Takes: A list of District objects, each of which contains: a list of candidates, a list of Voter objects,
# and the number of representatives to be elected from the District in question.
# Voter objects each contain that voter's 1st, 2nd, and 3rd choices.

#Returns: A list of districts <outDistrict>, each of which 

class outDistrict:
    def init(self, name, winners):
        self.name = name #the name of the district
        self.winners = winners #a list of the winning candidates from that district

def STV_Algorithm(districts): #returns a list of outDistrict objects!
    #Create a list of districts
    #For each district:
        #Resolve that district individually and add the result to the list
    #Return the completed list
    
    #TODO


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

    #TODO
    