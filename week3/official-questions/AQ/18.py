# You are given the results of a sequence of matches played by India in ODIs. A win is represented by 'W' and a loss is represented by 'L'. A winning streak is a string of consecutive wins. For example, if India has played five matches with the following results - 'WLWWWL' - then it has a three-match streak. Write a code to accept the result-sequence as input and find the longest streak in it.


s = input()
max_streak = 0
current_streak = 0
for result in s:
    if result == 'W':
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0
print(max_streak)



