import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def check_website(url):
    try:
        response = requests.get(url, headers=headers)
    
        return {
            'url': url,
            'ping_sec': round(response.elapsed.total_seconds(), 2),
            'status': response.status_code,
            'is_up': response.status_code == 200
        }
    except requests.exceptions.RequestException:
        return {
            'url': url,
            'ping_sec': 0.0,
            'status': 'Connection Error',
            'is_up': False
        }
