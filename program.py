# Challenge:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def modulo(x):
    i = 1
    print(x)
    while i < 20:
        if (x % i) != 0:
            print("again")
        else:
            i += 1

    print("Done")

modulo(1)



users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9),
               ]

# print (users[9])
# print (friendships[3])

for user in users:
    user["friends"] = []
    # print(user)

for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j])  # add i as a friend of j
    users[j]["friends"].append(users[i])  # add j as a friend of i


def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)  # 24

num_users = len(users)
print("Number of users is {0}", (num_users))
avg_connections = total_connections / num_users

print(avg_connections)
# print(total_connections)

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

testvar = sorted(num_friends_by_id,                             # get it sorted
       key = lambda num_friends_by_id : num_friends_by_id[1],   # by num_friends
       reverse=True)                                            # largest to smallest

def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]     # for each of user's friends
            for foaf in friend["friends"]]    # get each of _their_ friends

print(friends_of_friend_ids_bad(users[0]))


# print(testvar)

# sum = lambda x, y : x + y
# print (sum(3,4))