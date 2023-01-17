from bs4 import BeautifulSoup
import requests


def ScrapeURL(text):
    url = "https://google.com/search?q="
    result = url + text
    return result


def scrape_page(url):
    response = requests.get(ScrapeURL(url))
    questions = []
    soup = BeautifulSoup(response.text, "html.parser")
    question_summary = soup.find_all("div", class_="P8ujBc")
    for q in question_summary:
        questions.append(
            {
                'url': q
            }
        )

    return questions
