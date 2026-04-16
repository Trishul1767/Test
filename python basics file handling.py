player_name, score = input("Enter player name and score: ").split()

try:
    with open("highscores.txt", "r") as file:
        # Read existing scores into a list of tuples
        scores = [line.strip().split() for line in file.readlines()]
except FileNotFoundError:
    scores = [] # If file doesn't exist yet
    
scores.append([player_name, str(score)])
# Sort by score (index 1) in descending order
scores.sort(key=lambda x: int(x[1]), reverse=True)

# Keep only top 5
top_5 = scores[:5]

with open("highscores.txt", "w") as file:
    for s in top_5:
        file.write(f"{s[0]} {s[1]}\n")
        
print("Top 5 high scores updated")