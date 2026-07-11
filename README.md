# ✈️ TravelPlanner — AI Travel Planner

> **An AI-powered Travel Planner Agent built with Python Flask and IBM watsonx.ai (Granite models)**

TravelPlanner generates personalised, day-wise travel itineraries, budget breakdowns, hotel suggestions, packing checklists, visa guidance, and much more — all through a beautiful conversational chat interface.

---

## 📸 Screenshots

| Dashboard & Chat | Trip Planner Form |
|:---:|:---:|
| Conversational AI chat with Granite | Day-wise itinerary generation |

---

## 🚀 Features

### 🤖 AI Capabilities (IBM watsonx.ai + Granite)
- **Personalised Day-wise Itinerary Generation** — Morning / Afternoon / Evening breakdown
- **Destination Recommendations** — Top spots + hidden gems
- **Budget Estimation** — Flights, hotels, food, transport, activities & misc
- **Hotel & Accommodation Suggestions** — 3 price tiers
- **Flight & Transportation Recommendations**
- **Tourist Attraction Recommendations** — UNESCO sites & local gems
- **Restaurant & Local Cuisine Suggestions** — Including vegetarian options
- **Weather-Aware Travel Advice** — Best seasons to visit
- **Packing Checklist Generation**
- **Visa & Travel Document Guidance**
- **Local Transportation Tips**
- **Emergency Contacts & Safety Recommendations**
- **Multi-turn Conversational Memory** — Context-aware dialogue

### 🗺️ Trip Types Supported
| Type | Description |
|------|-------------|
| 👨‍👩‍👧 Family | Child-friendly, safe, logistically smooth |
| 🧑 Solo | Empowering solo journeys with safety focus |
| 💑 Couple / Honeymoon | Romantic hideaways & experiences |
| 👥 Group / Friends | Group logistics & shared experiences |
| 🏔️ Adventure | Trekking, extreme sports, off-the-beaten-path |
| 💎 Luxury | 5-star stays, private transfers, exclusives |
| 🎒 Budget | Hostels, local food, free attractions |
| 🦁 Wildlife | Safari drives, conservation, bird watching |
| ⛪ Pilgrimage | Sacred sites, religious journeys |
| 🏖️ Beach | Coastal retreats, water sports |
| 💼 Business | Efficient itineraries, business amenities |

### 🎨 Frontend
- **Responsive Dashboard** — Works on desktop, tablet, and mobile
- **Conversational Chat Interface** — Real-time AI dialogue
- **Trip Planner Form** — Destination, budget, dates, travelers, interests
- **Day-wise Itinerary Timeline** — Clean markdown-rendered output
- **Budget Summary Cards**
- **Saved Trips** — Persist to localStorage
- **Travel Checklist** — Interactive, customisable
- **Weather Section** — Seasonal travel advice
- **Map Placeholder** — Ready for Google Maps / OpenStreetMap integration
- **User Travel Profile** — Stats tracking (trips, days, countries)
- **Dark Mode** — Toggle with one click
- **Animated Hero** — Globe animation, counter effects
- **Toast Notifications** — User feedback for all actions

---

## 🏗️ Project Structure

```
travel-planner/
├── app.py                          # Flask application entry point
├── config.py                       # Configuration (reads .env)
├── requirements.txt                # Python dependencies
├── .env                            # Secrets (never commit)
├── .env.example                    # Template for .env
│
├── routes/
│   ├── __init__.py
│   ├── main.py                     # HTML page routes
│   └── api.py                      # REST API endpoints (JSON)
│
├── utils/
│   ├── __init__.py
│   ├── agent_instructions.py       # ← CUSTOMISE AGENT HERE
│   └── watsonx_client.py           # IBM watsonx.ai integration
│
├── templates/
│   ├── base.html                   # Shared layout (navbar, footer)
│   └── index.html                  # Main dashboard page
│
└── static/
    ├── css/
    │   └── style.css               # Custom design system
    ├── js/
    │   └── main.js                 # Frontend logic
    └── images/                     # Static images (optional)
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- IBM Cloud account with watsonx.ai access
- IBM Cloud API Key
- watsonx.ai Project ID

### 2. Clone / Navigate to Project
```bash
cd travel-planner
```

### 3. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your credentials:
```bash
cp .env.example .env
```

Edit `.env`:
```env
IBM_API_KEY=your_actual_ibm_cloud_api_key
WATSONX_PROJECT_ID=your_actual_watsonx_project_id
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-3-8b-instruct
FLASK_SECRET_KEY=replace-with-a-long-random-string
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
```

### 6. Run the Application
```bash
python app.py
```

Visit: **http://localhost:5000**

---

## 🔑 Getting IBM watsonx.ai Credentials

### IBM Cloud API Key
1. Go to [https://cloud.ibm.com/iam/apikeys](https://cloud.ibm.com/iam/apikeys)
2. Click **Create an IBM Cloud API key**
3. Give it a name and copy the key

### watsonx.ai Project ID
1. Go to [https://dataplatform.cloud.ibm.com](https://dataplatform.cloud.ibm.com)
2. Open your watsonx.ai project
3. Go to **Manage → General**
4. Copy the **Project ID**

### Supported Granite Models
| Model ID | Description |
|----------|-------------|
| `ibm/granite-3-8b-instruct` | **Recommended** — Best balance of speed & quality |
| `ibm/granite-3-2b-instruct` | Faster & lighter |
| `ibm/granite-13b-chat-v2` | More capable |

### watsonx.ai Regional URLs
| Region | URL |
|--------|-----|
| Dallas (US South) | `https://us-south.ml.cloud.ibm.com` |
| Frankfurt | `https://eu-de.ml.cloud.ibm.com` |
| London | `https://eu-gb.ml.cloud.ibm.com` |
| Tokyo | `https://jp-tok.ml.cloud.ibm.com` |

