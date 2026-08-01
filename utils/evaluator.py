def evaluate_answer(answer):

    score = 0
    strengths = []
    feedback = []

    answer_lower = answer.lower()

    words = answer.split()
    answer_length = len(words)


    # 1. Answer Detail Check (30%)
    if answer_length >= 40:
        score += 3
        strengths.append(
            "Answer has good explanation and sufficient detail."
        )

    elif answer_length >= 20:
        score += 2
        strengths.append(
            "Answer has basic explanation."
        )

    else:
        score += 1
        feedback.append(
            "Try to explain the concept in more detail."
        )


    # 2. Technical Knowledge Check (40%)

    technical_keywords = [
        "machine learning",
        "artificial intelligence",
        "model",
        "algorithm",
        "training",
        "testing",
        "data",
        "prediction",
        "accuracy",
        "performance",
        "evaluation",
        "classification",
        "regression",
        "deep learning",
        "neural network"
    ]


    matched = 0

    for keyword in technical_keywords:

        if keyword in answer_lower:
            matched += 1


    if matched >= 5:
        score += 4
        strengths.append(
            "Excellent technical understanding."
        )

    elif matched >= 3:
        score += 3
        strengths.append(
            "Good technical concepts."
        )

    else:
        score += 1
        feedback.append(
            "Add more technical concepts."
        )


    # 3. Practical Example Check (20%)

    practical_words = [
        "example",
        "project",
        "real world",
        "application",
        "used",
        "implemented"
    ]


    practical_match = False

    for word in practical_words:

        if word in answer_lower:
            practical_match = True
            break


    if practical_match:

        score += 2

        strengths.append(
            "Included practical application or example."
        )

    else:

        feedback.append(
            "Try adding a real-world example."
        )


    # 4. Structure Check (10%)

    if (
        "because" in answer_lower
        or "therefore" in answer_lower
        or "as a result" in answer_lower
    ):

        score += 1

        strengths.append(
            "Answer structure is clear."
        )

    else:

        score += 1



    # Maximum Score

    if score > 10:
        score = 10



    return {

        "score": score,

        "strengths": strengths,

        "feedback": feedback

    }