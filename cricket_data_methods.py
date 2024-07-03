from all_imports import requests, BeautifulSoup


def extract_links(url: str) -> list[str]:
    """

    :rtype: list
    """
    match_links: list = []
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # You would need to inspect the HTML structure of the webpage to locate the specific data elements
        # Here is an example of how you might extract table data:

        table = soup.find('table', class_='ds-w-full')  # Replace 'your_table_class' with the actual class name
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')[6]
            for cell in cells:
                link = cell.find('a', href=True)
                if link:
                    match_links.append(f"https://www.espncricinfo.com" + link['href'])
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return match_links


def scrape_batting_data(batting_table: list, team1: str, team2: str, team_name: str,
                        tag: str = 'td') -> list[dict]:
    match_batting_data = []
    batting_position = 0
    for row in batting_table[1:]:
        cells = row.find_all(tag)
        if len(cells) > 6:
            batting_position += 1
            batsman_name = cells[0].text.strip()
            dismissal = cells[1].text.strip()
            runs = cells[2].text.strip()
            balls = cells[3].text.strip()
            fours = cells[5].text.strip()
            sixes = cells[6].text.strip()
            strike_rate = cells[7].text.strip()

            match_batting_data.append({
                "match": f"{team1} Vs {team2}",
                "teamInnings": team_name,
                "battingPos": batting_position,
                "batsmanName": batsman_name,
                "dismissal": dismissal,
                "runs": runs,
                "balls": balls,
                "4s": fours,
                "6s": sixes,
                "SR": strike_rate
            })

    return match_batting_data


def scrape_bowling_data(bowling_table: list, team1, team2, team_name, tag: str = 'td'):
    match_bowling_data: list[dict] = []
    for row in bowling_table[1:]:
        cells = row.find_all('td')
        if len(cells) > 6:
            bowlerName = cells[0].text.strip()
            overs = cells[1].text.strip()
            maiden = cells[2].text.strip()
            runs = cells[3].text.strip()
            wickets = cells[4].text.strip()
            economy = cells[5].text.strip()
            zero = cells[6].text.strip()
            fours = cells[7].text.strip()
            sixes = cells[8].text.strip()
            wides = cells[9].text.strip()
            noBalls = cells[10].text.strip()

            match_bowling_data.append({
                "match": f"{team1} Vs {team2}",
                "bowlingTeam": team_name,
                "bowlerName": bowlerName,
                "overs": overs,
                "maiden": maiden,
                "runs": runs,
                "wickets": wickets,
                "economy": economy,
                "0s": zero,
                "4s": fours,
                "6s": sixes,
                "wides": wides,
                "noBalls": noBalls
            })

    return match_bowling_data


def scrape_players_links(url: str) -> list[dict]:
    players_info_links: list[dict] = []

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        teams = soup.find_all('div', class_='ds-rounded-lg ds-mt-2')

        if not teams:
            return []  # No results for this match

        team1 = teams[0].find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()
        team2 = teams[1].find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()

        # from batting innings
        for team in teams:
            team_name = team.find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()
            team_innings = team.find('table', class_='ci-scorecard-table')
            player_links = team_innings.find_all('a', href=True)
            for link in player_links:
                player_name = link.find('span', class_='ds-text-tight-s').find('span').text.strip()
                player_link = f"https://www.espncricinfo.com" + link['href']
                player_batting_obj = {"name": player_name, "team": team_name, "url": player_link}
                if player_batting_obj not in players_info_links:
                    players_info_links.append(player_batting_obj)

        # from bowling innings solution
        team_innings = soup.find_all('table', class_='ds-w-full ds-table ds-table-md ds-table-auto')
        player_links_1 = team_innings[0].find_all('a', href=True)
        for link in player_links_1:
            player_bowling_obj_1 = bowl_players_data(link, team2)
            if player_bowling_obj_1 not in players_info_links and len(player_bowling_obj_1) != 0:
                players_info_links.append(player_bowling_obj_1)

        player_links_2 = team_innings[1].find_all('a', href=True)
        for link in player_links_2:
            player_bowling_obj_2 = bowl_players_data(link, team1)
            if player_bowling_obj_2 not in players_info_links and len(player_bowling_obj_2) != 0:
                players_info_links.append(player_bowling_obj_2)

    return players_info_links


def bowl_players_data(player_link: str, team_name: str) -> dict:
    if player_link['href'].startswith("/cricketers"):
        player_name = player_link.find('span').text.strip()
        player_link = f"https://www.espncricinfo.com" + player_link['href']
        player_obj = {"team": team_name, "url": player_link}
        return player_obj
    else:
        return {}
