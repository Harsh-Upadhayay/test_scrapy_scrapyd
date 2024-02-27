import requests
# Removed unused import statement

def fetch_spider_info(url, params):
    # Make the HTTP request to get the response
    response = requests.get(url, params=params)
    response_json = response.json()

    # Extract spider info
    spider_info = {'running': [], 'pending': [], 'finished': []}
    for status, spiders in response_json.items():
        if status in ['running', 'pending', 'finished']:
            for spider in spiders:
                spider_name = spider.get('spider')
                start_time = spider.get('start_time')
                pid = spider.get('pid') if 'pid' in spider else None
                spider_info[status].append([spider_name, start_time, pid])
    return spider_info

def print_spider_info(spider_info):
    # Display spider info with headings
    for status, spiders in spider_info.items():
        print(status.capitalize() + ":")
        for spider in spiders:
            print(spider)
        print()  # Empty line between sections

if __name__ == "__main__":
    url = 'http://localhost:6800/listjobs.json'
    params = {'project': 'dummy_project'}
    spider_info = fetch_spider_info(url, params)
    print_spider_info(spider_info)
