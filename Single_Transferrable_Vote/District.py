#Joshua Mandell

class District:
    #candidates = [] a list of Candidates
    #voters = [] a list of Voter objects
    #repsToElect = 0
    #name = the name of the district

    def __init__(self, repsToElect, candidates, voters, name):
        self.repsToElect = repsToElect
        self.candidates = candidates
        self.voters = voters
        self.name = name

class Voter:
    choice = 0 #The current index in their list of choices.

    def __init__(self, votes):
        self.votes = votes #A list of Candidates ordered by preference

    def resolveVote(self):
        #If your current choice doesn't have enough votes, keep that as your choice
        # and add self to that Candidate's list of voters.
        votes = self.votes
        choice = self.choice
        if len(votes[choice].voters) < votes[choice].votesNeeded and self not in votes[choice].voters:
            print("Index was not out of range")
            votes[choice].voters.append(self)
            return
        #If your current choice DOES have enough votes and you're not at the end of your list of choices,
        # increase choice by 1 and try again.
        else:
            self.choice += 1
            if self.choice >= len(self.votes):
                #print("Problem: Not enough choices were provided, and a voter exceeded their list of chosen candidates!")
                return #Something has gone wrong
            self.resolveVote() #the "try again" phase


class Candidate:
    def __init__(self, name):
        self.name = name
    #votesGained = 0 #don't need this var, use length(voters) instead
    votesNeeded = 0
    voters = [] #A list of the voters who voted for that candidate