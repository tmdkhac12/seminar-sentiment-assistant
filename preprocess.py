from underthesea import word_tokenize

# --- 30 từ phổ biến nhất ---
VIET_NORMALIZER = {
    # --- Teen code / viết tắt (10 từ) ---
    "hok": "không",
    "ko": "không",
    "k": "không",
    "dc": "được",
    "vs": "với",
    "zui": "vui",
    "bn": "bạn",
    "mik": "mình",
    "iu": "yêu",
    "thik": "thích",

    # --- Không dấu -> Có dấu (20 từ) ---
    "toi": "tôi",
    "ban": "bạn",
    "minh": "mình",
    "yeu": "yêu",
    "thuong": "thương",
    "dep": "đẹp",
    "hom": "hôm",
    "nay": "nay",
    "troi": "trời",
    "vui": "vui",
    "buon": "buồn",
    "khoe": "khỏe",
    "rat": "rất",
    "nho": "nhớ",
    "tuyetvoi": "tuyệt vời",
    "an": "ăn",
    "uong": "uống",
    "ngon": "ngon",
    "hen": "hẹn",
    "gap": "gặp",
}

def normalize_text(text: str) -> str:
    if not text or len(text.strip()) < 3 or len(text.strip()) > 50:
        raise ValueError("Độ dài câu phải từ 3-50 kí tự")

    tokens = text.lower().split()
    normalized_tokens = [VIET_NORMALIZER.get(tok, tok) for tok in tokens]
    normalized_text = " ".join(normalized_tokens)

    result = word_tokenize(normalized_text, format="text")

    return result
