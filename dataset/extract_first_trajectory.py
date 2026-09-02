
import pandas as pd
import json

df = pd.read_parquet(
    r"D:\Huawei_Code\terminal-bench-2\dataset\train-00000-of-00002.parquet"
)

for _, row in df.iterrows():
    steps = json.loads(row["steps"]) if row["steps"] else None

    if isinstance(steps, list) and len(steps) > 0:
        output = {
            "task_name": row["task_name"],
            "agent": row["agent"],
            "model": row["model"],
            "reward": row["reward"],
            "trial_name": row["trial_name"],
            "trial_id": row["trial_id"],
            "steps": steps
        }

        output_file = (
            r"D:\Huawei_Code\terminal-bench-2\dataset\sample_trajectory.json"
        )

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print("saved:", output_file)
        print("task_name:", row["task_name"])
        print("trial_name:", row["trial_name"])
        print("steps:", len(steps))
        break

