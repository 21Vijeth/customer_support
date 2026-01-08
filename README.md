
# Customer Support Response Generator

An enterprise-grade, prompt-based AI system designed to generate polite, professional, and safe customer support responses using **Azure OpenAI**. 

## 🎯 Objective
To build a reusable AI component that follows strict enterprise constraints (tone, safety, and length) rather than a casual chat interface. This system uses **Prompt Engineering** as a method of system design.

## 🛠️ Project Structure
- `main.py`: The core logic that handles variable injection and the Azure OpenAI API call.
- `prompts.py`: The Prompt Library containing reusable templates with defined Roles, Tasks, and Constraints.
- `.env`: A protected file for storing sensitive API keys and endpoints.

## 🚀 Setup & Installation

1. **Install Dependencies:**
   ```bash
   pip install openai python-dotenv
   ```

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Azure credentials:
   ```env
   AZURE_OPENAI_API_KEY=your_key_here
   AZURE_OPENAI_ENDPOINT=your_endpoint_uri
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
   ```

3. **Run the System:**
   ```bash
   python main.py
   ```

## 🧠 Key Features
- **Parameterized Prompts:** Supports dynamic inputs like product name, issue type, and tone.
- **Strict Constraints:** Every response is governed by mandatory rules:
    - No false promises or guarantees.
    - No customer blaming.
    - No legal/financial advice.
    - Max length of 120 words.
- **Enterprise-Ready:** Designed to behave as a backend component for professional communication.

## 📝 Usage Example
The system takes a raw customer query and transforms it into a structured response:
- **Input:** *"I've been billed twice!"*
- **AI Response:** A professional, empathetic acknowledgement that follows the internal safety guidelines without making unauthorized financial promises.