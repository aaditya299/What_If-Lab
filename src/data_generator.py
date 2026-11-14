import numpy as np
import pandas as pd
n=1000
rng=np.random.default_rng(42)
motivation=rng.normal(0,1,n)
print(motivation[:10])
print("Mean:",np.mean(motivation))
print("Standard deviation:",np.std(motivation))
study_noise=rng.normal(0,0.8,n)
score_noise=rng.normal(0,5,n)
study_hours=6+motivation+study_noise
exam_score=55+2.5*study_hours+4*motivation+score_noise
data=pd.DataFrame({
    "motivation":motivation,
    "study_hours":study_hours,
    "exam_score":exam_score
})
print(data.head())
print("\nDataset statistics:")
print(data.describe())
data.to_csv("data/raw/students.csv",index=False)
print("\nDataset saved successfully")