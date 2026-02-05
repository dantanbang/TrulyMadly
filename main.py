import os
from dotenv import load_dotenv
from llm.gemini_client import GeminiClient
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

def run_assistant():
    # 1. Setup
    print("--- Initializing AI Operations Assistant ---")
    load_dotenv()
    llm = GeminiClient()
    
    planner = PlannerAgent(llm)
    executor = ExecutorAgent()
    verifier = VerifierAgent(llm)

    # 2. Get User Input
    user_query = input("\nWhat task would you like me to perform? ")
    
    # 3. Step 1: Planning
    print("\n[Planner] Creating a step-by-step plan...")
    plan = planner.create_plan(user_query)
    print(f"Plan created: {plan}")

    # 4. Step 2: Execution
    print("\n[Executor] Running tools and fetching data...")
    results = executor.execute_plan(plan)

    # 5. Step 3: Verification & Final Output
    print("\n[Verifier] Checking results and formatting final response...")
    final_answer = verifier.verify_and_finalize(user_query, results)

    print("\n" + "="*50)
    print("FINAL RESPONSE")
    print("="*50)
    print(final_answer)

if __name__ == "__main__":
    run_assistant()