---

## 🎛️ Customising the Agent

All agent behaviour is controlled from a **single file**: [`utils/agent_instructions.py`](utils/agent_instructions.py)

```python
# Change the agent's name
AGENT_NAME = "TravelPlanner"

# Change personality and tone
AGENT_PERSONALITY = """
You are a friendly, enthusiastic travel expert...
"""

# Adjust response formatting
RESPONSE_STYLE = """
- Use markdown headings and bullet points
- Include cost estimates in every itinerary
...
"""

# Tune budget guidelines
BUDGET_GUIDELINES = """
- Always show Low / Mid-range / Luxury tiers
...
"""

# Modify safety rules
SAFETY_GUIDELINES = """
- Always include emergency numbers
- Recommend travel insurance
...
"""
```

**No restart needed** — changes take effect on the next API call.

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/chat` | Send a chat message, get AI reply |
| `POST` | `/api/generate-itinerary` | Generate full itinerary from form data |
| `POST` | `/api/clear-history` | Reset conversation for the session |
| `GET` | `/api/greeting` | Get the agent's greeting message |
| `GET` | `/api/health` | Service health + watsonx.ai status |

### Example: `/api/chat`
```json
// Request
POST /api/chat
{ "message": "Plan a 7-day trip to Japan for 2 people on a mid-range budget." }

// Response
{
  "reply": "<html rendered markdown>",
  "raw": "markdown string",
  "session_id": "uuid"
}
```

### Example: `/api/generate-itinerary`
```json
// Request
POST /api/generate-itinerary
{
  "destination": "Paris",
  "origin": "New York",
  "start_date": "2025-04-10",
  "duration": "7",
  "travelers": "2",
  "traveler_type": "couple",
  "budget": "mid-range",
  "travel_style": "Romantic & Honeymoon",
  "interests": "History & Culture, Local Cuisine",
  "special_requirements": "Vegetarian meals preferred"
}
```

---

## 🚀 Deployment

### Option 1: IBM Code Engine (Recommended for IBM ecosystem)
```bash
# Build and push Docker image
docker build -t TravelPlanner-travel-planner .
docker tag TravelPlanner-travel-planner us.icr.io/<namespace>/TravelPlanner:latest
docker push us.icr.io/<namespace>/TravelPlanner:latest

# Deploy to IBM Code Engine
ibmcloud ce application create \
  --name TravelPlanner \
  --image us.icr.io/<namespace>/TravelPlanner:latest \
  --env-from-secret TravelPlanner-secrets
```

### Option 2: Local Docker
```dockerfile
# Dockerfile (create in project root)
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```
```bash
docker build -t TravelPlanner .
docker run -p 5000:5000 --env-file .env TravelPlanner
```

### Option 3: Heroku / Render / Railway
```bash
# Add a Procfile
echo "web: python app.py" > Procfile

# Set environment variables in your platform's dashboard
# then deploy via git push
```

### Production Checklist
- [ ] Set `FLASK_ENV=production` and `FLASK_DEBUG=False`
- [ ] Generate a strong random `FLASK_SECRET_KEY`
- [ ] Use environment secrets (not a `.env` file) in production
- [ ] Set up HTTPS / TLS termination
- [ ] Configure a production WSGI server (Gunicorn): `gunicorn app:app`
- [ ] Set up proper logging and monitoring

---

## 🧪 Testing the Health Endpoint

```bash
curl http://localhost:5000/api/health
```

Expected response when configured correctly:
```json
{
  "service": "Travel Planner Agent",
  "status": "running",
  "watsonx": {
    "status": "ok",
    "model": "ibm/granite-3-8b-instruct",
    "url": "https://us-south.ml.cloud.ibm.com"
  }
}
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Credits

- **IBM watsonx.ai** — Foundation model API
- **IBM Granite** — Language model
- **Flask** — Python web framework
- **Bootstrap 5** — CSS framework
- **Bootstrap Icons** — Icon library
- **Inter & Playfair Display** — Google Fonts

---

*Built with ❤️ for explorers everywhere. Happy travels! ✈️*
