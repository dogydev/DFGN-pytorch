import os
import yake
import json
import nltk.data
import wikipedia

def keyword_extraction_new(question):
    nlp = spacy.load("en_core_web_sm")
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    nlp.disable_pipes(*other_pipes)


    doc = nlp(question)
    keys = []

    for ent in doc.ents:
        print(ent.label_, ent.text)
        if not ent.label_ == 'DATE' or ent.label_ == 'TIME' or ent.label_ == 'PERCENT' or ent.label_ == 'MONEY' or ent.label_ == 'QUANTITY' or ent.label_ == 'ORDINAL' or ent.label_ == 'CARDINAL':
            keys.append(ent.text)
    return keys

def get_context(keyword):
    """r = Rake()
    r.extract_keywords_from_text(question)
    scores = r.get_ranked_phrases()"""

    # print(scores)
    contexts = ''
    for key in keyword:
        searches = wikipedia.search(key)
        context = wikipedia.summary(searches[0])
        contexts += context

    return contexts


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

                context1, title1 = get_context(keywords)
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

