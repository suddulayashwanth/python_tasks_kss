"""
Quick run file for the Q2 project.

Run:
    python sample_app.py
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
