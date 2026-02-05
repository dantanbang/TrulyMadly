import json
from llm.gemini_client import GeminiClient

class PlannerAgent:
    def __init__(self, llm_client: GeminiClient):
        self.llm = llm_client

    def create_plan(self, user_task: str):
        """
        Converts a user task into a JSON plan.
        """
        prompt = f"""
        You are an AI Operations Planner. Your job is to break down a user request into a sequence of steps.
        You have access to two tools:
        1. get_weather(city: str)
        2. search_github(query: str)

        User Request: "{user_task}"

        Response Format (Strict JSON):
        {{
            "steps": [
                {{"step": 1, "tool": "tool_name", "args": {{"arg_name": "value"}}, "description": "why this step?"}}
            ]
        }}
        
        Only return the JSON object. Do not include markdown formatting or explanations.
        """
        
        raw_response = self.llm.generate_response(prompt)
        
        # Clean up common LLM formatting issues (like ```json blocks)
        clean_json = raw_response.replace('```json', '').replace('```', '').strip()
        
        try:
            return json.loads(clean_json)
        except Exception as e:
            return {"error": f"Failed to parse plan: {str(e)}", "raw": raw_response}
