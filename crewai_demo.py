import os
import time

from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM


load_dotenv()


# =========================
# 1. Model Configuration
# =========================

llm = LLM(
    model="deepseek/deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)



# =========================
# 2. Define Agents
# =========================


project_manager = Agent(
    role="Project Manager",
    goal="Analyze weekly updates and create a report structure.",
    backstory="""
You are an experienced project manager.
You focus on identifying achievements,
issues and next steps.
""",
    llm=llm,
    verbose=True
)



technical_writer = Agent(
    role="Technical Writer",
    goal="Generate a professional weekly project report.",
    backstory="""
You specialize in technical documentation
and professional project communication.
""",
    llm=llm,
    verbose=True
)



reviewer = Agent(
    role="Reviewer",
    goal="Review and improve the final report.",
    backstory="""
You are a strict quality reviewer.
You check clarity, structure and accuracy.
""",
    llm=llm,
    verbose=True
)



# =========================
# 3. Define Tasks
# =========================


planning_task = Task(
    description="""
Analyze the following weekly updates:

Completed:
- Finished data preprocessing

Issues:
- API timeout problem

Next:
- Improve model performance


Create a structured plan for a weekly report.
""",
    expected_output="A structured weekly report plan.",
    agent=project_manager
)



writing_task = Task(
    description="""
Based on the project manager's plan,
write a professional weekly project report.
""",
    expected_output="A complete weekly report.",
    agent=technical_writer
)



review_task = Task(
    description="""
Review the generated weekly report.
Improve clarity and professionalism.
Output the final report.
""",
    expected_output="A polished final weekly report.",
    agent=reviewer
)



# =========================
# 4. Create Crew
# =========================


crew = Crew(
    agents=[
        project_manager,
        technical_writer,
        reviewer
    ],
    tasks=[
        planning_task,
        writing_task,
        review_task
    ],
    process=Process.sequential,
    verbose=True
)



# =========================
# 5. Run Experiment
# =========================


start=time.time()


result = crew.kickoff()


end=time.time()


print(
    "Runtime:",
    end-start,
    "seconds"
)


print("\nFinal Output:\n")

print(result)


with open(
    "outputs/crewai_output.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(str(result))