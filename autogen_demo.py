import os
import asyncio
import time

from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from autogen_ext.models.openai import OpenAIChatCompletionClient


load_dotenv()


# =========================
# 1. Model Configuration
# =========================

model_client = OpenAIChatCompletionClient(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "family": "deepseek"
    }
)



# =========================
# 2. Define Agents
# =========================


project_manager = AssistantAgent(
    name="ProjectManager",
    model_client=model_client,
    system_message="""
You are a project manager.

Your responsibility:
- Analyze weekly project updates.
- Create a clear structure for a weekly report.
- Focus on important achievements, issues and next steps.

Do not write the final report.
Only provide the report plan.
"""
)



technical_writer = AssistantAgent(
    name="TechnicalWriter",
    model_client=model_client,
    system_message="""
You are a technical writer.

Your responsibility:
- Convert the project manager's plan into a professional weekly report.
- Use clear business writing style.
- Include sections such as:
  Executive Summary,
  Completed Tasks,
  Issues,
  Next Steps.

Do not review the report.
"""
)



reviewer = AssistantAgent(
    name="Reviewer",
    model_client=model_client,
    system_message="""
You are a reviewer.

Your responsibility:
- Check the generated weekly report.
- Improve clarity and professionalism.
- Output the final version.

When finished, include the word DONE.
"""
)



# =========================
# 3. Create Team
# =========================


team = RoundRobinGroupChat(
    participants=[
        project_manager,
        technical_writer,
        reviewer
    ],
    termination_condition=TextMentionTermination("DONE")
)



# =========================
# 4. Run Experiment
# =========================


async def main():

    start=time.time()


    task="""
Create a weekly project report.

Weekly updates:

Completed:
- Finished data preprocessing

Issues:
- API timeout problem

Next:
- Improve model performance
"""


    result = await team.run(
        task=task
    )


    end=time.time()


    print(
        "Runtime:",
        end-start,
        "seconds"
    )


    final_output = result.messages[-1].content


    print("\nFinal Output:\n")

    print(final_output)


    with open(
        "outputs/autogen_output.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(final_output)



asyncio.run(main())