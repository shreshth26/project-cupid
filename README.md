# Project Cupid

A small, mobile-friendly romantic landing page built with Streamlit.

## Run locally

In the VS Code PowerShell terminal, create and activate a virtual environment, install the one dependency, and start Streamlit:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit will print a local address, usually `http://localhost:8501`. Open it in a browser to view the page. To stop the server, press `Ctrl+C` in the terminal.

## Personalize the page

All names and editable messages are grouped in the clearly labeled `PERSONAL_CONTENT` section near the top of `app.py`. The current version addresses Rashi and is signed by Shreshth. Edit the website title, greeting, reasons, letter, question, and surprise there. The copy does not include invented relationship history or memories. The floral photograph and typefaces load from Unsplash and Google Fonts, so those visual assets need an internet connection.

## Try the features

1. Select **Read this reason** on any reasons card to reveal its message. Select it again to close it.
2. Open **Open your letter, Rashi** to read the letter.
3. Choose either answer under the romantic question. Each choice displays its own reply.
4. Select **Open your surprise, Rashi** to reveal the closing message.

The interactions use Streamlit's built-in controls and keep their temporary state in the current browser session. No database or extra packages are used.