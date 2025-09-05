import requests

def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    return response.text

if __name__ == "__main__":
    url = input("Enter the long URL: ")
    short = shorten_url(url)
    print("Shortened URL:", short)