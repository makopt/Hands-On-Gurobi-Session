
# 🧠 Hands-On Gurobi Session — Setup Guide

Welcome to the **Hands-On Gurobi Session** repository! This repository contains materials to help you learn optimization modeling using the Gurobi Optimizer in Python.

To get the most out of this session, please complete the following setup tasks **before** the session begins.

---

## 📦 1. Clone this Repository

Clone or download this repository to your local machine:

```bash
git clone <repository-url>
```

Or download it as a ZIP file using the green "Code" button above.

---

## 🐍 2. Install Python

Make sure Python is installed (we recommend version **3.13.7**). Download it from the official website:

🔗 [Python Downloads](https://www.python.org/downloads/)  
☑️ *Choose the version that matches your operating system.*

---

## 🚀 3. Install Gurobi Optimizer

Download and install the latest version of **Gurobi Optimizer** (currently **v12.0.3**) from:

🔗 [Gurobi Optimizer Download](https://www.gurobi.com/downloads/gurobi-software/)  
☑️ *Make sure it matches your OS and Python version.*

---

## 🧩 4. Install the Gurobi Python Interface

After Gurobi is installed, open your terminal or command prompt and run:

```bash
pip install gurobipy
```

---

## 🔐 5. Activate Your Gurobi License

You need a valid license to run Gurobi. Choose one of the following:

- 🎓 **Academic License** (Unlimited usage)  
  🔗 [Gurobi Academic License](https://www.gurobi.com/academia/academic-program-and-licenses/)  
  > *You must register using your university email and activate your license when you are connected under the university domain.*

- 📘 **Learner License** (Limited to 2,000 variables and 2,000 constraints)  
  🔗 [Gurobi Learner License](https://www.gurobi.com/academia/for-online-courses/)
  > *You can activate your licence even if you are not connected to the university network.*

▶️ You can follow this video tutorial to activate your license:  
🎥 [How to Activate Gurobi License](https://www.youtube.com/watch?v=oW6ma8rdZk8)

---

## ⚙️ 6. Verify Your Installation

To confirm Gurobi is properly installed, open your terminal and run:

```bash
gurobi
```

---

## 🧪 7. Run the Test Script

- Navigate to the cloned repository folder.
- Open the script `gurobi_test.py` in your preferred code editor (e.g., VS Code, PyCharm, Jupyter).
- Run the script.

You should see output similar to the following:

```
Academic license - for non-commercial use only - expires 2026-03-26
...
Optimal solution found
x 1.0
y 0.0
z 1.0
Obj: 3.0
```

---

## 🧮 8. Repository Contents

This repository includes the following materials:

- 🎒 **Knapsack.ipynb** — Jupyter notebook for the Knapsack Problem
- 📦 **Binpacking.ipynb** — Jupyter notebook for the 1D Bin Packing Problem
- 🧪 **gurobi_test.py** — Test script to verify your Gurobi installation
- 📁 **kp_instances/** — Knapsack problem instance files for practice
- 🛠️ **kp_gen.py** — Generator script for knapsack problem instances

---

## 🧮 9. What We'll Cover in the Session

We’ll use Gurobi to solve two classic optimization problems in Python:

- 🎒 **Knapsack Problem** → `Knapsack.ipynb`
- 📦 **1D Bin Packing Problem** → `Binpacking.ipynb`

---

## 💻 10. Recommended IDE: Visual Studio Code

We'll use **Visual Studio Code** during the session.

- 🔗 [Download Visual Studio Code](https://code.visualstudio.com/download)
- 💡 Add the **Python extension** and **Jupyter extension** to run notebooks and scripts easily.

> VS Code is lightweight, user-friendly, and supports multiple programming languages through extensions.

---

✅ **Please complete all steps before the session begins** so we can focus on hands-on modeling and solving problems using Gurobi.

If you run into any issues, feel free to reach out for help.

---

## 📚 Additional Resources

- 📖 [Gurobi Documentation](https://www.gurobi.com/documentation/)
- 🎓 [Gurobi Examples](https://www.gurobi.com/documentation/current/examples/index.html)
- 💬 [Gurobi Community Forum](https://support.gurobi.com/hc/en-us/community/topics)

