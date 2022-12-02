with open('input.txt') as f:
    lines = f.readlines()

OPP_ROCK = 'A'
OPP_PAPER = 'B'
OPP_SCISSORS = 'C'

P_ROCK = 'X'
P_PAPER = 'Y'
P_SCISSORS = 'Z'

choice_score = {
    P_ROCK: 1,
    P_PAPER: 2,
    P_SCISSORS: 3
}

rules = {
    P_ROCK: {
        OPP_ROCK: 3,
        OPP_PAPER: 0,
        OPP_SCISSORS: 6
        },
    P_PAPER: {
        OPP_ROCK: 6,
        OPP_PAPER: 3,
        OPP_SCISSORS: 0
    },
    P_SCISSORS: {
        OPP_ROCK: 0,
        OPP_PAPER: 6,
        OPP_SCISSORS: 3
    }
}

def get_choice_score(ch):
    return choice_score.get(ch)

def get_outcome_score(ch, opp):
    return rules.get(ch).get(opp)

p_score = 0

for line in lines:
    line = line.rstrip()
    l = line.split(' ')

    opp = l[0]
    player = l[1]

    p_score += get_choice_score(player)
    p_score += get_outcome_score(player, opp)

print(p_score)