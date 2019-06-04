from bs4 import BeautifulSoup
import requests


search = input("Enter Search term: ")
url = "http://www.bing.com/search"
params = {"q": search}
r = requests.get(url, params=params)
print(r.url)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {'id': "b_results"})
links = results.findAll("li", {'class': "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print('\n')
        print(item_text)
        print(item_href)
        print("Summary:", item.find("a").parent.parent.find("p").text)

        children = item.children
        for child in children:
            print("Children:", child)

        sib = item.find("h2")
        print("Next sibling:", sib.next_sibling)
