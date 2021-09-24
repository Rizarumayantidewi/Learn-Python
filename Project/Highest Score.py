user_scores = [110, 800, 250, 100, 210, 200]
highest = user_scores[0]

for score in user_scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")