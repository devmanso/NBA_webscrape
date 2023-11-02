import NBA

urls : list[str] = [
    "https://www.nba.com/stats/player/1628368",
    "https://www.nba.com/stats/player/203954",
    "https://www.nba.com/stats/player/203076",
    "https://www.nba.com/stats/player/203999",
    "https://www.nba.com/stats/player/2544",
    "https://www.nba.com/stats/player/203507",
    "https://www.nba.com/stats/player/202691",
    "https://www.nba.com/stats/player/1627736",
    "https://www.nba.com/stats/player/203992",
    "https://www.nba.com/stats/player/1630178"
]

for url in urls:
    ppg: float = NBA.scrape_player_details(url, "APG")
    print(f"points per game {ppg}")

