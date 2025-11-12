# Create a class Player with team = "India".
# Create an object p1, then set p1.team = "Australia".
# Print p1.team and Player.team.
# Delete p1.team using del and print again.

class Player:
    team = "India"

p1 = Player()
p1.team = "Australia"
print(p1.team)
print(Player.team)

del p1.team

print(p1.team)