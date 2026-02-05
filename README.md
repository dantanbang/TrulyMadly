AI Operations Assistant

An AI-powered operations assistant that utilizes a multi-agent architecture to process natural language tasks, plan execution steps, call external APIs, and verify results. This project was developed for the 24-Hour GenAI Intern Assignment.

🚀 Core Capabilities

Multi-Agent Architecture: Dedicated Planner, Executor, and Verifier.

LLM Reasoning: Powered by Google Gemini 1.5 Flash for planning and verification.

Real-world API Integration: Integrated with OpenWeatherMap API and GitHub Search API.

Local Execution: Runs locally via a Command Line Interface (CLI).

📂 Project Structure

ai_ops_assistant/
├── agents/             # Logic for Planner, Executor, and Verifier
├── tools/              # API tool functions (Weather, GitHub)
├── llm/                # Gemini client configuration
├── main.py             # Entry point of the application
├── requirements.txt    # List of project dependencies
└── README.md           # Documentation


🛠️ Installation & Setup

Install Dependencies:
Open your terminal in the project folder and run:

python -m pip install -r requirements.txt


Environment Configuration:
Create a .env file in the root directory and add your API keys:

GEMINI_API_KEY=your_gemini_key
OPENWEATHER_API_KEY=your_weather_key
GITHUB_TOKEN=your_github_token


Run the Assistant:

python main.py


📋 Evaluation Criteria Check

[x] Multi-agent architecture (Planner, Executor, Verifier)

[x] Integration with 2+ real APIs

[x] LLM-powered reasoning (JSON plan generation)

[x] Clear documentation and project structure
