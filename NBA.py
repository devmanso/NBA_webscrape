import requests
import re


def scrape_player_details(playerurl: str, stat: str):
    try:
        response = requests.get(playerurl)
        response.raise_for_status()  # Check for HTTP errors
        html = response.text

        start_index = html.find(stat) + len(stat)
        end_index = html.find("</div>", start_index)
        statsinfo = html[start_index:end_index]

        detail = re.findall("\d+\.\d+", statsinfo)  # Use "\d+" for integers
        return float(detail[0]) if detail else None
        except requests.RequestException as e:
        print(f"scrape_player_details request error : {e}")
    return None
