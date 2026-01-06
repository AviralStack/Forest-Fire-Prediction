# 🔥 Algerian Forest Fire Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/YOUR_USERNAME/YOUR_REPO_NAME)

## 📌 Project Overview
This project predicts the occurrence of forest fires in Algeria using weather data (Temperature, Humidity, Wind Speed, etc.) and Fire Weather Indices (FWI).

The model solves a **Binary Classification** problem (Fire vs. Not Fire) with an accuracy of **~96%**. It is deployed as a user-friendly web application using **Streamlit**.

👉 **[Click here to view the Live App](https://forest-fire-prediction-e2cyy56rxe6nwqjkhlub4u.streamlit.app/)**

---

## 📊 The Dataset
The dataset includes 244 instances from two regions in Algeria: **Bejaia** and **Sidi-Bel Abbes**.

**Key Features:**
* **Weather Data:** Temperature, RH (Relative Humidity), Ws (Wind Speed), Rain.
* **FWI Components:** FFMC, DMC, DC, ISI, BUI, FWI.
* **Target:** `Classes` (Fire / Not Fire).

---

## 🛠️ Technical Approach & Pipeline

### 1. Data Cleaning & EDA
The dataset required significant preprocessing:
* **Header Correction:** Handled the "hidden header" row found in the middle of the dataset merging the two regions.
* **Label Fixing:** Cleaned the target column `Classes` which contained extra spaces (e.g., `"fire   "` vs `"fire"`).
* **Outlier Analysis:** Visualized outliers but retained them, as extreme weather conditions are often the exact cause of forest fires.

### 2. Feature Selection (Handling Multicollinearity)
During EDA, I discovered high multicollinearity between the Fire Weather Indices.
* **Problem:** `BUI`, `DC`, and `FWI` were highly correlated (>0.9) with `DMC` and `ISI`.
* **Solution:** Dropped `['BUI', 'DC', 'FWI']` to reduce noise and prevent overfitting, while retaining the core signal in `DMC` and `ISI`.

### 3. Model Training & Comparison
I experimented with multiple regression techniques to predict the fire risk score, then thresholded the result for classification.

| Model | Performance Notes |
| :--- | :--- |
| **Linear Regression** | Good baseline ($R^2 \approx 0.66$), but prone to overfitting. |
| **Lasso Regression** | Initially underperformed (negative $R^2$) due to aggressive feature penalization, proving some complexity was needed. |
| **Ridge Regression** | Performed well ($R^2 \approx 0.66$), providing better stability than Linear Regression. |
| **ElasticNet (Winner)** | **Selected Final Model.** It combined the best of Ridge (stability) and Lasso (feature selection), achieving **~96% Accuracy** on test data. |

---

## 🚀 How to Run Locally

If you want to run this app on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AviralStack/Forest-Fire-Prediction.git 
    cd Algerian Forest Fires
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

## 💻 Tech Stack
* **Language:** Python
* **Libraries:** Scikit-learn, Pandas, Numpy, Matplotlib, Seaborn
* **Deployment:** Streamlit Cloud

## 👨‍💻 Author
**[Aviral Gupta]**
* [LinkedIn](https://www.linkedin.com/in/aviral-gupta-2208b0330/)
* [GitHub](https://github.com/AviralStack)