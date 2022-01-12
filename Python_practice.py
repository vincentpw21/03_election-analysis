# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election?"))

# # Total votes in the election.
# total_votes = int(input("What is the total number of votes in the election?"))

# # Calculate the percentage of votes you recieved.
# perecentage_votes = (my_votes/total_votes) * 100
# print("I recieved " + str(perecentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso are in the list of counties.")
# else:
#     print("Arapahoe and El Paso is not in the list of counties.")

for county in counties.keys():
    print(county)