import pandas as pd
from bs4 import BeautifulSoup

def main():
    file_paths = [
        './wine_reports/top-100-wines-of-2019.txt',
        './wine_reports/top-100-wines-of-2020.txt',
        './wine_reports/top-100-wines-of-2021.txt'
    ]

    wine_list = []

    for file_path in file_paths:
        file = open(file_path, "r")
        html = file.read()
        soup = BeautifulSoup(html, 'html.parser')

        accordion = soup.find('div', 'tasting-note-response')
        try:
            for group in accordion.find_all('div', 'accordion-group'):
                notes = group.find('div', 'description').text
                wine_list.append({'prompt': '', 'completion': notes})
        except AttributeError:
            pass

    df = pd.DataFrame(wine_list)
    df.to_csv('wine_tasting_notes_completion_training.csv', index=False)


if __name__ == '__main__':
    main()
