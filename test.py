from database_handler import save_sentiment_to_db
from sentiment_engine import *

TEST_CASES = [
    "Hôm nay tôi rất vui",
    "Món ăn này dở quá",
    "Thời tiết bình thường",
    "Rat vui hom nay",
    "Công việc ổn định",
    "Phim này hay lắm",
    "Tôi buồn vì thất bại",
    "Ngày mai đi học",
    "Cảm ơn bạn rất nhiều",
    "Mệt mỏi quá hôm nay"
]

for test in TEST_CASES:
    directory = predict_sentiment(test)
    print(directory, "\n")

    # Uncomment the line below if you want to create example data
    # save_sentiment_to_db(directory)