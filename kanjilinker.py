import pandas as pd
def main():
    file = pd.read_csv('rtk-kanjis.csv')
    links = []
    for element in file['Kanji']:
        url = 'https://jisho.org/search/'+ element+'%20%23kanji'
        links.append(url)
    file.insert(0,'Jisho link (for vocab)', links, True)
    file.to_csv('rtk-kanjis-jisho.csv', index=False, encoding='utf-8')
if __name__ == '__main__':
    main()
