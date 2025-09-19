# Sewage Network Simplification Automator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Libraries](https://img.shields.io/badge/libraries-pandas%20%7C%20networkx%20%7C%20matplotlib-orange.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A Python script designed to automate the simplification of sewage pipe network data by intelligently identifying and filtering non-critical manholes, directly addressing a common workflow bottleneck for hydraulic engineers.

---

##  The Problem

Engineers working with hydraulic modeling software like **Bentley's SewerCAD** often receive complex network data from clients in formats like CSV. A common, time-consuming task is the manual pre-processing of this data to remove "unnecessary" manholes—those that serve as simple pass-throughs and are not critical intersections or endpoints. This manual process is repetitive, prone to error, and can take hours, slowing down the critical path to analysis and modeling.

##  The Solution

This script automates this simplification process entirely. It ingests raw pipe and manhole data, models the system as a graph, and applies a set of rules to programmatically identify and filter out non-critical manholes. The final output is a visually and structurally simplified network that retains its essential geometric and topological integrity, ready for engineering analysis.

This project was developed to directly support the lead engineer's workflow, transforming a manual, multi-hour task into an automated process that runs in seconds.

---

##  Key Features

* **Intelligent Simplification:** Uses graph theory (via `networkx`) to analyze node degrees, accurately identifying critical manholes (intersections, endpoints) versus non-critical ones (pass-throughs).
* **Geometric Preservation:** The simplification is purely visual for the manholes; the original, precise geometry and curvature of the pipe network are perfectly preserved in the final plot.
* **Configurable Sampling:** For long, straight, or curved sections, the script keeps one manhole every four nodes to ensure the path is still represented without overwhelming the visual.
* **Handles Disconnected Networks:** The algorithm processes all disconnected sub-graphs ("connected components") independently, ensuring that the entire area of interest is simplified, not just the largest single network.
* **Dual Output:** Generates both a visually simplified `.png` plot for quick assessment and a cleaned `simplified_manholes.csv` file for direct use in other software.

---

##  Technology Stack

* **Python 3.8+**
* **Pandas:** For data manipulation and handling of CSV files.
* **NetworkX:** For graph creation, analysis, and topological calculations.
* **Matplotlib:** For generating high-quality visualizations of the original and simplified networks.

---

##  Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    A `requirements.txt` file is included for easy setup.
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, create one and add these lines:)*
    ```
    pandas
    networkx
    matplotlib
    ```

---

##  Usage

1.  **Place your data files** in the root directory of the project. The script is currently configured to look for:
    * `ofakim pipe data 01.csv`
    * `ofakim MH data 01.csv`

2.  **Configure Paths:** Open `main.py` and update the file paths at the top of the `main()` function if your files are named differently or located elsewhere.

3.  **Run the script:**
    ```bash
    python main.py
    ```
    The script will print its progress to the console and save the output files in the configured directory.

---

##  Output Showcase

The script generates two key visual outputs and one data output.

1.  **`original_network.png`**: A plot of the full, unprocessed network.
2.  **`simplified_network.png`**: The same network with the original pipe geometry but only displaying the critical and sampled manholes.
3.  **`simplified_manholes.csv`**: A CSV file containing the data for only the manholes that were kept.

*(Note: You will need to add your own images to the repository for them to display here. I recommend creating an `assets` folder.)*

| Original Network                                   | Simplified Network                               |
| -------------------------------------------------- | ------------------------------------------------ |
| ![Original Network](path/to/your/original_network.png) | ![Simplified Network](path/to/your/simplified_network.png) |
| **5796** Manholes Displayed                        | **1350** Manholes Displayed (77% Reduction)      |

##  Original Grid


<img width="5964" height="4768" alt="original_network" src="https://github.com/user-attachments/assets/af7d82dd-f438-435d-9368-115fdb6d68b4" />

##  New Grid


<img width="5964" height="4768" alt="simplified_network" src="https://github.com/user-attachments/assets/e019a1a5-8067-44cb-a84f-9f7a60e80bbc" />

