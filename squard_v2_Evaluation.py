import sqlite3
import evaluate
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("deepset/gelectra-base-germanquad-distilled")

def getStartEnd(context,answer) : 
        # Tokenize with offset mapping
        encoded_context = tokenizer(
            context, 
            return_offsets_mapping=True,
            add_special_tokens=False  # Avoids mapping for CLS/SEP tokens
        )
        offsets = encoded_context["offset_mapping"]

        # Find the character start and end for the labeled answer
        answer_start_char = context.find(answer)
        answer_end_char = answer_start_char + len(answer)

        start_token_index = None
        end_token_index = None

        # Find the token indices
        for idx, (start_char, end_char) in enumerate(offsets):
            # Check if the token's character span contains the answer's start
            if start_char <= answer_start_char < end_char:
                start_token_index = idx
            # Check if the token's character span contains the answer's end
            if start_char <= answer_end_char <= end_char:
                end_token_index = idx
                break # We found both, so we can stop
        
        return(start_token_index,end_token_index)
        #print(f"Start token index: {start_token_index}, End token index: {end_token_index}")

        
        
        # Output: Start token index: 4, End token index: 6
        # (Note: This is an approximation as tokenizers can be complex, but it's a much more robust method)

        # To verify, you can decode the tokens
        #tokens = encoded_context.tokens()[start_token_index:end_token_index+1]
        #print(f"Tokens: {tokens}")
        # Output: Tokens: ['13.', 'Juni', '1886']


def getStartEndV2(context,answer) :
    
    answerWords = answer.strip().split(" ")    
    #take first 12 words 
    res_phrase=""
    nwords=0
    if len(answerWords)>10:
        nwords=10
    else:
        nwords=len(answerWords)
    for w in range(0,nwords,1):
        res_phrase+=f"{answerWords[w]} "

    #print(res_phrase)
    start_position = context.find(res_phrase)
    #print(f'start p {start_position}')
    if start_position != -1:
        end_position = start_position + len(answer)
        #print(f"Start index: {start_position}, End index: {end_position}")
        return (start_position,end_position)
    else:
        return(None,None)


conn = sqlite3.connect('newsEvents.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM articlesTESTSET")
articlesRows = cursor.fetchall()


def prepare_predictions_references(id_question):
    predictions = []
    references =[]
    for article in  articlesRows:
        cursor.execute("SELECT * FROM answers WHERE id_question=? AND id_article = ?", (id_question,f'{article[0]}',))
        answerPred = cursor.fetchall()

        ptext=""
        if (answerPred[0][4] is not None ):
            ptext=answerPred[0][4]

        predictions.append(
            {
                "id": f'{article[0]}',
                "prediction_text":f'{ptext}',
                'no_answer_probability':answerPred[0][5]
            }
        )
        cursor.execute("SELECT * FROM answersTEST WHERE id_question=? AND id_article = ?", (id_question,f'{article[0]}',))
        markedAnswersRows = cursor.fetchall()
        articleAnswers=[]
        texts=[]
        starts=[]
        for answ in markedAnswersRows:
            if answ[3]!="":
                (s,e)=getStartEndV2(article[2],answ[3])
                #print(F'{article[0]};{answ[0]};{s};{e}')
                texts.append(answ[3])
                starts.append(s)
        references.append(
        {    
            "id": f'{article[0]}',
            "answers":{"answer_start" : starts, "text" : texts}
        })
    return(predictions,references)           




squad_v2_metric = evaluate.load("squad_v2")

(p1,r1)=prepare_predictions_references(1)

results = squad_v2_metric.compute(predictions=p1, references=r1)
print("question 1")
print(results)

(p2,r2)=prepare_predictions_references(2)
results = squad_v2_metric.compute(predictions=p2, references=r2)
print("question 2")
print(results)