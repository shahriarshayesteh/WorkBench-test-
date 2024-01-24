import pandas as pd
import argparse
from src.evals.utils import is_correct

parser = argparse.ArgumentParser()
parser.add_argument("--predictions_path", type=str, help="path to answers csv")
parser.add_argument("--ground_truth_path", type=str, help="path to ground truth csv")
args = parser.parse_args()

predictions = pd.read_csv(args.predictions_path)
predictions = predictions.rename(columns={"function_calls": "prediction"})
predictions = predictions.fillna("")

ground_truth = pd.read_csv(args.ground_truth_path, dtype=str)
ground_truth = ground_truth.rename(columns={"answer": "ground_truth"})

assert len(predictions) == len(
    ground_truth
), "Number of predictions does not match number of ground truth answers."

df = predictions.merge(ground_truth, on="question")

df["correct"] = df.apply(is_correct, axis=1)

# print out the questions that were not answered correctly
print(df[~df["correct"]])

# print accuracy as a percentage to 2dp
print(f"Accuracy: {round(df['correct'].mean() * 100, 2)}%")
