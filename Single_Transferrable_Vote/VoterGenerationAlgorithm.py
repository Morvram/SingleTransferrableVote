#Joshua Mandell

from District import *


def voterGenerationAlgorithm(districts, numVoters, candidatesPerDistrict, choiceVotesForCandidates): # first draft


    #districts = a list (1d) of district names
    #numVoters = a list (1d) of the number of voters in each district.
    #candidatesPerDistrict = a list (2d) of lists of candidates, of equal length.
    #choiceVotesForCandidate = a list (3d):
        #1st layer: one list corresponding to each district.
        #2nd layer one list corresponding to each candidate in that district.
        #3rd layer number of votes at first, second, third etc. choice.

    #For each district, create the district object using:
    i = 0
    while i < len(districts):
        name = districts[i]
        #1) The relevant name,

        #2) The candidate names in that district, (initialize the Candidates as objects)
        canNames = candidatesPerDistrict[i]
        candidates = []
        for c in canNames:
            candidates.append(Candidate(c))

        repsToElect = len(choiceVotesForCandidates[i][0])

        #3) OK this one's more complicated:
            #(1) Create a list voters[] of Voter objects of length equal to the total number of first-choice votes that exist in the district,
            # with empty lists as their contents


            # (2) For each Voter in that list, append a first choice candidate. If the first candidate has 754 first-choice votes,
            # the first 754
            #Voter objects will have that candidate inserted as their first choice.
                # An aside on this: basically, we'll be setting the first choice of the Voter in the i spot of the list of voters,
                # while i < choiceVotesForCandidate[currentDistrict][i][0].
                # 0 in this case should be the initial value for j, which corresponds to choice number -1.
                #Voter.votes[j] = candidatesPerDistrict[currentDistrict][k]
                #Where k is the index of the candidate we're currently on (i will have to reset each time we increment k)

                #YEAH OKAY THIS IS COMPLICATED BUT INTERESTING.

            #Do the same for second choice, third choice, etc etc until the end

        #1
        voters = []
        for n in range(0, numVoters[i]):
            voters.append(Voter([])) #voters[n] = Voter([])
        # follow above todo (2) - 
        for n in range(0, len(choiceVotesForCandidates[i][0])):

            k = 0 #Candidate index in the candidates[] list
            j = 0 #Voter index in the voters[] list
            ij = 0 #counter up to number of first-choice votes for that candidate.
            while j < len(voters):
                if ij < choiceVotesForCandidates[i][k][0]: #i represents current district, k represents candidate index in candidates[] list
                    ij += 1
                    voters[j].votes.append(candidates[k])
                    j += 1
                else: #switch to the next candidate
                    ij = 0 #reset this because ij is what counts up to the number of first-choice voters for that candidate.
                    k += 1
                #We will eventually run out of voters (j will reach len(voterS))




        # repsToElect = the number of representatives that the district in question is electing.
            # determine how we will decide how many representatives will be elected in a district!
        #note above, line 27: repsToElect = len(choiceVotesForCandidates[currentDistrict][0])
            # the number of candidates to elect from a district should be equal to the number of choices each voter may cast in that election.
            # if there are going to be three candidates elected in a particular district race, each voter should choose a first, second, and third choice candidate.
        
        #Then initialize the District object to the current slot in the districts[] list
        districts[i] = District(repsToElect, candidates, voters, name)
        i += 1

    #You should now have a list of Districts, each of which has Candidates (whose Voter pools are not yet filled)
    #and Voters (with their choices determined) within.
    
    return districts