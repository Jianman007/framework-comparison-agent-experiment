import asyncio
import time

from dotenv import load_dotenv

load_dotenv()


# =========================
# MetaGPT compatibility fix
# =========================

from metagpt.provider import openai_api


openai_api.count_message_tokens = lambda messages, model: 0

openai_api.OpenAIGPTAPI._update_costs = lambda self, rsp: None

openai_api.count_string_tokens = lambda text, model: 0



# =========================
# Import MetaGPT
# =========================

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.llm import LLM



# =========================
# 1. Define Actions
# =========================


class GenerateReportPlan(Action):

    async def run(self, updates):

        prompt = f"""
You are a project manager.

Analyze these weekly updates:

{updates}


Create a report plan.

Include:
- Executive Summary
- Completed Tasks
- Issues
- Next Steps
"""

        response = await self._aask(prompt)

        return response



class WriteReport(Action):

    async def run(self, plan):

        prompt = f"""
You are a technical writer.

Based on this report plan:

{plan}


Write a professional weekly project report.

Include:
- Executive Summary
- Completed Tasks
- Issues and Risks
- Next Steps
- Mitigation

Do not add unsupported information.
"""

        response = await self._aask(prompt)

        return response



class ReviewReport(Action):

    async def run(self, report):

        prompt = f"""
You are a reviewer.

Review this weekly report:

{report}


Improve:
- clarity
- structure
- professionalism

Return only the final report.
"""

        response = await self._aask(prompt)

        return response



# =========================
# 2. Define Roles
# =========================


class ProjectManager(Role):

    def __init__(self):

        super().__init__(
            name="ProjectManager",
            profile="Project Manager"
        )

        self._actions = [
            GenerateReportPlan()
        ]



class TechnicalWriter(Role):

    def __init__(self):

        super().__init__(
            name="TechnicalWriter",
            profile="Technical Writer"
        )

        self._actions = [
            WriteReport()
        ]



class Reviewer(Role):

    def __init__(self):

        super().__init__(
            name="Reviewer",
            profile="Report Reviewer"
        )

        self._actions = [
            ReviewReport()
        ]



# =========================
# 3. Run Experiment
# =========================


async def main():

    llm = LLM()


    manager = ProjectManager()

    writer = TechnicalWriter()

    reviewer = Reviewer()



    weekly_updates = """
Completed:
- Finished data preprocessing

Issues:
- API timeout problem

Next:
- Improve model performance
"""


    start = time.time()


    # Agent 1
    plan = await manager._actions[0].run(
        weekly_updates
    )


    print("\n===== PLAN =====\n")
    print(plan)



    # Agent 2
    report = await writer._actions[0].run(
        plan
    )


    print("\n===== REPORT =====\n")
    print(report)



    # Agent 3
    final_report = await reviewer._actions[0].run(
        report
    )


    end = time.time()


    print("\n===== FINAL REPORT =====\n")
    print(final_report)



    print(
        "\nRuntime:",
        end-start,
        "seconds"
    )


    with open(
        "outputs/metagpt_multi_output.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(final_report)



if __name__ == "__main__":

    asyncio.run(main())