import requests

def schedule_spider(url, project, spider, wait_time):
    # Endpoint to schedule spider
    endpoint = f"{url}/schedule.json"

    # Parameters for the request
    data = {'project': project, 'spider': spider, 'wait_time': wait_time}

    # Send the request to schedule the spider
    response = requests.post(endpoint, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Spider scheduled successfully.")
    else:
        print("Failed to schedule spider.")

if __name__ == "__main__":
    scrapyd_url = 'http://localhost:6800'
    project_name = 'dummy_project'
    spider_name = 'dummy'
    wait_time = 10
    schedule_spider(scrapyd_url, project_name, spider_name, wait_time)
