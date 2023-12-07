from sys import argv
import requests
import os
from time import perf_counter


def get_content(url: str):
    response = requests.get(url)
    return response.content

def write_content(content, file):
    if not os.path.exists("./TP6/web_pages"):
        os.makedirs("./TP6/web_pages")
    file = "./TP6/web_pages/"+file
    with open(file, 'wb') as f:
        f.write(content)

def main():
    args = argv[1:]
    # read urls from file
    urls = []
    with open(args[0], "r") as f:
        urls = f.readlines()
    # remove \n from urls
    urls = [url.strip() for url in urls]
    for url in urls:
        file_name="web_"+url.split('//')[1]+".html"
        write_content(get_content(url), file_name)

if __name__ == "__main__":
    start = perf_counter()    
    main()
    end = perf_counter()
    print(f"Time elapsed: {end-start} seconds")