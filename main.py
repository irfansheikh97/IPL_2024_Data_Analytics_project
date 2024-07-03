from all_imports import json
from get_match_data import scrape_batting_match_data, scrape_bowling_match_data, scrape_players_info
from cricket_data_methods import extract_links, scrape_players_links

# all_matches_data = []
match_links = extract_links(
    "https://www.espncricinfo.com/records/tournament/team-match-results/indian-premier-league-2024-15940")

# # code for batting data of all matches - start
# for match_link in match_links:
#     match_bat_data = scrape_batting_match_data(match_link)
#     all_matches_data.append({"battingSummary": match_bat_data})

# # Print the JSON data
# batting_data = json.dumps(all_matches_data, indent=4)

# # Writing batting data of all matches into JSON file
# with open("ipl_2024_batting_summary_data.json", 'w') as file:
#     print("Writing data in json file.....")
#     file.write(batting_data)
#     print("Done")
# # batting code ends here

# # code for bowling data of all matches - start
# for match_link in match_links:
#     match_bowl_data = scrape_bowling_match_data(match_link)
#     all_matches_data.append({"bowlingSummary": match_bowl_data})

# # Print the JSON data
# bowling_data = json.dumps(all_matches_data, indent=4)

# # Writing bowling data of all matches into JSON file
# with open("ipl_2024_bowling_summary_data.json", 'w') as file:
#     print("Writing data in json file.....")
#     file.write(bowling_data)
#     print("Done")
# # bowling code ends here

# # Players info data code -- start
# # getting all players team and links from all matches
# all_players_links = []
# for match_link in match_links:
#     players_links = scrape_players_links(match_link)
#     for player_obj in players_links:
#         if player_obj not in all_players_links:
#             all_players_links.append(player_obj)
#
# # getting players data from above lines of code and converting into json form
# players_data = json.dumps(scrape_players_info(all_players_links), indent=4)
#
# # Writing players info data of all matches into JSON file
# with open("dummy-json-files/ipl2024_players_info.json", 'w') as file:
#     print("Writing data in json file.....")
#     file.write(players_data)
#     print("Done")
# # players info code ends here
