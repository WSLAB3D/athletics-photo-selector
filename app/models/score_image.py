def score_image(tags):
    score = 0
    score += tags.get("pose_score", 0)
    score += tags.get("num_athletes", 0) * 2
    if tags.get("gender") != "unknown":
        score += 1
    if tags.get("ethnicity") != "unknown":
        score += 1
    score += tags.get("clip_score", 0) * 10
    return score
