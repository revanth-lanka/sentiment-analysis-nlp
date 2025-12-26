# 🚘 EXACT STEP-BY-STEP GUIDE (COPY-PASTE READY)

## FOR WINDOWS USERS

### STEP 1: Download and Install Python (if you don't have it)

**Action:**
1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.11" (or newer)
3. Run the installer
4. **IMPORTANT:** Check "Add Python to PATH" (✅)
5. Click "Install Now"
6. Wait for it to finish

**Verify Installation:**
1. Open Command Prompt (Press Windows key + type `cmd`, press Enter)
2. Type: `python --version`
3. You should see: `Python 3.11.x` or higher

---

### STEP 2: Open Command Prompt

**Action:**
1. Press `Windows key`
2. Type `cmd`
3. Click on "Command Prompt"

**You'll see something like:**
```
C:\Users\YourName>
```

---

### STEP 3: Navigate to Downloads (or where you want the project)

**Action:**
Type this command and press Enter:
```
cd Downloads
```

**You'll see:**
```
C:\Users\YourName\Downloads>
```

---

### STEP 4: Download the Project

**Action:**
Copy and paste this command, then press Enter:
```
git clone https://github.com/revanth-lanka/sentiment-analysis-nlp.git
```

**What happens:**
- Files will start downloading
- Wait until you see the prompt again
- It creates a folder called `sentiment-analysis-nlp`

---

### STEP 5: Go Into the Project Folder

**Action:**
Type this command and press Enter:
```
cd sentiment-analysis-nlp
```

**You'll see:**
```
C:\Users\YourName\Downloads\sentiment-analysis-nlp>
```

---

### STEP 6: Install All Required Libraries

**Action:**
Copy and paste this command, then press Enter:
```
pip install -r requirements.txt
```

**What happens:**
- Lots of text will appear
- It downloads PyTorch, Flask, Transformers, etc.
- **DO NOT CLOSE THE TERMINAL**
- Wait 5-10 minutes for it to finish
- You'll see `Successfully installed ...` when done

---

### STEP 7: Start the Application (FIRST TERMINAL)

**Action:**
Type this command and press Enter:
```
python app.py
```

**You'll see:**
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

**IMPORTANT:**
- **DO NOT CLOSE THIS TERMINAL**
- Leave it running
- The app is now running!

---

### STEP 8: Test the API (OPEN A NEW TERMINAL)

**Action:**
1. Press `Windows key`
2. Type `cmd`
3. Click "Command Prompt" (opens a NEW window)

**You'll have TWO terminals now:**
- Terminal 1: Running the app (left open)
- Terminal 2: For testing (new one)

---

### STEP 9: Test Health Check (SECOND TERMINAL)

**Action:**
In the NEW terminal, copy and paste:
```
curl http://localhost:5000/health
```
Press Enter

**Expected Response:**
```json
{"status": "healthy", "service": "sentiment-analysis-api"}
```

✅ **SUCCESS! Your API is working!**

---

### STEP 10: Test Sentiment Analysis (SECOND TERMINAL)

**Action:**
Copy and paste this command (all in one line):
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"This is amazing!\"}"
```
Press Enter

**Expected Response:**
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

✅ **SUCCESS! Your sentiment analysis works!**

---

### STEP 11: Test with Different Texts

**Try These Examples (SECOND TERMINAL):**

**Example 1: Negative Sentiment**
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"This is terrible!\"}" 
```

**Example 2: Neutral Sentiment**
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"It is okay.\"}"
```

**Example 3: Your Own Text**
Replace "Your text here" with anything:
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"Your text here\"}"
```

---

### STEP 12: Batch Test (Multiple Texts)

**Action:**
Copy and paste:
```
curl -X POST http://localhost:5000/batch-predict -H "Content-Type: application/json" -d "{\"texts\": [\"Great!\", \"Terrible!\", \"Good!\"]}"
```
Press Enter

**Expected Response:**
```json
{
  "predictions": [
    {"text": "Great!", "sentiment": "POSITIVE", "confidence": 0.98},
    {"text": "Terrible!", "sentiment": "NEGATIVE", "confidence": 0.97},
    {"text": "Good!", "sentiment": "POSITIVE", "confidence": 0.96}
  ]
}
```

---

## FOR MAC USERS

### STEP 1-6: Same as Windows

Just open Terminal (Cmd + Space, type "terminal")

All the same commands work!

### STEP 7: Start Application

Same command:
```
python app.py
```

### STEP 8-12: Same as Windows

All curl commands work the same!

---

## FOR LINUX USERS

### Everything is the same!

Just use your terminal application

**One tip:** You might need to use `python3` instead of `python`:
```
python3 app.py
```

---

## 📄 SUMMARY OF ALL COMMANDS

| Step | Command | What it does |
|------|---------|-------------|
| 1 | `python --version` | Check if Python is installed |
| 2 | `cd Downloads` | Go to Downloads folder |
| 3 | `git clone https://github.com/revanth-lanka/sentiment-analysis-nlp.git` | Download the project |
| 4 | `cd sentiment-analysis-nlp` | Go into project folder |
| 5 | `pip install -r requirements.txt` | Install all libraries |
| 6 | `python app.py` | Start the app (TERMINAL 1) |
| 7 | `curl http://localhost:5000/health` | Test if working (TERMINAL 2) |
| 8 | `curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"Your text here\"}"` | Test sentiment (TERMINAL 2) |

---

## 🙆 HELP! I Have an Error

### Error: "Python not found"
**Solution:** Install Python from https://www.python.org/downloads/

### Error: "pip not found"
**Solution:** Install Python properly (check "Add Python to PATH")

### Error: "git not found"
**Solution:** Install Git from https://git-scm.com/

### Error: "Port 5000 already in use"
**Solution:** Close other programs using port 5000, or change the port in app.py

### Error: "No module named 'torch'"
**Solution:** Run `pip install -r requirements.txt` again

### Error: "Connection refused"
**Solution:** Make sure the first terminal is still running `python app.py`

### Slow downloads?
**Solution:** This is normal! The BERT model is large (~300MB). Wait patiently.

---

## 👋 IMPORTANT REMINDERS

⚠️ **Terminal 1:** Always keep the terminal running the app open
⚠️ **Terminal 2:** Use a separate terminal for testing commands
⚠️ **Copy-Paste:** Use right-click to paste in Command Prompt
⚠️ **File Location:** Make sure you're in the correct folder
⚠️ **Wait:** Let installations finish before moving to next step

---

## 🎆 YOU DID IT!

You now have:
✅ A running AI application
✅ A sentiment analysis API
✅ Tested it successfully

**Next Steps:**
- Try more text examples
- Modify the code
- Deploy to cloud (Heroku, AWS, etc.)
- Share on GitHub
- Show recruiters for that 50 LPA job!

---

## 📧 Still Stuck?

1. **Read the README.md** on GitHub
2. **Check BEGINNER_GUIDE.md** for concepts
3. **Check WHERE_TO_RUN_STEPS.md** for location help
4. **Google the error message**
5. **Ask on Stack Overflow** with the error

---

**You've got this! Happy coding!** 🚀🚀🚀
