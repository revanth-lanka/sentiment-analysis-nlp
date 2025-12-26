# 🎓 Beginner's Guide to Sentiment Analysis NLP Project

## 📚 What is This Project? (Simple Explanation)

Imagine you want to know if people like your product or not by reading their comments.

**This project does exactly that!**

- You give it a text (like "I love this product!" or "This is terrible")
- It analyzes the text and tells you: Is this positive or negative?
- It also gives you confidence score (how sure it is)

---

## 🤔 Key Concepts (Explained Simply)

### 1. **What is Sentiment Analysis?**
Sentiment analysis = Understanding emotions in text
- "Great product!" = POSITIVE ✅
- "Worst experience ever" = NEGATIVE ❌
- "It's okay" = NEUTRAL

### 2. **What is BERT?**
BERT = Smart AI model that understands language
- It's pre-trained (already learned from millions of texts)
- We're using it to detect emotions in text
- Think of it as a very smart English teacher

### 3. **What is Flask?**
Flask = A tool to create a web API
- API = A way for programs to talk to each other
- We use it so you can send text and get analysis results

### 4. **What is REST API?**
REST API = A standard way to communicate over the internet
- Client sends request → Server processes → Sends response
- Like sending a question and getting an answer

---

## 🚀 How to Run This Project

### Step 1: Prerequisites (Things You Need)
Make sure you have:
- **Python 3.10+** - Download from python.org
- **pip** - Python package manager (comes with Python)
- **Git** - Download from git-scm.com (optional, for cloning)

### Step 2: Download the Project

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/revanth-lanka/sentiment-analysis-nlp.git
cd sentiment-analysis-nlp
```

**Option B: Manual Download**
- Click "Code" button on GitHub
- Click "Download ZIP"
- Extract the ZIP file
- Open terminal in the folder

### Step 3: Install Dependencies

Open your terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

**What this does:**
- Downloads all required libraries (PyTorch, Flask, Transformers, etc.)
- Installs them on your computer
- May take 5-10 minutes (be patient!)

### Step 4: Run the Application

```bash
python app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

✅ **Congratulations! Your API is running!**

---

## 🧪 How to Test the API

### Test 1: Health Check (Is the API Working?)

Open a new terminal and run:

```bash
curl http://localhost:5000/health
```

**Expected response:**
```json
{"status": "healthy", "service": "sentiment-analysis-api"}
```

### Test 2: Single Text Prediction

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!"}'
```

**Expected response:**
```json
{
  "text": "This is amazing!",
  "sentiment": "POSITIVE",
  "confidence": 0.9876,
  "scores": {
    "negative": 0.0124,
    "positive": 0.9876
  }
}
```

### Test 3: Batch Prediction (Multiple Texts)

```bash
curl -X POST http://localhost:5000/batch-predict \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Great!", "Terrible", "Not bad"]}'
```

---

## 📁 Project File Structure

```
sentiment-analysis-nlp/
├── app.py              ← Main application (the brain!)
├── requirements.txt    ← List of dependencies
├── Dockerfile         ← Instructions to run in Docker
├── .env.example       ← Configuration template
├── LICENSE            ← Usage rights
├── README.md          ← Full documentation
└── BEGINNER_GUIDE.md  ← This file!
```

### What Each File Does:

1. **app.py**
   - Contains the Flask application
   - Loads the BERT model
   - Defines API endpoints
   - Processes text and returns sentiment

2. **requirements.txt**
   - Lists all Python libraries needed
   - pip uses this to install everything

3. **Dockerfile**
   - Contains instructions to run the app in a container
   - Useful for deployment

---

## 🔍 Understanding the Code

### app.py - The Main Application

**Key parts:**

1. **Load the Model**
   ```python
   MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
   tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
   model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
   ```
   - Downloads a pre-trained BERT model
   - This model already knows how to detect sentiment!

2. **Preprocess Text**
   ```python
   def preprocess_text(text: str) -> str:
       text = text.lower().strip()
       return text
   ```
   - Cleans the input text
   - Makes it lowercase
   - Removes extra spaces

3. **Predict Sentiment**
   ```python
   def predict_sentiment(text: str) -> Dict:
       # Convert text to tokens
       inputs = tokenizer(text, return_tensors="pt")
       
       # Get predictions
       with torch.no_grad():
           outputs = model(**inputs)
       
       # Return result
       return {"sentiment": "POSITIVE", "confidence": 0.98}
   ```
   - Takes your text
   - Converts it to numbers (tokens)
   - BERT processes it
   - Returns sentiment and confidence

4. **API Endpoints**
   - `/health` - Check if API is running
   - `/predict` - Analyze single text
   - `/batch-predict` - Analyze multiple texts

---

## 🐛 Troubleshooting

### Problem: "Python not found"
**Solution:** Install Python from python.org and add to PATH

### Problem: "pip: command not found"
**Solution:** Install Python properly or use `python -m pip` instead

### Problem: "ModuleNotFoundError: No module named 'torch'"
**Solution:** Run `pip install -r requirements.txt` again

### Problem: "Port 5000 already in use"
**Solution:** Either:
- Close other applications using port 5000
- Change port in app.py (line: `app.run(port=5001)`)

### Problem: Slow first run
**Solution:** Normal! First run downloads the BERT model (~300MB)

---

## 🎯 Next Steps

### Learn More:
1. Read the full README.md
2. Study the app.py code
3. Experiment with different texts
4. Learn about BERT (Google "BERT transformer model")

### Enhance the Project:
1. Add more sophisticated text preprocessing
2. Implement unit tests
3. Create a simple web UI
4. Deploy to cloud (Heroku, AWS, etc.)

### Use It In Real Projects:
1. Product review analysis
2. Customer feedback analysis
3. Social media monitoring
4. Chatbot sentiment detection

---

## 💡 Tips

- **Keep app.py running** - Terminal must stay open while testing
- **Use a new terminal** - For testing commands
- **Save responses** - They're in JSON format (easy to parse)
- **Test different texts** - See how model performs

---

## 🤝 Need Help?

- Check README.md for more details
- Google the error message
- Check GitHub Issues
- Try Stack Overflow

---

## ✨ Summary

**This project:**
- Takes text as input
- Uses AI (BERT) to understand it
- Returns sentiment (positive/negative) + confidence
- Provides REST API for easy integration

**To run it:**
1. Clone/download project
2. `pip install -r requirements.txt`
3. `python app.py`
4. Send requests to `http://localhost:5000`

**Happy Learning!** 🚀
