# 👀 WHERE To Run ALL The Steps

## 🙋 Quick Answer

**ALL steps are run in a TERMINAL/COMMAND PROMPT on YOUR COMPUTER**

**NOT in GitHub. NOT in Browser. NOT online.**

---

## 💻 What is a Terminal/Command Prompt?

A terminal is a program where you type commands to control your computer.

**On Windows:**
- Called "Command Prompt" or "PowerShell"
- Press `Windows key` and type `cmd` or `powershell`
- Open it

**On Mac:**
- Called "Terminal"
- Press `Cmd + Space`, type `terminal`, press Enter

**On Linux:**
- Already know this! Open your terminal

---

## 🔟 Step-by-Step: WHERE To Do What

### Step 1: Download the Project
**WHERE:** Your Computer Terminal/Command Prompt
**WHAT:** Copy the project files to your computer

1. Open Terminal/Command Prompt
2. Type this command:
```bash
git clone https://github.com/revanth-lanka/sentiment-analysis-nlp.git
```
3. Press ENTER
4. Wait for it to download

**Visual:**
```
Your Computer
└─ Terminal (OPEN HERE)
   └─ Type: git clone ...
   └─ Press: ENTER
```

---

### Step 2: Go Into Project Folder
**WHERE:** Terminal/Command Prompt
**WHAT:** Navigate into the downloaded folder

```bash
cd sentiment-analysis-nlp
```

Press ENTER

**Visual:**
```
Terminal
└─ Before: C:\Users\YourName\Documents>
└─ After: C:\Users\YourName\Documents\sentiment-analysis-nlp>
```

---

### Step 3: Install Dependencies
**WHERE:** Terminal/Command Prompt (same location)
**WHAT:** Download and install all required libraries

```bash
pip install -r requirements.txt
```

Press ENTER

**IMPORTANT:**
- This will take 5-10 minutes
- You'll see lots of text
- DON'T CLOSE THE TERMINAL
- Wait for it to finish (you'll see the prompt return)

**Visual:**
```
Terminal Output:
Collecting torch==2.0.0
  Downloading torch...
Collecting flask==2.3.2
  Downloading flask...
...
...
Successfully installed ...
```

---

### Step 4: Run the Application
**WHERE:** Terminal/Command Prompt (same location)
**WHAT:** Start the Flask server

```bash
python app.py
```

Press ENTER

**Expected Output:**
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

**Visual:**
```
Terminal
└─ Running on http://127.0.0.1:5000
└─ Leave this terminal OPEN
```

⚠️ **IMPORTANT: KEEP THIS TERMINAL OPEN!**

The terminal must stay open while you're testing!

---

### Step 5: Test the API
**WHERE:** NEW Terminal/Command Prompt (DON'T use the one running the app)
**WHAT:** Send test requests to verify it works

**DO THIS:**
1. Open a SECOND Terminal/Command Prompt window
2. Type this command:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!"}'
```
3. Press ENTER

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

**Visual:**
```
Screen Layout:

┌────────────────────────────────────┐
│ Terminal 1 (KEEP OPEN)             │
│ Running on http://127.0.0.1:5000   │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│ Terminal 2 (USE THIS FOR TESTING)   │
│ $ curl -X POST ...                 │
│ {"sentiment": "POSITIVE", ...}     │
└────────────────────────────────────┘
```

---

## 📊 Complete Visual Workflow

```
1. Your Computer
   ├─ Download Project
   │  └─ Terminal: git clone ...
   │
   ├─ Go into folder
   │  └─ Terminal: cd sentiment-analysis-nlp
   │
   ├─ Install Dependencies
   │  └─ Terminal: pip install -r requirements.txt
   │
   ├─ Start Application
   │  └─ Terminal 1: python app.py
   │     (KEEP OPEN)
   │
   └─ Test the API
      └─ Terminal 2: curl -X POST http://localhost:5000/predict ...
         (Get response)
```

---

## 📦 File Locations

**After downloading, your computer will have:**

```
Your Downloads / Documents
├── sentiment-analysis-nlp/          ← PROJECT FOLDER
├── requirements.txt                 ← DEPENDENCIES LIST
├── app.py                          ← THE APPLICATION
├── BEGINNER_GUIDE.md               ← TUTORIAL
├── WHERE_TO_RUN_STEPS.md           ← THIS FILE!
├── README.md                       ← DOCUMENTATION
├── Dockerfile                      ← DOCKER CONFIG
└── .env.example                    ← SETTINGS
```

---

## 🙌 Common Mistakes

### ❌ Mistake 1: Running commands in GitHub

**WRONG:**
Don't type commands in the GitHub website

**CORRECT:**
Open Terminal on your computer and type there

---

### ❌ Mistake 2: Closing the Terminal Running the App

**WRONG:**
```
Terminal 1: python app.py
(You close it after a few seconds)
```

**CORRECT:**
```
Terminal 1: python app.py
(LEAVE IT OPEN)

Terminal 2: Run your test commands
```

---

### ❌ Mistake 3: Not Installing Dependencies

**WRONG:**
Skipping the `pip install -r requirements.txt` step

**CORRECT:**
Always run this first!
```bash
pip install -r requirements.txt
```

---

### ❌ Mistake 4: Wrong Directory

**WRONG:**
```bash
cd Downloads
pip install -r requirements.txt  ← requirements.txt not here!
```

**CORRECT:**
```bash
cd Downloads
cd sentiment-analysis-nlp       ← Go into project folder first
pip install -r requirements.txt  ← Now it works!
```

---

## 💡 Pro Tips

### Tip 1: Use Copy-Paste
Don't type long commands. Copy them from the guide and paste in terminal:
- Copy: Ctrl+C (or Cmd+C on Mac)
- Paste: Right-click and select Paste

### Tip 2: Multiple Terminals
If you're on Windows:
- Open multiple Command Prompt windows
- One for running the app
- One for testing

### Tip 3: Check if Python is Installed
Run this command:
```bash
python --version
```

You should see: `Python 3.10.x` or higher

If not, download from python.org

---

## 🗓️ Quick Reference

| Step | Command | WHERE | Notes |
|------|---------|-------|-------|
| Download | `git clone https://github.com/revanth-lanka/sentiment-analysis-nlp.git` | Terminal | Once |
| Enter Folder | `cd sentiment-analysis-nlp` | Terminal | Once |
| Install | `pip install -r requirements.txt` | Terminal | Once (takes 10 min) |
| Run | `python app.py` | Terminal 1 | Keep open |
| Test | `curl -X POST http://localhost:5000/predict ...` | Terminal 2 | Multiple times |

---

## 🎆 You're Ready!

Now you know exactly WHERE to run everything!

**Summary:**
1. Open Terminal
2. Download & enter project folder
3. Install dependencies
4. Run the application (Terminal 1)
5. Open new Terminal (Terminal 2)
6. Test the API

**That's it! Happy coding!** 🚀
