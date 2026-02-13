
# 🧠 Hands-On Gurobi Session — Preparation Instructions

To get the most out of our upcoming **Hands-On Gurobi Session** on **Sunday, September 21, 2025**, please complete the following setup tasks **before** the session.

---

## 📦 1. Download the Working Folder

Download the materials (ZIP format) from the link below and extract them to a convenient location on your computer:

🔗 [Knapsack Working Folder](https://drive.google.com/file/d/1sk8Z6tt-4rqsnauisxEIPt4tTH0PstDx/view?usp=sharing)

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

- Unzip the working folder.
- Open the script `test_gurobi.py` in your preferred code editor (e.g., VS Code, PyCharm, Jupyter).
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

## 🧮 8. What We'll Cover in the Session

We’ll use Gurobi to solve two classic optimization problems in Python:

- 🎒 **Knapsack Problem** → `Knapsack.ipynb`
- 📦 **1D Bin Packing Problem** → `Binpacking.ipynb`

---

## 💻 9. Recommended IDE: Visual Studio Code

We'll use **Visual Studio Code** during the session.

- 🔗 [Download Visual Studio Code](https://code.visualstudio.com/download)
- 💡 Add the **Python extension** and **Jupyter extension** to run notebooks and scripts easily.

> VS Code is lightweight, user-friendly, and supports multiple programming languages through extensions.

---

✅ **Please complete all steps before the session begins** so we can focus on hands-on modeling and solving problems using Gurobi.

If you run into any issues, feel free to contact us ahead of time.
