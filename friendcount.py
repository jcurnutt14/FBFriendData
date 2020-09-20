#Program Name: Friendship Paradox
#Author: Jon Curnutt
#Date: 10/15/19

import networkx as nx
G = nx.read_graphml('FrankMcCown-Facebook.graphml')

#Determine number of friends
my_friends = len(G.nodes)
print(f'Total Friends: {my_friends}')

#Determine the average number of friends each friend has
friends_of_friends_total = 0
for friend in G.nodes:
 # Make sure node has friend_count attribute
    if ('friend_count' in G.node[friend]):
        friends_of_friends_total += G.node[friend]['friend_count']

#Calculate average
friends_of_friends_avg = friends_of_friends_total / my_friends
print('Average friend count: ' + "{:.1f}".format(friends_of_friends_avg))

#Determine how many friends have more friends than Dr. McCown
more_friends = 0
for friend in G.nodes:
    if ('friend_count' in G.node[friend]):
        if G.node[friend]['friend_count'] > my_friends:
            more_friends += 1

#Determine percentage
more_friends_percentage = (more_friends / my_friends) * 100
print(f'How many have more friends: {more_friends} ({"{:.1f}".format(more_friends_percentage)}%)')

#Determine which friend has the most friends
most_friends_name = " "
most_friends = 0
for friend in G.nodes:
    if ('friend_count' in G.node[friend]):
        if G.node[friend]['friend_count'] > most_friends:
            most_friends = G.node[friend]['friend_count']
            most_friends_name = G.node[friend]['name']

print(f'Most friends: {most_friends_name} ({most_friends})')

#Determine the friend with the greatest number of mutual friends
friend_name = " "
friend_mutual_friends = 0
for friend in G.nodes:
    if ('friend_count' in G.node[friend]):
        if len(G.edges(friend)) > friend_mutual_friends:
            friend_name = G.node[friend]['name']
            friend_mutual_friends = len(G.edges(friend))

print(f'Most friends in common: {friend_name} ({friend_mutual_friends})') 

#Determine if friendship paradox is true or false
if friends_of_friends_avg > my_friends:
    print('Friendship paradox: YES')
else:
    print('Friendship paradox: NO')