from bs4 import BeautifulSoup

def main():
    file_paths = [
        './wine_reports/top-100-wines-of-2019.txt',
        './wine_reports/top-100-wines-of-2020.txt',
        './wine_reports/top-100-wines-of-2021.txt'
    ]

    list = []

    for file_path in file_paths:
        file = open(file_path, "r")
        html = file.read()
        soup = BeautifulSoup(html, 'html.parser')

        accordion = soup.find('div', 'tasting-note-response')
        try:
            for group in accordion.find_all('div', 'accordion-group'):
                print(group.find('span', 'title-vintage').text)
                name = group.find('span', 'title-vintage').text
                country = group.find('div', 'country').text
                region = group.find('div', 'region').text
                vintage = group.find('div', 'vintage').text
                score_holder = group.find('div', 'score')
                score = score_holder.find('div', 'count').text
                notes = group.find('div', 'description').text
                list.append(
                    f'''NAME: {name}, COUNTRY: {country}, REGION: {region}, VINTAGE: {vintage}, SCORE: {score}, NOTES: {notes}\n''')
                # list.append(f'''{name} is a wine from the {region} region in {country} it's a {vintage} vintage with a score of {score} out of 100. Tasting Notes: {notes}\n''')
        except AttributeError:
            pass

    html=open('wine_tasting_notes_tagged.csv', 'w')
    for line in list:
        html.writelines([line])

    html.close()


if __name__ == '__main__':
    main()
