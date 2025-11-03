from database_handler import get_all_sentiments

sentiments = get_all_sentiments()
for item in sentiments:
    print(item)
