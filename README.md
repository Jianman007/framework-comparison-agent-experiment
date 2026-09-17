# Framework Comparison Experiment

A comparative experiment on several **LLM agent frameworks** for **automated weekly project report generation**.

> This project investigates how different agent frameworks perform on the **same real-world automation task**, and compares them from the perspectives of **runtime**, **token consumption**, **implementation complexity**, and **output quality**.

---

## Overview

This experiment compares the following frameworks:

- **LangGraph**
- **AutoGen**
- **CrewAI**
- **MetaGPT (Single-Agent)**
- **MetaGPT (Multi-Agent)**

All frameworks are tested on the same task:

> **Generate a professional weekly project report from raw project updates.**

---

## Results Snapshot

| Framework | Runtime (s) | Token Consumption | Code Lines (LOC) | Output Quality |
|---|---:|---:|---:|---:|
| LangGraph | 12.19 | 864 | 187 | 9.0 / 10 |
| AutoGen | 8.66 | 444 | 170 | 8.5 / 10 |
| CrewAI | TBD | 610 | TBD | 9.5 / 10 |
| MetaGPT Single-Agent | 4.55 | 545 | 134 | 9.5 / 10 |
| MetaGPT Multi-Agent | TBD | 248 | 259 | 9.5 / 10 |

> **Observation:**  
> - **LangGraph** produced a highly structured report, but consumed the most tokens.  
> - **AutoGen** used fewer tokens and had relatively low implementation complexity, but its output contained more placeholders.  
> - **CrewAI** produced strong report quality with a clear role-based collaboration style.  
> - **MetaGPT Single-Agent** was simple and efficient.  
> - **MetaGPT Multi-Agent** achieved high quality with the **lowest token usage** among the evaluated frameworks.

---

## Objective

This project explores how different agent frameworks behave when solving the **same automation problem**.

The selected task is:

> **Generate a structured weekly project report from raw weekly updates.**

The goal is not only to compare whether the frameworks can complete the task, but also to observe:

- how they organize the workflow,
- how much code is needed,
- how many tokens they consume,
- and how strong the final report quality is.

---

## Experiment Task

### Input

Raw weekly project updates containing:

- completed tasks,
- current issues,
- next steps.

### Example Input

```text
Completed:
- Finished data preprocessing

Issues:
- API timeout problem

Next:
- Improve model performance
