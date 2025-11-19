# 🤖 IASA – Autonomous Agent with Planning and Sequential Decision-Making

> Project for the course **Inteligência Artificial para Sistemas Autónomos (IASA)**  
> BSc in Computer Engineering and Multimedia – **ISEL**  
> Academic year **2024 / 2025**

---

## 👤 Author

- **Name:** Miguel Cordeiro  
- **Student Number:** 49765  
- **Instructor:** Luís Morgado  

---

## 📝 Project Description

This repository contains the work developed for the course **Inteligência Artificial para Sistemas Autónomos (IASA)**, focused on the study and implementation of **autonomous agents** with capabilities for **decision-making, reasoning and learning**, complemented with good **Software Engineering** practices.

Across four stages, the project evolves from a purely reactive agent to a deliberative agent capable of **planning, evaluating options** and **making sequential decisions under uncertainty**, integrating concepts such as:

- **reactive**, **deliberative** and **hybrid** architectures  
- **state-space search** (including A* and Uniform Cost Search)  
- **Markov Decision Processes (MDP)**  
- basic notions of **reinforcement learning** and reward-based decision-making  

The final result is an agent that **perceives**, **deliberates**, **plans** and **acts** in a simulated environment, following a modular and extensible architecture.

---

## 🎯 Learning Objectives

- Implement and compare different **agent architectures** (reactive vs deliberative).  
- Apply **Software Engineering** techniques:  
  - abstraction, modularization and factorization  
  - use of UML diagrams as a basis for implementation  
  - low coupling and high cohesion  
- Explore **search techniques**:
  - uninformed search (breadth-first, depth-first, depth-limited, iterative deepening)  
  - informed search (heuristics, cost, A*, uniform-cost, greedy)  
- Build agents with:
  - **hierarchical reactive behaviours**, with or without memory  
  - **automatic planning** in state space  
  - **sequential decision-making** with Markov Decision Processes  

---

## 🎥 Project Demo

[![Click the image to watch the video demo](media/thumb_demo.png)](https://youtu.be/_BO9eytQb0c "Watch on YouTube")

> 👉 **Click the image above** to watch the full demonstration of the agent in action on YouTube.

---

## 🧠 High-Level Architecture Overview

At an abstract level, the agent follows the classic perception–decision–action loop:

```mermaid
flowchart LR
    P[Perception] --> C[Control]
    C --> A[Action]
    A --> E[Environment]
    E --> P
