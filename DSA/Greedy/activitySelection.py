'''
Given N number of activities with their start and end times. We need to select the maximum number of activities
that can be performed by a single person, assuming that a person can only work on a single activity at a time
'''

activities = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9]
]

def printMaxActivites(activities):
    # sort the activities array base on their finish time
    activities.sort(key=lambda x: x[2])
    i = 0
    # pick first activity and print it to start
    firstA = activities[i][0]
    print(firstA)
    # traverse through the array
    for j in range(len(activities)):
        # if the start of current activity is greater than end of previous activity
        if activities[j][1] > activities[i][2]:
            # then print the activity
            print(activities[j][0])
            # after that set the current activity to previous activity
            i = j

printMaxActivites(activities)