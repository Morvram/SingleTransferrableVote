class District:
    #candidates = [] a list of Candidates
    #voters = [] a list of Voter objects
    #repsToElect = 0
    #name = the name of the district

    def init(self, repsToElect, candidates, voters, name):
        self.repsToElect = repsToElect
        self.candidates = candidates
        self.voters = voters
        self.name = name

class Voter:
    choice = 0 #The current index in their list of choices.

    def init(self, votes):
        self.votes = votes #A list of Candidates ordered by preference


class Candidate:
    votesGained = 0
    votesNeeded = 0
    voters = [] #A list of the voters who voted for that candidate

    def init(self, name):
        self.name = name