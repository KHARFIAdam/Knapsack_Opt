# Knapsack Problem Solver 🚀

This repository contains a solution to the classic **Knapsack Problem** using various optimization techniques, including **Genetic Algorithm (GA)**, **Tabu Search**, and **Linear Programming** with a solver. The goal of this project is to efficiently solve the **0/1 Knapsack Problem** with different approaches to compare their performance and accuracy.

## Problem Overview 🎒

The **Knapsack Problem** involves selecting a subset of items with given weights and values to maximize the total value without exceeding a weight limit. This is a common problem in combinatorial optimization and has applications in areas like resource allocation, logistics, and more.

### Problem Definition:
- You have `n` items, each with a specific weight and value.
- You have a knapsack that can carry a maximum weight, `W`.
- The goal is to find the subset of items that maximizes the total value without exceeding the weight limit.

Formally:

$$ \text{Maximize} \quad \sum_{i=1}^{n} v_i x_i $$
$$ \text{Subject to} \quad \sum_{i=1}^{n} w_i x_i \leq W $$
Where:
- \(v_i\) = value of item i
- \(w_i\) = weight of item i
- \(x_i\) = binary decision variable (1 if item i is selected, 0 otherwise)
- \(W\) = maximum weight capacity of the knapsack

---

## Optimization Techniques Used 🧠

This project applies three distinct methods to solve the Knapsack Problem:

### 1. **Genetic Algorithm (GA)** 🧬

Genetic algorithms are inspired by natural selection and use a population-based approach. In this implementation:
- Solutions are encoded as binary strings.
- Parents are selected based on their fitness (total value), and offspring are created through crossover and mutation.
- The best individuals are chosen for the next generation.

### 2. **Tabu Search** 🔄

Tabu Search is a local search algorithm that enhances the performance of simple neighborhood search methods by using memory structures (tabu lists) to avoid revisiting previous solutions. The algorithm:
- Starts with an initial solution and explores the neighborhood iteratively.
- Avoids cycling by keeping track of recent moves using a Tabu list.

### 3. **Linear Programming with Solver** 📊

Linear programming (LP) is used to solve the problem as a series of linear equations and inequalities. This method is implemented with a solver to find the optimal solution by:
- Defining decision variables, objective function, and constraints.
- Using the **Simplex Method** or another LP solver to find the optimal solution efficiently.

---

## Installation 🔧

To run this project locally, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/knapsack-optimization.git
   cd knapsack-optimization