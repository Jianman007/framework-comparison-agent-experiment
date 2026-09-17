# Framework Comparison Experiment Results

## Experiment Task

**Task:** Multi-Agent Weekly Project Report Generation

**Input:**

Raw weekly project updates containing:

- Completed tasks
- Current issues
- Next steps


**Output:**

A structured professional weekly project report.

---

# Overall Evaluation Summary

| Framework | Architecture | Runtime | Token Consumption | LOC | Output Quality |
|---|---|---|---|---|---|
| LangGraph | Graph-based multi-agent | 12.19s | 864 | 187 | 9/10 |
| AutoGen | Message-based multi-agent | 8.66s | 444 | 170 | 8.5/10 |
| CrewAI | Role-based multi-agent | 9.60s | 610 | 173 | 9.5/10 |
| MetaGPT Multi-Agent | Role + Action-based multi-agent | 8.62s | 248 | 259 | 9.5/10 |
| MetaGPT Single-Agent | Action-based single agent | 4.55s | 545 | 134 | 9.5/10 |

# Output Quality Evaluation

Output quality was evaluated using a human-defined rubric.
The evaluation focuses on five criteria related to weekly project report generation.

| Criterion | Description | Score |
|---|---|---|
| Completeness | Coverage of required report sections | 0-2 |
| Structure & Organization | Logical organization and readability | 0-2 |
| Factual Consistency | Alignment with provided input information | 0-2 |
| Professional Writing | Quality of business-oriented language | 0-2 |
| Actionability | Usefulness of next steps and mitigation | 0-2 |

The maximum quality score is 10 points.

---

# Detailed Framework Analysis

# 1. LangGraph


## Architecture

LangGraph implements a graph-based multi-agent workflow:

Planner Node
↓
Writer Node
↓
Reviewer Node


## Agent Responsibilities

| Agent | Responsibility |
|---|---|
| Planner | Analyze raw updates and design report structure |
| Writer | Generate a professional weekly report |
| Reviewer | Review and improve the generated report |


## Runtime

12.19 seconds


## Output Analysis

### Strengths

- Generated a complete professional project report structure.
- Successfully decomposed the task into multiple sequential stages.
- Reviewer stage improved readability, organization, and stakeholder-oriented communication.
- Workflow execution was explicit and controllable through graph edges.


### Limitations

- The model generated unsupported information beyond the original input.
- Additional details such as project name, reporting period, KPI values, and technical metrics were hallucinated.
- Additional validation or human review would be required for fact-sensitive scenarios.


## Quality Observation

The generated report achieved high completeness and professional writing quality.

However, factual consistency with the original input requires improvement.


## Metrics

| Metric | Result |
|---|--|
| Runtime | 12.19 seconds |
| Output Token Consumption | 864 tokens |
| Code Lines (LOC) | 187 lines |
| Output Quality | 9/10  |

# 2. AutoGen

## Architecture

AutoGen implements a message-based multi-agent collaboration workflow.

ProjectManager Agent  
↓  
TechnicalWriter Agent  
↓  
Reviewer Agent


## Agent Responsibilities

| **Agent** | **Responsibility** |
| ----------------------- | ----------------------------------------------- |
| ProjectManager | Analyze raw updates and create a report plan |
| TechnicalWriter | Transform the plan into a structured weekly report |
| Reviewer | Review and refine the final report quality |


## Runtime

8.66 seconds


## Output Analysis

### Strengths

- Successfully implemented multi-agent collaboration through agent-to-agent message exchange.
- Clear separation of responsibilities between planning, writing, and reviewing stages.
- Generated a structured weekly report with good readability and professional writing style.
- Produced a more conservative output compared with LangGraph, with fewer unsupported factual additions.


### Limitations

- The generated report was less detailed compared with LangGraph.
- Some sections contained placeholders instead of complete project information.
- The workflow execution order depends on predefined agent interaction patterns rather than explicit graph control.
- More detailed instructions are required if specific report formats or evaluation criteria are needed.


## Quality Observation

The generated report demonstrated good factual consistency with the provided input.

Compared with LangGraph, AutoGen showed better control over avoiding unsupported information, but produced a less comprehensive report structure.

The result indicates that AutoGen is suitable for scenarios requiring role-based collaboration and conversational agent interaction.


## Metrics

| **Metric** | **Result**   |
| ----------------- |--------------|
| Runtime | 8.66 seconds |
| Output Token Consumption | 444 tokens   |
| Code Lines (LOC) | 170 lines    |
| Output Quality | 8.5/10       |

# 3. CrewAI


## Architecture

CrewAI implements a role-based multi-agent workflow.

Project Manager Agent  
↓  
Technical Writer Agent  
↓  
Reviewer Agent


## Agent Responsibilities

| **Agent** | **Responsibility** |
| ----------------------- | ----------------------------------------------- |
| Project Manager | Analyze weekly updates and create report structure |
| Technical Writer | Generate a professional weekly report |
| Reviewer | Review and improve report quality |


## Runtime

9.60 seconds


## Output Analysis

### Strengths

- Successfully implemented sequential collaboration between role-based agents.
- Produced a highly structured weekly report with multiple professional sections.
- Clear separation between planning, writing, and reviewing responsibilities.
- Agent roles and task descriptions make the workflow easy to understand and maintain.


