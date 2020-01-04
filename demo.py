from OpenNER.main import get_ner

import os
import yake
import json
import nltk.data
import wikipedia

def keyword_extraction_new(question):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(question)

    key = []

    for kw in keywords:
        key.append(kw)
    keys = key[0:3]

    final_keywords = []

    for key in keys:
        final_keywords.append(key[0])

    return final_keywords

def get_context(keyword):
    """r = Rake()
    r.extract_keywords_from_text(question)
    scores = r.get_ranked_phrases()"""

    # print(scores)

    searches = wikipedia.search(keyword)
    context = wikipedia.summary(searches[0])
    title = searches[0]

    print(context)

    return context, title



def mergeDict(dict1, dict2):
    ''' Merge dictionaries and keep values of common keys in list'''


    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value, dict1[key]]
    return dict3


def mergeDict(dict1, dict2):
    ''' Merge dictionaries and keep values of common keys in list'''
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value, dict1[key]]

    return dict3

if __name__ == '__main__':

    while True:
        #try:

            question = str(input('question: '))
            if question != 'Q':
                keywords = keyword_extraction_new(question)

                context1, title1 = get_context(keywords[0])
                #context2, title2 = get_context(keywords[1])
                #context3, title3 = get_context(keywords[2])

                #data, title = get_context(question)

                tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


            if question == 'Q':
                break

            context = context1
            context1 = tokenizer.tokenize(context1)
            #context2 = tokenizer.tokenize(context2)
            #context3 = tokenizer.tokenize(context3)

            inp = [
                {
                    "_id": "5a8b57f25542995d1e6f1371",
                    "answer": "None",
                    "question": question,
                    "supporting_facts": [
                        [
                            "None",
                            0
                        ],
                        [
                            "None",
                            0
                        ]
                    ],
                    "context": [
                        [
                            title1,
                            context1

                        ]
                    ],
                    "type": "None",
                    "level": "None"
                }
            ]

            with open('input.json', 'w') as f:
                json.dump(inp, f)
                f.close()

            os.system('sh full_predict.sh')

            with open('output.json', 'r') as f2:
                out = json.load(f2)

            print('short answer: ', out['answer']['5a8b57f25542995d1e6f1371'])
            print('long answer: ', context)
        #except Exception as e:

            #print('short answer: ', 'Error')
            #print('long answer: ', 'Error')
            #print('Error:', e)

