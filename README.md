# 💬Sentiment Assistant — Vietnamese Sentiment Classification (Transformer + PhoBERT)

Ứng dụng nhỏ để **phân loại cảm xúc tiếng Việt** (POSITIVE / NEUTRAL / NEGATIVE) sử dụng mô hình Transformer (PhoBERT / model fine-tuned), kết hợp tiền xử lý (normalize, tokenization, có tùy chọn restore diacritics).  
Lưu lịch sử kết quả vào SQLite và có giao diện Streamlit đơn giản.

---
## 📁 Cấu trúc project
```
sentiment_assistant/
├── app.py                  # 💻 Giao diện Streamlit
├── database_handler.py     # 🧩 Xử lý đọc/ghi dữ liệu từ SQLite
├── init_database.py        # 🗃️ Script khởi tạo database (chạy 1 lần)
├── preprocess.py           # 🧠 Tiền xử lý văn bản trước khi đưa vào Transformer
├── sentiment_engine.py     # ⚡ Mô hình Transformer dự đoán nhãn cảm xúc
├── sentiments.db           # 💾 Database cục bộ lưu trữ lịch sử dự đoán
├── test.py                 # 🧪 Script test nhanh
└── requirements.txt        # 📦 Danh sách thư viện cần thiết
```
---
## ⚙️ Cài đặt nhanh (Windows)
### 1. Mở PowerShell / CMD ở folder project:
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1        # PowerShell
# hoặc: .\.venv\Scripts\activate    # CMD
```

### 2. Cập nhật pip và cài dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Khởi tạo database
```
python init_database.py     
```

### 4. Chạy ứng dụng (Streamlit)
🔹 Bạn có thể test nhanh thông qua terminal (Khuyến khích với lần chay đầu tiên vì cần phải tải model, sau đó có thể chạy qua cách bên dưới)
```
python test.py
```
🔹 Hoặc truy cập giao diện ứng dụng qua http://localhost:8501
```
streamlit run app.py --server.headless true
```

---
## ✨ Kết quả
Ứng dụng sẽ hiển thị cảm xúc dự đoán và lưu lại lịch sử trong bảng SQLite,
giúp bạn dễ dàng theo dõi và phân tích cảm xúc tiếng Việt một cách trực quan.