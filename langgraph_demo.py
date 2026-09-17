import os
import time
from dotenv import load_dotenv
from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END


load_dotenv()



llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

class ReportState(TypedDict):

    updates: str

    plan: str

    draft_report: str

    final_report: str

def planner_node(state):

    prompt = f"""
You are a project manager.

Analyze these weekly updates:

{state["updates"]}

Create a structure for a weekly report.
"""

    response = llm.invoke(prompt)

    return {
        "plan": response.content
    }

def writer_node(state):

    prompt = f"""
You are a technical writer.

Based on this plan:

{state["plan"]}

Generate a professional weekly report.
"""

    response = llm.invoke(prompt)

    return {
        "draft_report": response.content
    }

def reviewer_node(state):

    prompt = f"""
You are a reviewer.

Review this report:

{state["draft_report"]}

Improve it and output the final version.
"""

    response = llm.invoke(prompt)

    return {
        "final_report": response.content
    }

workflow = StateGraph(ReportState)


workflow.add_node(
    "planner",
    planner_node
)


workflow.add_node(
    "writer",
    writer_node
)


workflow.add_node(
    "reviewer",
    reviewer_node
)


workflow.set_entry_point(
    "planner"
)


workflow.add_edge(
    "planner",
    "writer"
)


workflow.add_edge(
    "writer",
    "reviewer"
)


workflow.add_edge(
    "reviewer",
    END
)


app = workflow.compile()


if __name__ == "__main__":

    # =========================
    # Measure Runtime
    # =========================

    start = time.time()


    result = app.invoke(
        {
            "updates":
            """
            Completed:
            - Finished data preprocessing

            Issues:
            - API timeout problem

            Next:
            - Improve model performance
            """
        }
    )


    end = time.time()


    runtime = end - start


    # =========================
    # Print Results
    # =========================

    print("Runtime:", runtime, "seconds")

    print("\nFinal Report:\n")

    print(result["final_report"])



    # =========================
    # Save Output
    # =========================

    with open(
            "outputs/langgraph_output.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(result["final_report"])


    print("\nReport saved as langgraph_output.md")