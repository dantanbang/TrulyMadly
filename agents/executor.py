from tools.api_tools import get_weather, search_github

class ExecutorAgent:
    def __init__(self):
        # Map the tool names from the planner to actual Python functions
        self.tools = {
            "get_weather": get_weather,
            "search_github": search_github
        }

    def execute_plan(self, plan: dict):
        """
        Iterates through the steps in the plan and calls the tools.
        """
        results = []
        
        if "error" in plan:
            return plan
            
        for step in plan.get("steps", []):
            tool_name = step.get("tool")
            args = step.get("args", {})
            
            if tool_name in self.tools:
                print(f"Executing {tool_name} with args {args}...")
                tool_result = self.tools[tool_name](**args)
                results.append({
                    "step": step.get("step"),
                    "tool": tool_name,
                    "output": tool_result
                })
            else:
                results.append({
                    "step": step.get("step"),
                    "error": f"Tool '{tool_name}' not found."
                })
                
        return results
