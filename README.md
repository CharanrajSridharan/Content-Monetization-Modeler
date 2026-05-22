# 🎬 YouTube Ad Revenue Predictor

A machine learning project that predicts YouTube ad revenue based on video performance metrics. Built with Python, Scikit-learn, and Streamlit.

---

## 📌 Project Overview

This project analyzes a dataset of 122,400 YouTube video records and builds a regression model to predict ad revenue in USD. The final model is deployed as an interactive web application using Streamlit.

---

## 🗂️ Project Structure

```
Content Monetization Modeler/
│
├── content_monetization_modeler.ipynb   # Main Jupyter Notebook (EDA + ML)
├── app.py                               # Streamlit Web Application
├── best_model.pkl                       # Saved Ridge Regression Model
├── model_columns.pkl                    # Saved Column Names
├── youtube_ad_revenue_dataset.csv       # Dataset
└── README.md                            # Project Documentation
```

---

## 📊 Dataset

| Property | Detail |
|---|---|
| Total Records | 122,400 rows |
| Features | 12 columns |
| Target Variable | `ad_revenue_usd` |
| Missing Values | ~5% in likes, comments, watch_time |
| Duplicate Rows | ~2% (2,400 rows) |

### Features

| Column | Type | Description |
|---|---|---|
| video_id | Text | Unique video identifier |
| date | DateTime | Upload date |
| views | Integer | Total video views |
| likes | Float | Number of likes |
| comments | Float | Number of comments |
| watch_time_minutes | Float | Total watch time |
| video_length_minutes | Float | Duration of video |
| subscribers | Integer | Channel subscribers |
| category | Text | Video category (6 types) |
| device | Text | Viewing device (4 types) |
| country | Text | Viewer country (6 countries) |
| ad_revenue_usd | Float | **Target Variable** |

---

## 🔍 Exploratory Data Analysis (EDA)

Key findings from the dataset:

- **watch_time_minutes** has a 0.99 correlation with ad revenue — the strongest predictor
- **views, subscribers, video_length** have near-zero correlation with revenue
- All categories, devices, and countries are balanced (~equal distribution)
- Ad revenue ranges from **$126 to $382** with a uniform distribution

### Correlation with Ad Revenue

| Feature | Correlation |
|---|---|
| watch_time_minutes | **0.989** 🔥 |
| likes | 0.146 |
| views | 0.038 |
| comments | 0.034 |
| subscribers | 0.006 |
| video_length_minutes | -0.000 |

---

## 🛠️ Data Preprocessing

1. **Removed duplicates** → 122,400 → 120,000 rows
2. **Filled missing values** with median (likes, comments, watch_time_minutes)
3. **Feature engineering** → created `engagement_rate = (likes + comments) / views`
4. **Dropped useless columns** → removed `video_id` and `date`
5. **One-hot encoding** → encoded category, device, country
6. **Train/test split** → 80% train (96,000 rows), 20% test (24,000 rows)

---

## 🤖 Models Trained & Results

| Model | R² Score | RMSE | MAE |
|---|---|---|---|
| **Ridge Regression** 🏆 | **0.9526** | **13.4798** | **3.1071** |
| Linear Regression | 0.9526 | 13.4806 | 3.1119 |
| Gradient Boosting | 0.9523 | 13.5249 | 3.6163 |
| Decision Tree | 0.9499 | 13.8542 | 4.2311 |
| Random Forest | 0.9499 | 13.8563 | 3.5872 |

**Best Model: Ridge Regression**
- R² = 0.9526 (explains 95.26% of variance)
- Average error of only ~$3.11 (MAE)

---

## 🚀 Streamlit Web App

The app allows users to input video stats and get an instant ad revenue prediction.

### How to Run

```bash
# Install dependencies
pip install streamlit scikit-learn pandas

# Run the app
streamlit run app.py
```

### App Features
- Input fields for all video metrics
- Dropdown menus for category, device, and country
- Instant revenue prediction on button click
- Displays engagement rate and model info

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/content-monetization-modeler.git

# Navigate to project folder
cd content-monetization-modeler

# Install required libraries
pip install pandas numpy matplotlib seaborn scikit-learn streamlit

# Launch the notebook
jupyter notebook content_monetization_modeler.ipynb

# Or run the web app
streamlit run app.py
```

---

## 🧰 Technologies Used

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| Matplotlib / Seaborn | Data visualization |
| Scikit-learn | Machine learning models |
| Streamlit | Web application |
| Jupyter Notebook | Analysis & documentation |

---

## 📈 Key Learnings

- Watch time is by far the most important predictor of YouTube ad revenue
- Simple linear models can outperform complex ones when data has strong linear relationships
- Feature engineering (engagement_rate) adds meaningful context to the model
- Balanced datasets make ML models more reliable and fair

---

## 👤 Author

**Charanraj Sridharan**  
