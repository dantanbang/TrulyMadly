from llm.gemini_client import GeminiClient

class VerifierAgent:
    def __init__(self, llm_client: GeminiClient):
        self.llm = llm_client

    def verify_and_finalize(self, user_task: str, execution_results: list):
        """
        Validates results and formats the final answer for the user.
        """
        prompt = f"""
        You are an AI Operations Verifier.
        Original User Task: "{user_task}"
        Raw Data Collected: {execution_results}

        Task:
        1. Check if the data collected answers the user's request.
        2. Format the answer into a professional, structured summary.
        3. If there are errors in the data, explain what went wrong gracefully.

        Final Response:
        """
        
        return self.llm.generate_response(prompt)
