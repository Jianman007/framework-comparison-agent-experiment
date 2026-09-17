import os
import tiktoken


def count_tokens(text):

    encoding = tiktoken.get_encoding(
        "cl100k_base"
    )

    return len(
        encoding.encode(text)
    )


def count_output_tokens(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    return count_tokens(content)



if __name__ == "__main__":


    output_dir = "../outputs"


    files = {
        "LangGraph": "langgraph_output.md",
        "AutoGen": "autogen_output.md",
        "CrewAI": "crewai_output.md",
        "MetaGPT Multi": "metagpt_multi_output.md",
        "MetaGPT Single": "metagpt_output.md"
    }


    print(
        "Token Consumption:"
    )


    for framework, filename in files.items():

        path = os.path.join(
            output_dir,
            filename
        )


        tokens = count_output_tokens(
            path
        )


        print(
            f"{framework}: {tokens} tokens"
        )