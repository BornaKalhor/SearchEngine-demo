import nltk
from nltk.corpus import stopwords
import re

token_list = []  # 2D list = movies * movie tokens
records = []  # mapped id to preprocessed tokens
documents = []  # mapped id to document contnet
all_tokens = []


def digestData():
    f = open("MovieSummaries/plot_summaries.txt").read()
    tmp_list = re.sub(r'[^\w\s]', '', f)
    tmp_list = tmp_list.split(sep='\n')
    for each in tmp_list[0:4]:
        tmp_tokens = nltk.word_tokenize(each)

        id = int(tmp_tokens[0])
        doc_content = ' '.join(tmp_tokens[1:])

        document = {
            'id': id,
            'doc_content': doc_content
        }
        documents.append(document)

        tmp_tokens = [word.lower() for word in tmp_tokens]
        tmp_tokens = [word for word in tmp_tokens if word not in stopwords.words()]
        token_list.append(tmp_tokens)

        for token in token_list[0:4]:
            all_tokens.append(token[1:])

            id = int(token[0])
            actual_tokens = set(token[1:])

            record = {
                "id": id,
                "tokens": actual_tokens
            }
        records.append(record)


def toCSV() -> None:
    with open('records.csv', 'a') as file:
        for recrod in records:
            file.write("{id},{tokens}\n".format(record[id]))












if __name__ == '__main__':
    digestData()
    all_tokens = ''.join(all_tokens)
    print(all_tokens.)
