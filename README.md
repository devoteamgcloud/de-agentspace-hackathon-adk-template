
# Agentspace Hackathon: Custom ADK Agent Template

This repository contains the template code for creating, testing, and deploying a custom **Sales Assistant Agent** using the **Google Agent Development Kit (ADK)**. This agent is designed to be integrated with **Agentspace** as part of the hackathon.

The agent comes with pre-built tools to:
- ✅ Check product availability in a CRM database.
- ✅ Create sales orders.

---

## 🧠 Project Overview

The goal is to provide a starting point for hackathon participants. You will begin with a basic agent, enable its tools, test it locally, deploy it as a Reasoning Engine, and finally integrate it into the main **Agentspace** environment.

---

## 🚀 Getting Started

Follow these steps to set up your environment and run the agent.

### ✅ Prerequisites

- A **Google Cloud Project** with Billing enabled.
- The **gcloud CLI** installed and authenticated.
- Access to the hackathon's Backend API

---

## 1. Setup Your Cloud Environment

### 🖥️ Open Cloud Shell

In the Google Cloud Console, click the **Activate Cloud Shell** icon. For the best experience, open the editor and run the shell in a new tab.

### 🔐 Authenticate & Set Project

```bash
gcloud auth login --update-adc
gcloud config set project <your-project-id>
```

### 🧬 Clone This Repository

```bash
git clone https://github.com/anandhan-sivakumar/de-agentspace-hackathon-adk-template.git
cd de-agentspace-hackathon-adk-template
```

---

## 2. Configure the Agent

### 📄 Create a `.env` File

```bash
touch .env
```

### ✏️ Add Environment Variables

```env
GOOGLE_CLOUD_PROJECT="<<Your project ID>>"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_API_BASE_URL="<<URL of your backend API>>"
GOOGLE_GENAI_USE_VERTEXAI=1
```

---

## 3. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage & Testing

### ▶️ Running the Agent Locally

Start the web server:

```bash
adk web .
```

This command will give you a `localhost` URL. Open it in a browser and test it by saying **"hi"**.

---

### ⚙️ Enabling Agent Tools

#### ✏️ Edit `sales_agent/agent.py`

Uncomment the tool definitions and add them inside the `tools` list:

```python
tools = [
    FunctionTool(func=check_product_availability),
    FunctionTool(func=create_order)
]
```

#### ✏️ Edit `sales_agent/instructions.py`

Uncomment the detailed instructions to guide the agent on how to use tools effectively.

---

### 🧪 Test the Tools

Restart the agent and try the following prompts:

- “Is the [Smartphone Model] in [Color] with [Storage] available?”
- “Please create an order for the [Smartphone Model].”

Use a dummy customer ID like: `CUST-2001`.

---

## ☁️ Deployment

After local testing, deploy your agent as a **Reasoning Engine**:

```bash
python sales-assistant-agent/main.py --deploy
```

The process takes 2–5 minutes.

### 📋 Save the Engine Name

After deployment, note down the engine name:

```
projects/<project-id>/locations/us-central1/reasoningEngines/<engine-id>
```

---

## 🔗 Integration with Agentspace

### 🧩 Register the Agent

Run the following (replace placeholders as needed):

```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -H "X-Goog-User-Project: <your-project-id>" \
  "https://discoveryengine.googleapis.com/v1alpha/projects/<your-project-id>/locations/global/collections/default_collection/engines/<your-agentspace-app-id>/assistants/default_assistant/agents" \
  -d '{
    "displayName": "Sales Assistant Agent - ADK",
    "description": "Agent used for checking availability and creating orders",
    "icon": {
      "uri": null
    },
    "adkAgentDefinition": {
      "toolSettings": {
        "toolDescription": "Use this agent when the user is requesting for creating an order or checking availability of a particular product"
      },
      "provisionedReasoningEngine": {
        "reasoningEngine": "projects/<your-project-id>/locations/us-central1/reasoningEngines/<your-engine-id>"
      }
    }
  }'
```

### ✅ Verify in Agentspace

Open the Agentspace UI. Your **Sales Assistant Agent - ADK** should appear. Refresh the page if necessary.

You can now chat with your agent directly inside **Agentspace**!

---

## 📂 Project Structure

```plaintext
.
├── sales-assistant-agent/
│   ├── __init__.py
│   ├── agent.py          # Main agent definition, tools are registered here.
│   ├── config.py         # Agent configuration settings.
│   ├── instructions.py   # System instructions for the agent's behavior.
│   ├── main.py           # Entry point for deploying the agent.
│   └── tools/
│       ├── __init__.py
│       ├── crm_client.py # GCP service client functions.
│       ├── crm_tools.py  # Tool logic (e.g., check availability, create order).
│       └── schema.py     # API schema definitions.
├── .env.example          # Example environment file.
├── requirements.txt      # Project dependencies.
└── README.md             # This file.
```

---

## 🙌 Happy Hacking!
Good luck in the Agentspace Hackathon 🎉
