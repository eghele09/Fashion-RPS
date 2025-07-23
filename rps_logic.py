import random

rps_moves = ["paper", "rock", "scissors"]

def simulate_decision():
    return random.choice(rps_moves), random.choice(rps_moves)

def check_rps_result(p1_move, p2_move):
    if p1_move == p2_move:
        return "tie"
    elif (p1_move == "rock" and p2_move == "scissors") or \
            (p1_move == "scissors" and p2_move == "paper") or \
            (p1_move == "paper" and p2_move == "rock"):
        return "player1"
    else:
        return "player2"

def play_best_of_three(option1, option2):
    p1_score = 0
    p2_score = 0
    round_num = 1
    results = []

    while p1_score < 2 and p2_score < 2:
        p1_move, p2_move = simulate_decision()
        winner = check_rps_result(p1_move, p2_move)
        results.append({
            "round": round_num,
            "option1_move": p1_move,
            "option2_move": p2_move,
            "winner": winner
        })

        if winner == "player1":
            p1_score += 1
        elif winner == "player2":
            p2_score += 1

        round_num += 1

    final_winner = option1 if p1_score > p2_score else option2
    return {
        "option1": option1,
        "option2": option2,
        "rounds": results,
        "final_winner": final_winner
    }
