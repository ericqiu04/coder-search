from bs4 import BeautifulSoup
import requests


def ScrapeURL(text):
    url = "https://google.com/search?q="
    result = url + text + "+site%3Astackoverflow.com&oq="
    return result


def scrape_page(url):
    response = requests.get(ScrapeURL(url))
    questions = []
    soup = BeautifulSoup(response.text, "html.parser")
    question_summary = soup.find_all("a", href = True)

    for q in question_summary:
        url = q.get('href')
        furl = url.strip('/url?q=')
        if "https://stackoverflow.com" in furl:
            questions.append(furl)

    value = str(answer_scrape(questions[0]))

    return value


def answer_scrape(url):
    print(url)
    response = requests.get(url)
    answers = []
    soup = BeautifulSoup(response.text, "html.parser")
    answer_summary = soup.find_all("div", class_="accepted-answer")

    # check if none
    if answer_summary is None:
        answer_summary = soup.find("div", class_="answer")

    for a in answer_summary:
        code = a.find_all('pre')

    return code[0]



