from District import *


def voterGenerationAlgorithm(districts, numVoters, candidatesPerDistrict, choiceVotesForCandidate): #TODO


    #districts = a list (1d) of districts
    #numVoters = a list (1d) of the number of voters in each district.
    #candidatesPerDistrict = a list (2d) of lists of candidates, of equal length.
    #choiceVotesForCandidate = a list (3d):
        #1st layer Districts
        #2nd layer Candidates
        #3rd layer number of votes at first, second, third etc. choice.

    #For each district, create the district object using:
    i = 0
    while i < length(districts):
        name = districts[i]
        #1) The relevant name,

        #2) The candidate names in that district, (initialize the Candidates as objects)
        canNames = candidatesPerDistrict[i]
        candidates = []
        for c in canNames:
            candidates.append(Candidate(c))

        #3) OK this one's more complicated:
            #Create a list voters[] of Voter objects of length equal to the total number of first-choice votes that exist in the district,
            # with empty lists as their contents


            #TODO For each Voter in that list, append a first choice candidate. If the first candidate has 754 first-choice votes,
            # the first 754
            #Voter objects will have that candidate inserted as their first choice.
                # An aside on this: basically, we'll be setting the first choice of the Voter in the i spot of the list of voters,
                # while i < choiceVotesForCandidate[currentDistrict][i][0].
                # 0 in this case should be the initial value for j, which corresponds to choice number -1.
                #Voter.votes[j] = candidatesPerDistrict[currentDistrict][k]
                #Where k is the index of the candidate we're currently on (i will have to reset each time we increment k)

                #YEAH OKAY THIS IS COMPLICATED BUT INTERESTING.

            #Do the same for second choice, third choice, etc etc until the end
        voters = []
        for n in range(:numVoters[i]):
            voters[n] = Voter([])
        #TODO follow above todo


        #TODO repsToElect = the number of representatives that the district in question is electing.
            #TODO determine how we will decide how many representatives will be elected in a district!
        
        #Then initialize the District object to the current slot in the districts[] list
        districts[i] = District(repsToElect, candidates, voters, name)
        i += 1

    #You should now have a list of Districts, each of which has Candidates (whose Voter pools are not yet filled)
    #and Voters (with their choices determined) within.
    
    return districts