import numpy as np


def calculate_risk(probabilities):

    if len(probabilities) == 0:
        return 0

    current_probability = np.mean(probabilities)

    # Convert to percentage
    risk = current_probability * 100

    return round(float(risk), 2)


def calculate_trend(probabilities):

    if len(probabilities) < 2:
        return "Stable"

    midpoint = len(probabilities) // 2

    first_half = np.mean(
        probabilities[:midpoint]
    )

    second_half = np.mean(
        probabilities[midpoint:]
    )

    difference = second_half - first_half

    if difference > 0.10:
        return "Increasing"

    elif difference < -0.10:
        return "Decreasing"

    return "Stable"


def risk_level(risk):

    if risk <= 30:
        return "LOW"

    elif risk <= 60:
        return "MEDIUM"

    elif risk <= 80:
        return "HIGH"

    return "CRITICAL"


def forecast_attack(probabilities):

    risk = calculate_risk(probabilities)

    trend = calculate_trend(probabilities)

    level = risk_level(risk)

    return {
        "risk": risk,
        "trend": trend,
        "level": level
    }