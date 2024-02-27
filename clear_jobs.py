import requests

def clear_finished_jobs(url, project):
    # Endpoint to delete project data
    endpoint = f"{url}/delproject.json"

    # Parameters for the request
    params = {'project': project}

    # Send the request to clear finished jobs
    response = requests.post(endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        print("Finished jobs cleared successfully.")
    else:
        print("Failed to clear finished jobs.")

if __name__ == "__main__":
    scrapyd_url = 'http://localhost:6800'
    project_name = 'dummy_project'
    clear_finished_jobs(scrapyd_url, project_name)
