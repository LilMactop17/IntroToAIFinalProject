# Setup Instructions

Follow these steps to set up and run the application:

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python3 app.py
   ```
If requirements.txt not found, repair venv
```bash
   deactivate
   rm -rf .venv
```
