# sentiment_engine.py
from transformers import pipeline
from preprocess import normalize_text

# Khởi tạo pipeline chỉ một lần để tránh load lại model
print("Đang khởi chạy mô hình Transformer (phobert-base-v2)...")

MODEL_NAME = "wonrax/phobert-base-vietnamese-sentiment"

sentiment_model = pipeline(
    "sentiment-analysis",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME
)

def predict_sentiment(text: str):
    # Preprocess text before send it to pipeline
    preprocessed = normalize_text(text)

    result = sentiment_model(preprocessed)[0]
    label = result['label']
    # score = round(result['score'], 4)

    # Map result's label into POSITIVE / NEUTRAL / NEGATIVE
    label_map = {
        "POS": "POSITIVE",
        "NEU": "NEUTRAL",
        "NEG": "NEGATIVE"
    }

    return {
        "text": text,
        "sentiment": label_map.get(label, label),
    }

    # return {
    #     "text": text,
    #     "normalized": preprocessed,
    #     "sentiment": label_map.get(label, label),
    #     "score": score
    # }