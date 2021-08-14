import requests
import config
 
HEADERS = {"Authorization": f"Bearer {config.API_KEY}"}

def get_projects():
    r = requests.get(
        "https://api.tokenterminal.com/v1/projects",
        headers=HEADERS
        )
    return r.json()


def get_historical(project_id, interval="daily", data_granularity="project"):
    r = requests.get(
        f"https://api.tokenterminal.com/v1/projects/{project_id}/metrics",
        params={"interval": interval, "data_granularity": data_granularity},
        headers=HEADERS
        )
    return r.json()