### Limitations

- The workflow relies on predefined task order and does not provide explicit graph-level control.
- Some generated information extends beyond the original input, such as inferred project impact and dependencies.
- Additional configuration is required to define agent roles and expected outputs.


## Quality Observation

The generated report achieved strong completeness and professional formatting.

Compared with AutoGen, CrewAI produced a richer report structure.
Compared with LangGraph, it showed similar completeness while generating fewer unsupported numerical details.

The result indicates that CrewAI is suitable for structured business workflows requiring clear role definitions and sequential collaboration.


## Metrics

| **Metric** | **Result**   |
| ----------------- |--------------|
| Runtime | 9.60 seconds |
| Output Token Consumption | 610 tokens   |
| Code Lines (LOC) | 173 lines    |
| Output Quality | 9.5/10       |

# 5. MetaGPT

## Architecture

MetaGPT implements a role-based multi-agent architecture using the Role and Action abstractions.

The workflow is composed of three specialized roles:

ProjectManager Role  
↓  
GenerateReportPlan Action  
↓  
TechnicalWriter Role  
↓  
WriteReport Action  
↓  
Reviewer Role  
↓  
ReviewReport Action


## Agent Responsibilities

| Role | Responsibility |
| ---------------- | ----------------------------------------------- |
| ProjectManager | Analyze weekly updates and generate a structured report plan |
| TechnicalWriter | Convert the plan into a professional weekly project report |
| Reviewer | Review and refine the generated report for clarity and quality |


## Runtime

8.62 seconds


## Output Analysis

### Strengths

- Generated a complete weekly project report with clear sections including Executive Summary, Completed Tasks, Issues and Risks, Next Steps, and Mitigation Plan.
- Successfully separated report generation into different role responsibilities, reflecting the role-based collaboration design of MetaGPT.
- Produced a concise and professional report format suitable for stakeholder communication.
- The reviewer stage improved the final report by refining wording and structure.


### Limitations

- The generated report still included some assumptions beyond the provided input.
- Information such as project status classification ("Amber") and potential impacts such as model deployment risks were inferred by the model rather than explicitly provided.
- Compared with graph-based workflows, the execution flow required more manual orchestration between roles in this implementation.
- Additional configuration adjustments were required to ensure compatibility between MetaGPT and the DeepSeek API.


## Quality Observation

The generated report demonstrated strong structure and professional writing quality.

The role-based workflow successfully simulated a project management process with planning, writing, and reviewing stages.

However, factual consistency remains a challenge because the model may introduce additional assumptions when the input information is limited.


## Metrics

| Metric | Result       |
| ----------------- |--------------|
| Runtime | 8.62 seconds |
| Output Token Consumption | 248 tokens   |
| Code Lines (LOC) | 259 lines    |
| Output Quality | 9.5/10       |

# 4. MetaGPT (Single-Agent)

## Architecture

MetaGPT Single-Agent implementation uses an Action-based architecture.

A single Action (`GenerateReportPlan`) is responsible for analyzing raw weekly updates and directly generating the final project report.

Workflow:

GenerateReportPlan Action

        ↓

LLM

        ↓

Weekly Project Report


## Agent Responsibilities

| Agent / Component | Responsibility |
| ---------------- | ----------------------------------------------- |
| GenerateReportPlan Action | Analyze weekly updates and generate a complete professional project report |


## Runtime

4.55 seconds


## Output Analysis

### Strengths

- Generated a complete weekly project report with clear sections including Executive Summary, Completed Tasks, Issues and Risks, Next Steps, and Risk Mitigation.
- Achieved the shortest execution time among the tested MetaGPT implementations due to the simplified single-action workflow.
- The generated report maintained a professional business writing style and provided actionable mitigation strategies.
- The implementation required fewer components and less orchestration compared with the role-based multi-agent version.


### Limitations

- The single-agent design lacks explicit role separation between planning, writing, and reviewing stages.
- The model directly generated the final report without intermediate validation or refinement steps.
- Similar to other frameworks, the output introduced additional assumptions beyond the original input, such as specific dates, technical details, and potential impacts.
- Compared with the multi-agent version, it provides less transparency regarding the reasoning process and task decomposition.


## Quality Observation

The Single-Agent MetaGPT implementation produced a well-structured and professional report with lower execution overhead.

However, because all responsibilities were handled by one Action, the workflow provides less modularity and controllability compared with the multi-agent implementation.


## Metrics

| Metric | Result       |
| ----------------- |--------------|
| Runtime | 4.55 seconds |
| Output Token Consumption | 545 tokens   |
| Code Lines (LOC) | 134 lines    |
| Output Quality | 9.5/10       |

# Overall Observations

## 1. Multi-Agent Collaboration Does Not Always Improve Quality

MetaGPT Multi-Agent and MetaGPT Single-Agent achieved the same quality score (9.5/10), suggesting that increasing the number of agents does not necessarily improve final output quality for relatively structured tasks.

## 2. Output Completeness and Factual Consistency Present a Trade-off

Frameworks producing richer reports may introduce additional assumptions beyond the provided input. LangGraph achieved high completeness but required stronger factual validation.

## 3. Single-Agent Workflow Provides Efficiency Advantages

MetaGPT Single-Agent achieved the shortest runtime and lowest implementation complexity while maintaining competitive output quality.