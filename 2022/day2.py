lines = []

choiceScores = {"X": 1, "Y": 2, "Z": 3}
outcomeScores = {"X": 0, "Y": 3, "Z": 6}
rpsScores = {"A": 1, "B": 2, "C": 3}
beats = {"A": "B", "B": "C", "C": "A"}
losesTo = {"A": "C", "B": "A", "C": "B"}
p1outcomes = {
	"A": {"X": 3, "Y": 6, "Z": 0},
	"B": {"X": 0, "Y": 3, "Z": 6},
	"C": {"X": 6, "Y": 0, "Z": 3}
}		

with open("day2input.txt") as f:
	lines = [l.strip().split(" ") for l in f.readlines()]

p1 = 0
p2 = 0
for l in lines:
	score = 0
	[theirs, mine] = l
	p1 = p1 + choiceScores[mine] + p1outcomes[theirs][mine]
	if mine == "Y": # draw
		score = outcomeScores[mine] + rpsScores[theirs]
	elif mine == "X": # lose
		score = outcomeScores[mine] + rpsScores[losesTo[theirs]]
	elif mine == "Z": #win
		score = outcomeScores[mine] + rpsScores[beats[theirs]]
	p2 = p2 + score



print(p1)
print(p2)