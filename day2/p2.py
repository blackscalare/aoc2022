with open('input.txt') as f:
    lines = f.readlines()

OPP_ROCK = 'A'
OPP_PAPER = 'B'
OPP_SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

rules = {
    OPP_ROCK: {
        LOSE: 3 + 0,
        DRAW: 1 + 3,
        WIN: 2 + 6
        },
    OPP_PAPER: {
        LOSE: 1 + 0,
        DRAW: 2 + 3,
        WIN: 3 + 6
    },
    OPP_SCISSORS: {
        LOSE: 2 + 0,
        DRAW: 3 + 3,
        WIN: 1 + 6
    }
}

def get_outcome_score(ch, opp):
    return rules.get(opp).get(ch)
    
p_score = 0
for line in lines:
    line = line.rstrip()
    l = line.split(' ')

    opp = l[0]
    player = l[1]

    p_score += get_outcome_score(player, opp)

print(p_score)