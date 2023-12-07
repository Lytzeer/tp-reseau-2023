from sys import argv
import requests
import os


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
    file_name=args[0].split('.')[1]+".html"
    print(get_content(args[0]))
    write_content(get_content(args[0]), file_name)

if __name__ == "__main__":
    main()