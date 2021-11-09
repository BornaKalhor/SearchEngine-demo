# import nltk
# from nltk.corpus import stopwords
# import re
from src.utils import generate_tokens, create_revert_index
import pickle

# token_list = []  # 2D list = movies * movie tokens
# records = []  # mapped id to preprocessed tokens
# documents = []  # mapped id to document contnet
# all_tokens = []


# def digestData():
#     f = open("MovieSummaries/plot_summaries.txt").read()
#     tmp_list = re.sub(r'[^\w\s]', '', f)
#     tmp_list = tmp_list.split(sep='\n')
#     for each in tmp_list[0:4]:
#         tmp_tokens = nltk.word_tokenize(each)

#         id = int(tmp_tokens[0])
#         doc_content = ' '.join(tmp_tokens[1:])

#         document = {
#             'id': id,
#             'doc_content': doc_content
#         }
#         documents.append(document)

#         tmp_tokens = [word.lower() for word in tmp_tokens]
#         tmp_tokens = [word for word in tmp_tokens if word not in stopwords.words()]
#         token_list.append(tmp_tokens)

#         for token in token_list[0:4]:
#             all_tokens.append(token[1:])

#             id = int(token[0])
#             actual_tokens = set(token[1:])

#             record = {
#                 "id": id,
#                 "tokens": actual_tokens
#             }
#         records.append(record)


# def toCSV() -> None:
#     with open('records.csv', 'a') as file:
#         file.write("id, tokens\n")
#         for this in records:
#             id = this['id']
#             tokens = ' '.join(list(this['tokens']))

#             csv_format = "{},'{}'\n".format(id, tokens)
#             file.write(csv_format)


def process_data() -> dict:
    """
        for each movie in the dataset:
            get the summary text
            generate tokens
            generate revert index
    """
    processed = {}
    print('Started generating...')
    with open("plot_summaries.txt") as file:
        for line in file:
            movie_id, summary = line.split('\t')
            tokens = generate_tokens(summary)
            index = create_revert_index(tokens)
            processed[movie_id] = {
                'summary': summary,
                'tokens': tokens,
                'index': index
            }
            # print(processed[movie_id])
    print('Finished...')
    return processed


if __name__ == '__main__':
    # digestData()
    # toCSV()
    try:
        with open('data.pkl', 'rb') as file:
            processed = pickle.load(file)
            print('Loaded files from disk...')
    except FileNotFoundError as e:
        processed = process_data() 
        with open('data.pkl', 'wb') as file:
            pickle.dump(processed, file)    
    
    terms = [
        'apart', 
    ]

    for term in terms:
        for movie_id in processed:
            term_info = processed[movie_id]['index'].get(term, None)
            if term_info:
                repeated_for = term_info['repeat']
                print(f'Movie:{movie_id} term:{term} repeated for: {repeated_for} times')