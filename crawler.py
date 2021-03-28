import requests

def crawl(start_url: str):
    r = requests.get(start_url)
    html = r.text
    print(html)

def run_tests():
    start_url = 'http://127.0.0.1:8000'
    crawl(start_url)

if __name__ == '__main__':
    run_tests()
