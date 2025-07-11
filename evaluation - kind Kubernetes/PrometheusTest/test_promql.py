

import pandas as pd
import requests

# Prometheus API endpoint
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

# Load the results CSV
results_path = "test_queries.csv"  # Adjust to your file location
results_df = pd.read_csv(results_path)

# Function to test a query against Prometheus API
def test_query(query, timeout=10):
    try:
        response = requests.get(
            PROMETHEUS_URL,
            params={"query": query},
            timeout=timeout
        )
        response.raise_for_status()
        data = response.json()
        status = data.get("status")

        if status == "success":
            result = data.get("data", {}).get("result", [])
            return {
                "valid": True,
                "result_count": len(result),
                "error": None
            }
        else:
            return {
                "valid": False,
                "result_count": 0,
                "error": data.get("error", "Unknown error")
            }
    except requests.exceptions.RequestException as e:
        return {
            "valid": False,
            "result_count": 0,
            "error": str(e)
        }

# List of output columns to evaluate
output_columns = [
    # 'expected_output',
    # 'generated_query',
    # 'fixed promql',
    'rag_v1_output',
    'rag_v2_output',
    'rag_v3_output',
    'rag_v4_output',
    'rag_v5_output',
    # 'rag_v6_output',
    # 'rag_v7_output'
]

# Evaluate all output columns
results = []
for index, row in results_df.iterrows():
    question = row.get('question', 'Unknown')
    result_row = {"question": question}
    
    for col in output_columns:
        query = row[col]
        result_row[f"{col}"] = query  # Store the original query text
        eval_result = test_query(query)
        result_row[f"{col}_is_valid"] = eval_result["valid"]
        result_row[f"{col}_result_count"] = eval_result["result_count"]
        result_row[f"{col}_error"] = eval_result["error"]
    
    results.append(result_row)

# Create a DataFrame with test results
eval_df = pd.DataFrame(results)

# Summary for each output column
print("Summary of Results:")
for col in output_columns:
    valid_count = eval_df[f"{col}_is_valid"].sum()
    total_count = len(eval_df)
    validity_rate = valid_count / total_count * 100 if total_count > 0 else 0
    print(f"{col}:")
    print(f"  Valid Queries: {valid_count}/{total_count}")
    print(f"  Validity Rate: {validity_rate:.2f}%")

# Show problematic queries for each output column
print("\nProblematic Queries:")
for col in output_columns:
    problematic_df = eval_df[
        (~eval_df[f"{col}_is_valid"]) | (eval_df[f"{col}_result_count"] == 0)
    ][['question', col, f"{col}_is_valid", f"{col}_result_count", f"{col}_error"]]
    if not problematic_df.empty:
        print(f"\n{col}:")
        print(problematic_df)

# Save results
eval_path = "tested_promql_title.csv"
eval_df.to_csv(eval_path, index=False)
print(f"\nTest results saved to {eval_path}")

# # python3 -m venv prometheustestenv
# #  source prometheustestenv/bin/activate

# import pandas as pd
# import requests

# # Prometheus API endpoint
# PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

# # Load the results CSV
# results_path = "ragv6.csv"  # Ensure this matches your file location
# results_df = pd.read_csv(results_path)

# # Function to test a query against Prometheus API
# def test_query(query, timeout=10):
#     try:
#         response = requests.get(
#             PROMETHEUS_URL,
#             params={"query": query},
#             timeout=timeout
#         )
#         response.raise_for_status()
#         data = response.json()
#         status = data.get("status")

#         if status == "success":
#             result = data.get("data", {}).get("result", [])
#             return {
#                 "valid": True,
#                 "result_count": len(result),
#                 "error": None
#             }
#         else:
#             return {
#                 "valid": False,
#                 "result_count": 0,
#                 "error": data.get("error", "Unknown error")
#             }
#     except requests.exceptions.RequestException as e:
#         return {
#             "valid": False,
#             "result_count": 0,
#             "error": str(e)
#         }

# # Evaluate generated queries
# results = []
# for index, row in results_df.iterrows():
#     question = row['nl_query']
#     # expected_query = row['expected_query']  # Kept as-is, not evaluated
#     generated_query = row['rag_v6_output']
    
#     eval_result = test_query(generated_query)
#     results.append({
#         "question": question,
#         # "expected_query": expected_query,
#         "generated_query": generated_query,
#         "is_valid": eval_result["valid"],
#         "result_count": eval_result["result_count"],
#         "error": eval_result["error"]
#     })

# # Create a DataFrame with test results
# eval_df = pd.DataFrame(results)

# # Summary
# valid_count = eval_df['is_valid'].sum()
# total_count = len(eval_df)
# validity_rate = valid_count / total_count * 100

# print(f"Valid Queries: {valid_count}/{total_count}")
# print(f"Validity Rate: {validity_rate:.2f}%")

# # Show problematic queries
# problematic_df = eval_df[~eval_df['is_valid'] | (eval_df['result_count'] == 0)]
# print("\nProblematic Queries:")
# print(problematic_df[['question', 'generated_query', 'is_valid', 'result_count', 'error']])

# # Save results
# eval_path = "tested_promql_results6-.csv"
# eval_df.to_csv(eval_path, index=False)
# print(f"Test results saved to {eval_path}")