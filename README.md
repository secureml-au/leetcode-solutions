<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=LeetCode%20Solutions&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=by%20Au%20%E2%80%94%20Systematic.%20Clean.%20Deliberate.&descAlignY=60&descSize=18" width="100%"/>
<img width="1297" height="307" alt="Image" src="https://github.com/user-attachments/assets/d166c39e-c5b6-4ca0-b526-5b5a1c8dcb9a" />

<!-- Badges -->
[![LeetCode](https://img.shields.io/badge/LeetCode-auamores-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/auamores/)
[![Language](https://img.shields.io/badge/Primary-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JS](https://img.shields.io/badge/Also-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)](https://github.com/secureml-au/leetcode-solutions)
[![License](https://img.shields.io/badge/License-MIT-8b5cf6?style=for-the-badge)](./LICENSE)

<br/>

> *"Understand the problem. Respect the constraints. Write it clean."*

</div>

---

## About This Repo

Personal archive of LeetCode solutions — synced via **LeetSync**, written for **clarity over cleverness**.

Each solution prioritizes:
- Readable logic over micro-optimizations
- Sound complexity tradeoffs (always stated)
- Pattern-driven thinking, not brute force

**Primary Language:** Python | **Secondary:** JavaScript | **DB:** SQL

---

## LeetCode Stats

<div align="center">

[![LeetCode Stats](https://leetcard.jacoblin.cool/auamores?theme=dark&font=Nunito&ext=heatmap)](https://leetcode.com/u/auamores/)

</div>

---

## Approach

| Principle | Practice |
|-----------|----------|
| **Understand first** | Map constraints and edge cases before writing a single line |
| **Complexity first** | Always define O(n) time/space before implementation |
| **Pattern recognition** | Solutions grouped by technique, not problem number |
| **Clean code** | No magic numbers. Meaningful names. Zero ambiguity. |
| **Security mindset** | Inputs treated as untrusted — always validate, never assume |

---

## Topics Covered

```
leetcode-solutions/
├── Arrays & Hashing
├── Two Pointers / Sliding Window
├── Binary Search
├── Linked Lists
├── Trees & BST
├── Graphs (BFS / DFS / Dijkstra)
├── Dynamic Programming
├── Backtracking
├── Math & Bit Manipulation
├── Stack & Queue
└── SQL / Database Problems
```

---

## Difficulty Breakdown

<div align="center">

![Easy](https://img.shields.io/badge/Easy-pass-22c55e?style=flat-square&labelColor=1a1a1a)
![Medium](https://img.shields.io/badge/Medium-pass-f59e0b?style=flat-square&labelColor=1a1a1a)
![Hard](https://img.shields.io/badge/Hard-pass-ef4444?style=flat-square&labelColor=1a1a1a)

</div>

---

## Featured Solutions

| # | Problem | Difficulty | Topic | Language |
|---|---------|------------|-------|----------|
| 51 | [N-Queens](./51-n-queens/) | Hard | Backtracking | Python |
| 76 | [Minimum Window Substring](./76-minimum-window-substring/) | Hard | Sliding Window | Python |
| 84 | [Largest Rectangle in Histogram](./84-largest-rectangle-in-histogram/) | Hard | Stack | Python |
| 303 | [Range Sum Query - Immutable](./303-range-sum-query-immutable/) | Easy | Prefix Sum | Python |
| 744 | [Network Delay Time](./744-network-delay-time/) | Medium | Graphs / Dijkstra | Python |
| 803 | [Cheapest Flights within K Stops](./803-cheapest-flights-within-k-stops/) | Medium | Graphs / Bellman-Ford | Python |
| 1456 | [Find the City with Smallest Neighbors](./1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | Graphs / Floyd-Warshall | Python |

---

## SQL Coverage

Heavy coverage on LeetCode SQL problems — JOIN strategies, window functions, subqueries, aggregations.

```sql
-- Sample pattern: Window Function approach
SELECT name,
 RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
FROM employees;
```

Topics: `GROUP BY` · `HAVING` · `JOIN` types · `CTE` · `CASE WHEN` · `Window Functions` · `Subqueries`

---

## Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![MySQL](https://img.shields.io/badge/MySQL-SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![LeetSync](https://img.shields.io/badge/Sync-LeetSync-FFA116?style=flat-square&logo=leetcode&logoColor=white)

</div>

---

## About the Author

<div align="center">

**Au** — AI/ML Engineer · Computer Vision · Secure Systems · Philippines 

*Building with a focus on structure, scalability, and security.*

[![Portfolio](https://img.shields.io/badge/Portfolio-au--dev--cs-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://au-dev-cs.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-au--amores-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/au-amores)
[![GitHub](https://img.shields.io/badge/GitHub-secureml--au-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/secureml-au)
[![LeetCode](https://img.shields.io/badge/LeetCode-auamores-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/auamores/)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

*This repo is a working document, not a showcase. Expect ongoing commits.*

</div>
