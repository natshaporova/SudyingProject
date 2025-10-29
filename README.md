# SudyingProject
Dependences need to be installed
pip install sqlite3
pip install bert_score 
pip install haystack 
pip install requests
pip install openai 
pip install bs4
pip install evaluate


Steps of the project
1. Get news articles from the site of the road segment supporting company (scrapNewsArticles.py)
2. Select  representative news articles as test dataset(createTestNewsArticlesTable.py)
3. Prepare test questions (createQuestionsTable.py)
4. Prepare references (truth answers) based on test dataset and test questions (insertCorrectAnswers.py)
5. Get model answers (getModelAnswer.py)
6. Evaluate  deepset/gelectra-base-germanquad-distilled with squard_v2 metric (squard_v2_Evaluation.py)
7. Evaluate  meta-llama/Llama-3.1-70B-Instruct with BERTscore metric (bertScoreEvaluation.py)
8. all data is saved in the newsEvents sqlite3 database.


To test project results evaluation files can be executed.   