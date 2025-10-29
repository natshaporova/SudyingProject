import sqlite3
from bert_score import score

conn = sqlite3.connect('newsEvents.db')
cursor = conn.cursor()

### get all articles
cursor.execute("SELECT * FROM answersTEST where id_question=1")
baseAnswers = cursor.fetchall()

cursor.execute("SELECT * FROM answersFromLLama")
llamaAnswers = cursor.fetchall()

baseAnsw=[]
curartId=1
fullanswer=""
for answer in baseAnswers:
    if(answer[3]==""):
        curstr="Keine Informationen zu Verkehrsbeschränkungen"
    else:
        curstr=answer[3]

    if(answer[1]==curartId):
        fullanswer+=f" {curstr} "
    else:    
        curartId=answer[1]
        baseAnsw.append(fullanswer)
        fullanswer=""
baseAnsw.append(fullanswer)

llamaAnsw=[]
for answer in llamaAnswers:
    llamaAnsw.append(answer[2])

P, R, F1 = score(llamaAnsw, baseAnsw, lang="de", verbose=True)


for i, (p, r, f) in enumerate(zip(P, R, F1)):
    print(f"Example {i+1}:")
    print(f"  Precision: {p:.4f}")
    print(f"  Recall:    {r:.4f}")
    print(f"  F1 score:  {f:.4f}")
    print()

# 🧾 Average across all examples
print(f"Average F1: {F1.mean().item():.4f}")