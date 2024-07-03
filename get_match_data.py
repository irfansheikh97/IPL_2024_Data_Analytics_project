from all_imports import requests, BeautifulSoup
from cricket_data_methods import scrape_batting_data, scrape_bowling_data


def scrape_batting_match_data(url: str) -> list[dict]:
    match_batting_data = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        teams = soup.find_all('div', class_='ds-rounded-lg ds-mt-2')

        if not teams:
            return []  # No results for this match

        team1 = teams[0].find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()
        team2 = teams[1].find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()

        for team in teams:
            team_name = team.find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()
            team_innings = team.find('table', class_='ci-scorecard-table')
            batting_rows = team_innings.find_all('tr')

            batting_data = scrape_batting_data(batting_rows, team1, team2, team_name)
            match_batting_data.extend(batting_data)

    return match_batting_data


def scrape_bowling_match_data(url: str) -> list[dict]:
    match_bowling_data = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        teams = soup.find_all('div', class_='ds-rounded-lg ds-mt-2')

        if not teams:
            return []  # No results for this match

        team1 = teams[0].find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()
        team2 = teams[1].find('span', class_='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()

        team_innings = soup.find_all('table', class_='ds-w-full ds-table ds-table-md ds-table-auto')
        firstInningRows = team_innings[0].find_all('tr')
        first_innings_bowling_data = scrape_bowling_data(firstInningRows, team1, team2, team2)
        match_bowling_data.extend(first_innings_bowling_data)

        secondInningRows = team_innings[1].find_all('tr')
        second_innings_bowling_data = scrape_bowling_data(secondInningRows, team1, team2, team1)
        match_bowling_data.extend(second_innings_bowling_data)

    return match_bowling_data


def scrape_players_info(players_data: list[dict]):
    players_info_data: list[dict] = []

    for player in players_data:
        response = requests.get(player.get('url'))
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            texts_to_compare = ["batting style", "bowling style", "playing role"]
            batting_style = ""
            bowling_style = ""
            playing_role = ""

            p_tags = soup.find_all('p', class_='ds-text-tight-m ds-font-regular ds-uppercase ds-text-typo-mid3')
            for p_tag in p_tags:
                p_text = p_tag.text.strip()
                if p_text.lower() in texts_to_compare:
                    next_element_text = p_tag.find_next().text.strip()
                    if p_text.lower() == "batting style":
                        batting_style = next_element_text
                    elif p_text.lower() == "bowling style":
                        bowling_style = next_element_text
                    elif p_text.lower() == "playing role":
                        playing_role = next_element_text

            if soup.find('div', class_='ci-player-bio-content'):
                description = soup.find('div', class_='ci-player-bio-content').text.strip()
            else:
                description = ""

            # players image url
            if soup.find('div', class_='ds-ml-auto ds-w-48 ds-h-48').find('img'):
                image_class = soup.find('div', class_='ds-ml-auto ds-w-48 ds-h-48').find('img')
                image_url = image_class['src']
            else:
                image_url = ""

            player_obj = {"name": player.get('name'), "image": image_url, "team": player.get('team'), "battingStyle": batting_style, "bowlingStyle": bowling_style, "playingRole": playing_role, "description": description}
            players_info_data.append(player_obj)

    return players_info_data


