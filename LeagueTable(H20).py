'''
The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function. 

The player's rank in the league is calculated using the following logic:

The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
If two players are tied on score, then the player who has played the fewest games is ranked higher.
If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.
Implement the player_rank function that returns the player at the given rank.

For example:
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))

All players have the same score.
However, Arnold and Chris have played fewer games than Mike,
and as Chris is before Arnold in the list of players, he is ranked first.
Therefore, the code above should display "Chris".

'''
from collections import Counter
from collections import OrderedDict  #remembers the order entries were added

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        #create a new dictionary for players' ranks and names
        players_rank={}
        i=1
        #recognise initial names order of player list
        for name in self.standings:
            players_rank[i]=name
            i=i+1

        for name in self.standings:
            for j in players_rank:
                if(j<len(players_rank)):
                    #check if score is higher --> ranked higher
                    if self.standings[players_rank[j+1]]['score'] > self.standings[players_rank[j]]['score']:
                        #lower score assigned to a lower rank
                        lower=players_rank[j]
                        players_rank[j]=players_rank[j+1]
                        players_rank[j+1]=lower
                    #check if score two players have the same score
                    elif self.standings[players_rank[j+1]]['score'] == self.standings[players_rank[j]]['score']:
                        # who played fewer games ranked higher
                        if self.standings[players_rank[j]]['games_played'] > self.standings[players_rank[j+1]]['games_played']:
                            #assign more games player to a lower rank 
                            lower=players_rank[j]
                            players_rank[j]=players_rank[j+1]
                            players_rank[j+1]=lower

        return players_rank[rank]  

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
