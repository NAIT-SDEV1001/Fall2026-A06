fav_fruit_voters = {
    "daniel": "apple",
    "jessica": "apple",
    "michael": "banana",
    "john": "banana",
    "jessie": "apple",
    "jim": "orange",
    "jenny": "apple",
    "jason": "orange",
    "joseph": "banana",
    "james": "orange",
    "mary": "apple",
    "melody": "banana",
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}

print("Voters:")
for voter in fav_fruit_voters.keys():
    print(f"- {voter}")


# for vote in fav_fruit_voters.values():
#     if vote == "banana":
#         voting_results["banana"] += 1
#     elif vote == "apple":
#         voting_results["apple"] += 1
#     elif voting_results == "orange":
#         voting_results["orange"] += 1

# print(voting_results)

for vote in fav_fruit_voters.values():
    voting_results[vote] += 1

print(voting_results)

total_votes = 0
for count in voting_results.values():
    total_votes += count

print(f"Total votes: {total_votes}")

for fruit, vote_count in voting_results.items():
    print(f"Fruit: {fruit}: {vote_count}")


for fruit, votes in sorted(voting_results.items()):
    print(f"{fruit}: {votes}")


while True:
    vote = input("Vote for your favorite fruit:")

    if vote == "":
        break

    if vote == "q" or vote == "quit":
        break

    if vote in voting_results:
        voting_results[vote] = voting_results[vote] + 1 # one or more votes already
        #voting_results[vote] += 1 # or this way
    else:
        voting_results[vote] = 1 # firsts vote

print(voting_results)