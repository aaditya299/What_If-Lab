import numpy as np
import pandas as pd
def generate_motivation(n,rng):
    return rng.normal(0,1,size=n)

def generate_study_hours(motivation,rng):
    return 6+ motivation+rng.normal(0,0.8,len(motivation))

def generate_exam_score(study_hours,motivation,rng):
    return 55+2.5*study_hours+4*motivation+rng.normal(0,5,len(motivation))

def simulate(n,rng,intervention=None):
    motivation=generate_motivation(n,rng)
    if intervention and "study_hours" in intervention:
        study_hours = np.full(n, intervention["study_hours"])
    else:
        study_hours = generate_study_hours(motivation, rng)
    exam_score=generate_exam_score(study_hours,motivation,rng)
    return pd.DataFrame({
        "motivation":motivation,
        "study_hours":study_hours,
        "exam_score":exam_score
    })

# rng = np.random.default_rng(42)
# motivation = generate_motivation(5, rng)
# print(motivation)

# study_hours = generate_study_hours(motivation, rng)
# print(study_hours)

# exam_score = generate_exam_score(study_hours, motivation, rng)
# print(exam_score)

# data = simulate(1000, rng)
# print(data.head())
# print(data.describe())

rng = np.random.default_rng(42)
baseline = simulate(1000, rng)
rng = np.random.default_rng(42)
intervention_data = simulate(1000, rng, {"study_hours": 8})
print(baseline.head())
print(intervention_data.head())

print("Baseline mean:", baseline["exam_score"].mean())
print("Intervention mean:", intervention_data["exam_score"].mean())
effect = (
    intervention_data["exam_score"].mean()
    - baseline["exam_score"].mean()
)
print("Estimated effect:", effect)

print("\n--- Intervention Comparison ---")
print("Baseline mean:", baseline["exam_score"].mean())
print("Intervention mean:", intervention_data["exam_score"].mean())
effect = intervention_data["exam_score"].mean() - baseline["exam_score"].mean()
print("Estimated effect:", effect)
