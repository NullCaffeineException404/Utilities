import os
from agents.c4_parser import C4ParserAgent
from agents.selector_agent import SelectorAgent
from agents.planner import PlannerAgent
from agents.reasoning_planner import ReasoningPlannerAgentPostgreSQL
from agents.planner_mongo import PlannerAgentMongoDB
from agents.executor_mongo import ExecutorAgentMongoDB
from agents.executor_postgres import ExecutorAgentPostgreSQL
from agents.logInference_transformer_agent import LogInferenceAgent

def main():
   log_path = os.path.join(os.path.dirname(__file__), "logs", "postgres.log")
   log_agent = LogInferenceAgent(log_path)
   inference = log_agent.infer_failure()

   planner = ReasoningPlannerAgentPostgreSQL()
   trp = planner.generate_trp(inference["failure_type"], "critical")

   print(f"\n Inferred Failure: {inference['failure_type']} (Confidence: {inference['confidence']})")
   print(" Evidence:")
   for line in inference["evidence"]:
        print(f"  - {line}")

   print("\n Recovery Plan:")
   for step in trp["steps"]:
        print(f"  - {step}")


if __name__ == "__main__":
    main()

