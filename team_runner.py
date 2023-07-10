from team import *

players = ["Andy Murray", " Leo Messi", " Jonah Lomu", " Michael Phelps"]

team = Team ("All stars", players, "Arsene Wenger")

print(team.has_player("Andy Murray")) 

print (team.has_player("Thierry Henry"))

team.add_player(" Zlatan Ibrahimovic") 

print (players)

team.play_game(True)
print (team.points)

team.play_game(False)
print (team.points)

team.play_game(True)
print (team.points)
