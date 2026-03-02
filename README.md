# DataSimpleBot

Simple data Telegram bot built with **python-telegram-bot (v 1.0)**.

---

## 📦 Project files

- `botdatosimple.py` – Main bot application. Loads `BotDataSimple_Token` from a `.env` file and starts polling.
- `requirements.txt` – Project dependencies (pinned for Windows stability).
- `.env` – Environment variables (not committed to git).
- `README.md` – Setup and usage instructions.

---

## 🧰 Requirements

- **Python 3.11.x (required)**
- Windows, macOS, or Linux
- A Telegram Bot Token (from @BotFather)

⚠️ **Important**
- Python **3.12+ (including 3.13)** is **not supported** due to dependency wheel issues on Windows.
- This project is tested with **Python 3.11.9**.

## Token
BotDataSimple_Token=your_telegram_bot_token_here

---

## ⚙️ Setup (virtual environment)

Using a virtual environment is strongly recommended.

### Windows (PowerShell)

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Command Prompt (cmd.exe):

```cmd
py -3.11 -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

macOS / Linux (bash/zsh):

```bash
python3.11 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Running the bot

1. Ensure `BotDataSimple_Token` is set in a `.env` file in the project root.
2. Activate your virtual environment (see above).
3. Run:

```bash
py botdatosimple.py
```

You should see a console message ("Bot en ejecución esperando archivos CSV...") and the bot will respond to `/start` and simple messages.

## Notes

- Requires Python 3.10+ (recommended).
- The bot uses `python-dotenv` to load environment variables from a `.env` file.
