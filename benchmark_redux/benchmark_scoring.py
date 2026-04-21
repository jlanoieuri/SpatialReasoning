from dataclasses import dataclass
from benchmark_types import Score



# string matching scoring functions
def binary_match_score(pred, target):
    # if pred/target are strings, remove whitespace/lowercase/newlines for more lenient matching
    if isinstance(pred, str) and isinstance(target, str):
        pred = pred.strip().lower().replace("\n", " ")
        target = target.strip().lower().replace("\n", " ")

        
    return 1.0 if pred == target else 0.0

def debug_binary_match_score(pred, target):
    score = binary_match_score(pred, target)
    print(f"Predicted: '{pred}', Target: '{target}', Score: {score}")
    return score


def score_prediction(pred, target, scoring_function_name: list=['binary_match']):
    scores = []

    for scoring_function in scoring_function_name:
        if scoring_function == 'binary_match':
            scores.append(Score(score_function='binary_match', calculated_score=binary_match_score(pred, target)))
        elif scoring_function == 'debug_binary_match':
            scores.append(Score(score_function='debug_binary_match', calculated_score=debug_binary_match_score(pred, target)))
        else:
            raise ValueError(f"Unknown scoring function: {scoring_function}")
    return scores