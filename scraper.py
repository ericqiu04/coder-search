from bs4 import BeautifulSoup
import requests


def ScrapeURL(text):
    url = "https://google.com/search?q="
    result = url + text + "+site:stackoverflow.com"
    print(url)
    return result


def scrape_page(url):
    response = requests.get(ScrapeURL(url))
    questions = []
    soup = BeautifulSoup(response.text, "html.parser")
    question_summary = soup.find_all("a", href=True)

    for q in question_summary:
        url = q.get('href')
        furl = url.strip('/url?q=')
        if furl.startswith("https://stackoverflow.com/questions/"):
            questions.append(furl)

    value = answer_scrape(questions[0])
    print(value)
    return value


def answer_scrape(url):
    print(url)
    response = requests.get(url)
    answers = []
    soup = BeautifulSoup(response.text, "html.parser")
    answer_summary = soup.find_all("div", class_="accepted-answer")

    print(answer_summary)
    # check if none
    if len(answer_summary) == 0:
        answer = soup.find_all("div", class_="answer")

        largest = 0
        index = 0
        for a in answer:
            num = a.select("js-vote-count")

            print(num)


        answer_summary.append(answer[index])

    print(answer_summary)


    for a in answer_summary:
        c = a.find_all('pre')

    listS = map(str, c)
    list_string = map(split, listS)

    print(list_string)

    return list(list_string)


def split(n):
    mytext = n.replace('\\n', '<br>')
    mytext = mytext.replace('\n', '<br>')
    mytext = mytext.replace('\\t', '&nbsp; &nbsp;')
    mytext = mytext.replace('\t', '&nbsp; &nbsp;')
    return mytext
