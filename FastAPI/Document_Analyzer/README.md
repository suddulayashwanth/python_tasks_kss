# Gemini AI - Intelligent Document Analyzer

This project reads a document from a file, generates a summary and interview
questions using Gemini AI, and stores the result in MongoDB.

## Project Structure

Document_Analyzer/
- app.py
- requirements.txt
- .env.example
- config/
- repository/
- service/
- utils/
- documents/

## Setup

### 1. Open the project in VS Code

Open the `Document_Analyzer` folder.

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

### 6. Create `.env`

Copy `.env.example` and rename the copy to `.env`.

Then add your Gemini API key:

```env
GEMINI_API_KEY=your_real_api_key
MONGO_URI=mongodb://localhost:27017/
```

For MongoDB Atlas, replace `MONGO_URI` with your Atlas connection string.

### 7. Run

```powershell
python app.py
```
