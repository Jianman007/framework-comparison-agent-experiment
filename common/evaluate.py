import time
import json
import os


def load_updates(path="data/weekly_updates.json"):
    """
    Load original project updates.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)



def measure_runtime(func):
    """
    Measure execution time of a function.
    """

    start = time.time()

    result = func()

    end = time.time()

    runtime = end - start

    return result, runtime



def save_output(
        framework_name,
        output,
        runtime=None,
        token_usage=None
):
    """
    Save framework execution results.
    """

    os.makedirs(
        "results",
        exist_ok=True
    )

    result = {
        "framework": framework_name,
        "output": output,
        "runtime_seconds": runtime,
        "token_usage": token_usage
    }


    file_path = (
        f"results/{framework_name}_result.json"
    )


    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            result,
            f,
            indent=4,
            ensure_ascii=False
        )


    return file_path



def basic_quality_check(output):
    """
    Basic rule-based quality evaluation.
    """

    required_sections = [
        "Completed Work",
        "Key Issues",
        "Risks",
        "Next"
    ]


    score = 0


    for section in required_sections:

        if section.lower() in output.lower():
            score += 1


    return {
        "structure_score":
            f"{score}/{len(required_sections)}"
    }