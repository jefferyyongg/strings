# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scored_0 = "Ruud Gullit"
goal_0 = 32

scored_1 = "Marco van Basten"
goal_1 = 54

scorers = scored_0 + " " + str(goal_0) + ", " + scored_1 + " " + str(goal_1)

report = f'{scored_0} scored in the {goal_0}nd minute\n{scored_1} scored in the {goal_1}th minute'

player = "Lionel Messi"

first_name = player[:(player.find(" "))]
first_name_len = len(first_name)

last_name = player[player.find(" ") + 1:]
last_name_len = len(last_name)

name_short = f'{first_name[0]}. {last_name}'

chant = f"{first_name}! " * (first_name_len)

chant = chant[:-1]

good_chant = chant[-1] != " "
