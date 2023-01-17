from bs4 import BeautifulSoup
import requests


def ScrapeURL(text):
    url = "https://google.com/search?q="
    result = url + text + "%Astackoverflow.com&sxsrf"
    return result


def scrape_page(url):
    response = requests.get(ScrapeURL(url))
    questions = []
    soup = BeautifulSoup(response.text, "html.parser")
    question_summary = soup.find_all("a", href=True)

    for q in question_summary:
        url = q.get('href')
        furl = url.strip('/url?q=')
        if "https://stackoverflow.com" in furl:
            questions.append(furl)
    return answer_scrape(questions[0])


def answer_scrape(url):
    response = requests.get(url)
    answers = []
    soup = BeautifulSoup(response.text, "html.parser")
    answer_summary = soup.find("div", class_="accepted-answer")

    # check if none
    if answer_summary is None:
        answer_summary = soup.find_all("div", class_="answer")
        largest = 0
        index = 0
        for a in answer_summary:
            vote = a.get('js-vote-count')

            if vote > largest:
                largest = vote
                index = a

        answers.append(answer_summary[index])

    else:
        answers.append(answer_summary)

    return code_scrape(answers[0])

def code_scrape(summary):
    code = summary.select('pre code')
    stackCode = []
    print(code)
    for c in code:
        stackCode.append(c)

    return stackCode
