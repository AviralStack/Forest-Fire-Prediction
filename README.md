# 🔥 Global Forest Fire Risk Predictor (Phase 2)

### 📌 Project Overview
This project predicts the **probability (%)** of forest fires based on the global **FWI (Fire Weather Index)** system.
Unlike simple "Yes/No" classifiers, this model uses **Logistic Regression** to calculate a precise risk score (e.g., "87% Risk") based on weather conditions (Temperature, Humidity, Wind) and Fuel Moisture Indices.

It is deployed as a user-friendly web application using **Streamlit**, featuring a dynamic "Probability Gauge" and color-coded risk levels.

👉 **[Click here to view the Live App](https://forest-fire-prediction-dzcsdunsblancljwkhxca3.streamlit.app/)**

---

### 📊 The Dataset
The model was trained on the **Algerian Forest Fires dataset**, which includes 244 instances from two distinct regions (Bejaia and Sidi-Bel Abbes). However, the logic relies on standard **FWI components**, making the physics applicable to forests globally.

* **Weather Data:** Temperature, RH (Relative Humidity), Ws (Wind Speed), Rain.
* **FWI Components:** FFMC (Fine Fuel Moisture Code), DMC (Duff Moisture Code), ISI (Initial Spread Index).
* **Target:** `Classes` (Fire / Not Fire).

---

### 🛠️ Technical Approach & Pipeline

#### 1. Data Cleaning & EDA
The dataset required significant preprocessing before training:
* **Header Correction:** Handled the "hidden header" row found in the middle of the dataset merging the two regions.
* **Label Fixing:** Cleaned the target column `Classes` which contained extra spaces (e.g., `"fire   "` vs `"fire"`).
* **Outlier Analysis:** Visualized outliers but retained them, as extreme weather conditions are often the exact cause of forest fires.

#### 2. Feature Selection (Handling Multicollinearity)
During EDA, high multicollinearity was detected between the Fire Weather Indices.
* **Problem:** `BUI`, `DC`, and `FWI` were highly correlated (>0.9) with `DMC` and `ISI`.
* **Solution:** Dropped `['BUI', 'DC', 'FWI']` to reduce noise and prevent overfitting, while retaining the core signal in `DMC` (Fuel Moisture) and `ISI` (Spread Potential).

#### 3. Model Upgrade (Phase 2)
In Phase 1, I used **ElasticNet Regression**. In Phase 2, I upgraded to **Logistic Regression** to utilize the **Sigmoid Function**.
* **Why?** To map raw model scores into a strict **0-100% Probability** curve.
* **The Tipping Point:** The model successfully learned that high FFMC (Dryness) alone is not enough; it requires high ISI (Wind/Spread) to trigger a >90% probability alert.

#### 4. Model Performance
The Phase 2 model achieved world-class metrics on the test set:

| Metric | Score | Notes |
| :--- | :--- | :--- |
| **Accuracy** | **97.26%** | Outperformed previous ElasticNet model. |
| **F1-Score** | **0.9773** | Perfect balance between Precision and Recall. |
| **Precision** | **97.73%** | Very low False Positive rate. |
| **Recall** | **97.73%** | Captures almost every actual fire event. |

---

### 🚀 How to Run Locally

If you want to run this app on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AviralStack/Forest-Fire-Prediction.git
    cd Forest-Fire-Prediction
    ```

2.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---

### 💻 Tech Stack
* **Language:** Python 3.x
* **Libraries:** Scikit-learn, Pandas, Numpy, Matplotlib, Seaborn
* **Deployment:** Streamlit Cloud
* **Version Control:** Git (Branching strategy: `main` vs `v2-logistic`)

---

### 👨‍💻 Author
**Aviral Gupta**
* [GitHub](https://github.com/AviralStack)
* [Linkdin](https://www.linkedin.com/in/aviral-gupta-2208b0330/)