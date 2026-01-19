🚀 Quasar Operation API
A FastAPI project that solves the Quasar Operation challenge by calculating a transmitter’s position using trilateration and reconstructing a fragmented message received by multiple satellites.

🛠️ Key Technologies
- Python 3.10+
- FastAPI – high‑performance API framework
- Uvicorn – ASGI server
- NumPy – vector math for trilateration
- Pydantic – request/response validation
- Swagger UI – automatic API documentation (/docs)

📌 Features
- Trilateration to compute the emitter’s (x, y) position
- Message reconstruction from fragmented satellite messages
- Two operation modes:
- /topsecret – all satellites in one request
- /topsecret_split – satellites sent individually
- Clean modular architecture (routers, services, models)

▶️ Running the Project
1. Install dependencies
pip install -r requirements.txt


2. Start the API
uvicorn app.main:app --reload


3. Open the interactive documentation
http://127.0.0.1:8000/docs



🛰️ Endpoints
POST /topsecret
Send all satellite data at once.
POST /topsecret_split/{satellite_name}
Send satellite data individually.
GET /topsecret_split
Returns the final position + message once all satellites are received.

📂 Project Structure
app/
 ├── main.py
 ├── routers/
 ├── services/
 ├── models/
 └── utils/



👤 Author
Carlos — Mechatronics Engineer transitioning into AI development.
Focused on Python, FastAPI, automation, and intelligent systems.

If you want, I can also generate:
- A French version
- A version with badges (Python, FastAPI, License)
- A version with diagrams
- A version tailored for recruiters
Just tell me which style you prefer.
