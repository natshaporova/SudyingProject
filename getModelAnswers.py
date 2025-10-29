import sqlite3

from haystack import Document
from haystack.components.readers import ExtractiveReader

import json
import os
import requests
from openai import OpenAI

conn = sqlite3.connect('newsEvents.db')
cursor = conn.cursor()

### get all articles
cursor.execute("SELECT * FROM articlesTESTSET")
articlesRows = cursor.fetchall()

### get all questions
cursor.execute("SELECT * FROM questionsMain")
questRows = cursor.fetchall() # return list of tuples, each tuple per row 
cursor.execute("DROP TABLE IF EXISTS answers")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS answers (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  id_article INTEGER, id_question INTEGER, score DOUBLE, answer TEXT, no_answer_probability DOUBLE)""")
conn.commit()

reader = ExtractiveReader(model="deepset/gelectra-base-germanquad-distilled")
reader.warm_up()

for article in articlesRows:
    for quest in questRows:
        docs = [Document(content=f'{article[2]}'),]
        question = f'{quest[1]}'
        result = reader.run(query=question,documents=docs,top_k=1)

        cursor.execute("INSERT INTO answers(id_article,id_question,score,answer,no_answer_probability) VALUES(?,?,?,?,?)",
                      (article[0],quest[0],result["answers"][0].score,result["answers"][0].data, 
                      result["answers"][1].score))
        conn.commit()

######################################
############ use LLama ###############
os.environ["OPENROUTER_API_KEY"] =""
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    )

def useLlamaApi(article_text):
    context = f'{article_text}'
    question = "Wo und wenn sind die verkehrlichen Einschränkungen?"
    prompt = f"""
    Sie sind ein Assistent, der dabei hilft, aus den Nachrichten die aussagekräftigsten Informationen über Verkehrsbeschränkungen und -änderungen zu extrahieren.
    Article:
    \"\"\"{context}\"\"\"

    Question: {question}
    Answer:
    """
    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-70b-instruct", 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=300,
    )

    return(response.choices[0].message.content) 


cursor.execute("""CREATE TABLE IF NOT EXISTS answersFromLLama (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  id_article INTEGER, answer TEXT)""")
conn.commit()

for article in articlesRows:
    model_answer = useLlamaApi(article[2])
    cursor.execute("INSERT INTO answersFromLLama(id_article,answer) VALUES(?,?)",(article[0],model_answer))                      
    conn.commit()