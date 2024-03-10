def standardize_scores(score):
    if score >= 5:
        return score / 20
    else:
        return score