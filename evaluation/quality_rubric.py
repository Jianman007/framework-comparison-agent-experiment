"""
Human-defined rubric evaluation
for framework comparison experiment.

Quality is evaluated based on a 10-point rubric:

1. Completeness (0-2)
2. Structure & Organization (0-2)
3. Factual Consistency (0-2)
4. Professional Writing (0-2)
5. Actionability (0-2)

Total Score = 10 points
"""


frameworks = {


    "LangGraph": {

        "Completeness": {
            "score": 2,
            "reason":
            "Included all major report sections such as executive summary, "
            "completed tasks, issues, next steps, KPI and action items."
        },

        "Structure & Organization": {
            "score": 2,
            "reason":
            "Provided a clear multi-stage workflow and well-organized report structure."
        },

        "Factual Consistency": {
            "score": 1,
            "reason":
            "Introduced unsupported information including project metadata, "
            "KPI values and technical metrics not provided in the input."
        },

        "Professional Writing": {
            "score": 2,
            "reason":
            "Used professional business reporting language with clear explanations."
        },

        "Actionability": {
            "score": 2,
            "reason":
            "Provided detailed next steps, risks, mitigation strategies and owners."
        }
    },


    "AutoGen": {

        "Completeness": {
            "score": 1.5,
            "reason":
            "Included core report sections but contained more template placeholders "
            "and fewer completed details."
        },

        "Structure & Organization": {
            "score": 2,
            "reason":
            "The report followed a clear sequential multi-agent generation process "
            "with understandable sections."
        },

        "Factual Consistency": {
            "score": 2,
            "reason":
            "Mostly stayed aligned with the provided weekly updates without "
            "introducing unsupported metrics."
        },

        "Professional Writing": {
            "score": 1.5,
            "reason":
            "Readable and professional, but contained many placeholder fields "
            "which reduced final report quality."
        },

        "Actionability": {
            "score": 1.5,
            "reason":
            "Provided general next steps but lacked detailed ownership and mitigation."
        }
    },


    "CrewAI": {

        "Completeness": {
            "score": 2,
            "reason":
            "Generated a complete weekly report covering progress, issues, "
            "next steps and mitigation."
        },

        "Structure & Organization": {
            "score": 2,
            "reason":
            "Role-based workflow produced a clearly organized business report."
        },

        "Factual Consistency": {
            "score": 1.5,
            "reason":
            "Mostly followed the input but added some assumptions beyond "
            "the original updates."
        },

        "Professional Writing": {
            "score": 2,
            "reason":
            "Output demonstrated strong business writing style and readability."
        },

        "Actionability": {
            "score": 2,
            "reason":
            "Included practical actions and mitigation approaches."
        }
    },


    "MetaGPT Multi-Agent": {

        "Completeness": {
            "score": 2,
            "reason":
            "Generated all required report components including mitigation planning."
        },

        "Structure & Organization": {
            "score": 2,
            "reason":
            "Produced a concise but logically structured project report."
        },

        "Factual Consistency": {
            "score": 1.5,
            "reason":
            "Generally followed the input but introduced some additional "
            "interpretation of project status."
        },

        "Professional Writing": {
            "score": 2,
            "reason":
            "Used professional project management language and concise formatting."
        },

        "Actionability": {
            "score": 2,
            "reason":
            "Provided clear mitigation actions for the API timeout issue."
        }
    },


    "MetaGPT Single-Agent": {

        "Completeness": {
            "score": 2,
            "reason":
            "Generated a complete weekly project report containing all required sections."
        },

        "Structure & Organization": {
            "score": 2,
            "reason":
            "Maintained a clear report hierarchy despite using a single action-based agent."
        },

        "Factual Consistency": {
            "score": 1.5,
            "reason":
            "Added some assumptions such as dates and technical details not explicitly provided."
        },

        "Professional Writing": {
            "score": 2,
            "reason":
            "Generated a polished and professional project report."
        },

        "Actionability": {
            "score": 2,
            "reason":
            "Included concrete mitigation strategies and future actions."
        }
    }

}



def calculate_total(framework_score):

    total = 0

    for criterion in framework_score.values():

        total += criterion["score"]

    return total



if __name__ == "__main__":


    print("Output Quality Evaluation\n")


    for framework, evaluation in frameworks.items():

        total = calculate_total(evaluation)


        print("=" * 50)

        print(framework)

        print(f"Total Score: {total}/10\n")


        for criterion, result in evaluation.items():

            print(
                f"{criterion}: {result['score']}/2"
            )

            print(
                f"Reason: {result['reason']}\n"
            )