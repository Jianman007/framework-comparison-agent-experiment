# Framework Comparison Experiment

A comparative experiment on different LLM agent frameworks for automated weekly project report generation.

## Objective

This project investigates how different LLM agent frameworks perform on the same real-world automation task.

The selected task is:

> Generate a professional weekly project report from raw project updates.

The experiment compares several agent frameworks:

- LangGraph
- AutoGen
- CrewAI
- MetaGPT

The frameworks are evaluated based on:

- Execution efficiency
- Token consumption
- Implementation complexity
- Output quality

---

## Experiment Task

### Input

Raw weekly project updates containing:

- Completed tasks
- Current issues
- Next steps

Example:

```text
Completed:
- Finished data preprocessing

Issues:
- API timeout problem

Next:
- Improve model performance
Output

A structured professional weekly project report containing:

Executive Summary
Completed Tasks
Issues and Risks
Next Steps
Risk Mitigation
Frameworks Compared
Framework	Architecture
LangGraph	Graph-based workflow
AutoGen	Message-based multi-agent workflow
CrewAI	Role-based multi-agent workflow
MetaGPT	Role/Action-based workflow (Single-Agent and Multi-Agent variants)
Evaluation Metrics

The frameworks are compared using four evaluation dimensions:

Metric	Description
Runtime	Total execution time required to generate the report
Token Consumption	Number of tokens consumed during generation
Code Lines (LOC)	Implementation complexity measured by source code size
Output Quality	Quality evaluation based on a structured assessment rubric

The output quality evaluation considers:

Completeness
Structure and Organization
Factual Consistency
Professional Writing
Actionability
Experimental Results
Framework	Runtime (s)	Token Consumption	Code Lines (LOC)	Output Quality
LangGraph	TBD	864	187	9.0/10
AutoGen	TBD	444	170	8.5/10
CrewAI	TBD	610	TBD	9.5/10
MetaGPT Single-Agent	4.55	545	134	9.5/10
MetaGPT Multi-Agent	TBD	248	259	9.5/10

Detailed experimental analysis is available in:

evaluation/results.md
Project Structure
framework-comparison-agent-experiment/

├── data/
│   └── weekly_updates.json
│
├── outputs/
│   ├── langgraph_output.md
│   ├── autogen_output.md
│   ├── crewai_output.md
│   ├── metagpt_output.md
│   └── metagpt_multi_output.md
│
├── evaluation/
│   ├── results.md
│   ├── token_counter.py
│   └── quality_rubric.py
│
├── common/
│   ├── evaluate.py
│   └── prompts.py
│
├── langgraph_demo.py
├── autogen_demo.py
├── crewai_demo.py
├── metagpt_demo.py
├── metagpt_multi_demo.py
│
├── requirements.txt
└── README.md
How to Run
1. Clone the repository
git clone https://github.com/Jianman007/framework-comparison-agent-experiment.git

cd framework-comparison-agent-experiment
2. Install dependencies
pip install -r requirements.txt
3. Configure API Environment

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key
OPENAI_API_BASE=your_api_base
OPENAI_API_MODEL=your_model
4. Run Framework Experiments

Example:

python langgraph_demo.py

Other frameworks:

python autogen_demo.py

python crewai_demo.py

python metagpt_demo.py

python metagpt_multi_demo.py
Notes
All frameworks use the same input task and weekly project update data.
The experiment focuses on differences in agent framework design and workflow implementation.
The comparison does not evaluate the underlying LLM capability itself.
MetaGPT is evaluated using both Single-Agent and Multi-Agent implementations to investigate the impact of agent collaboration.
