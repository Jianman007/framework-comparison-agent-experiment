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
from metagpt.llm import LLM



# =========================
# 1. Define Action
# =========================


class GenerateReportPlan(Action):
    PROMPT_TEMPLATE = """
    You are a project manager.

    Analyze the following weekly updates:

    {updates}


    Generate a professional weekly project report.

    The report should include:

    1. Executive Summary
    - Overall project status
    - Key achievements
    - Main issues

    2. Completed Tasks
    - Describe completed work clearly

    3. Issues and Risks
    - Explain blockers and potential impact

    4. Next Steps
    - Describe upcoming activities

    5. Risks and Mitigation
    - Provide possible solutions

    Use a professional business writing style.
    """


    async def run(self, context):

        prompt = self.PROMPT_TEMPLATE.format(
            updates=context
        )

        response = await self._aask(
            prompt
        )

        return response



# =========================
# 2. Define Role
# =========================


# =========================
# 3. Run Test
# =========================

async def main():
    action = GenerateReportPlan(
        llm=LLM()
    )


    weekly_updates = """
    Completed:
    - Finished data preprocessing

    Issues:
    - API timeout problem

    Next:
    - Improve model performance
    """
    start = time.time()

    result = await action.run(
            weekly_updates
        )

    end = time.time()

    print(
        "Runtime:",
        end - start,
        "seconds"
    )


    print("\nReport Plan:\n")

    print(result)


    with open(
        "outputs/metagpt_output.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(result)

if __name__ == "__main__":

    asyncio.run(main())