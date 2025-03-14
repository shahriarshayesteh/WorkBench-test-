import os
import sys

project_root = os.path.abspath(os.path.curdir)
sys.path.append(project_root)

from src.evals.utils import AVAILABLE_LLMS, generate_results

models = AVAILABLE_LLMS

query_paths = [
    # "data/processed/queries_and_answers/email_queries_and_answers.csv",
    # "data/processed/queries_and_answers/calendar_queries_and_answers.csv",
    # "data/processed/queries_and_answers/analytics_queries_and_answers.csv",
    # "data/processed/queries_and_answers/project_management_queries_and_answers.csv",
    # "data/processed/queries_and_answers/customer_relationship_manager_queries_and_answers.csv",
    "/data/sxs7285/Porjects_code/WorkBench-test-/data/processed/queries_and_answers/multi_domain_queries_and_answers.csv",
]

if __name__ == "__main__":
    # for tool_selection in ["all", "domains"]:
    print("models",models)
    for tool_selection in ["all"]:

        for model in models:
            for query_path in query_paths:
                generate_results(query_path, model, tool_selection)


# touch openai_key.txt && echo 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 > openai_key.txt






# touch anyscale_key.txt && echo QZ7bA4AKkX3QXUedjcu5CKHnLcAdL5wr > anyscale_key.txt
