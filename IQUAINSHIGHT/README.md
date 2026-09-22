# 💧 AquaInsights
**Every Drop. Every Insight. Every Decision.**

![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

AquaInsights is an enterprise-grade Water Quality Analytics Platform built with Python and Streamlit. Designed with modern commercial SaaS UI/UX standards, it enables users to analyze water quality datasets, inspect WHO compliance parameters, execute predictive Machine Learning models for potability, generate automated AI insights, and produce downloadable executive PDF/CSV reports.

---

## 🎨 Design System & Palette

- **Background:** `#F8FAFC`
- **Sidebar:** `#14213D`
- **Primary Blue:** `#1E88E5`
- **Secondary Blue:** `#42A5F5`
- **Highlight / Amber:** `#FCA311`
- **Cards:** `#FFFFFF`
- **Typography:** Inter, Poppins

---

## ✨ Application Navigation & Modules

1. **📊 Dashboard:** High-resolution analytics workspace matching reference specifications with KPI metrics, key parameter indicators, Plotly donut distribution chart, WHO standards compliance, AI quick insights, pH trend chart, parameter correlation heatmap, and recent dataset summary.
2. **📋 Dataset Overview:** Drag-and-drop CSV/XLSX uploader, sample dataset switcher, summary metrics, and full tabular data preview.
3. **🧹 Data Cleaning:** Dataset health score gauge, missing values imputation, duplicate row removal, inconsistency tracking, and outlier detection.
4. **💧 Water Parameters:** Interactive parameter grid (pH, Hardness, TDS, Turbidity, Conductivity, Chloramines, Sulfate, Organic Carbon) with detailed single-parameter explorer deep dive.
5. **📈 Analytics:** Summary statistics matrix (mean, median, variance, range) and correlation heatmap.
6. **📉 Visualizations:** Gallery featuring 6 interactive charts across 5 categories (Distribution, Relationship, Trend, Comparison, All Charts).
7. **✨ AI Insights:** Automated insights list, key findings extraction, and AI-powered natural language chat interface.
8. **🎯 Prediction:** Machine Learning inference engine form to predict water potability with confidence scoring.
9. **📄 Report Generator:** Customizable PDF document generator powered by ReportLab and CSV exporter.
10. **⚙️ Settings:** Appearance mode, language selection, threshold configuration, and preference saving.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Core Framework** | Python 3.12+, Streamlit |
| **Navigation & Extras** | `streamlit-option-menu`, `streamlit-extras` |
| **Data Processing** | Pandas, NumPy |
| **Data Visualization** | Plotly Express, Plotly Graph Objects, Matplotlib |
| **Machine Learning** | Scikit-Learn |
| **Document Generation** | ReportLab, OpenPyXL |
| **Image & Asset Processing** | Pillow (PIL) |

---

## 📁 Project Structure

```
AquaInsights/
│
├── app.py                     # Main application entry point
├── requirements.txt           # Project dependencies
├── README.md                  # Comprehensive documentation
│
├── assets/                    # Static assets & media
│   ├── logo/
│   ├── icons/
│   └── images/
│
├── components/                # Reusable UI components
│   ├── __init__.py
│   ├── sidebar.py             # Custom navy sidebar & navigation menu
│   ├── navbar.py              # Top bar with user profile & search UI
│   ├── footer.py              # Application footer
│   ├── metric_card.py         # Reusable metric card component
│   ├── chart_card.py          # Reusable chart wrapper card
│   ├── parameter_card.py      # Water quality parameter card
│   └── ai_card.py             # AI insight card component
│
├── pages/                     # Application pages
│   ├── __init__.py
│   ├── dashboard.py           # High-resolution dashboard page
│   ├── dataset.py             # Dataset upload & tabular preview
│   ├── cleaning.py            # Data health & cleaning tools
│   ├── parameters.py         # Water parameter overview & explorer
│   ├── analytics.py           # Statistical summary & correlations
│   ├── visualizations.py      # Visualizations gallery
│   ├── insights.py            # AI insights & data assistant
│   ├── prediction.py          # ML potability prediction model
│   ├── reports.py             # Executive PDF report generator
│   └── settings.py            # User preferences & configuration
│
├── services/                  # Business logic & engine services
│   ├── __init__.py
│   ├── csv_loader.py          # File loader & dataset state manager
│   ├── validator.py           # Dataset validator & health scoring
│   ├── analytics_engine.py    # Statistical & WHO compliance engine
│   ├── prediction_engine.py   # Machine Learning prediction engine
│   ├── ai_engine.py           # AI insight generator & data chat
│   └── report_engine.py       # PDF document & CSV export engine
│
├── utils/                     # Core design system & helper utilities
│   ├── __init__.py
│   ├── colors.py              # Centralized color tokens
│   ├── theme.py               # Application-wide CSS injection
│   ├── constants.py           # Global constants & page config
│   └── helpers.py             # General helper functions
│
├── datasets/                  # Datasets storage
│   └── water_quality_2024.csv # Default sample dataset (5,274 samples)
├── exports/                   # Exported reports output folder
└── models/                    # Trained Machine Learning models
```

---

## 🚀 Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AquaInsights.git
   cd AquaInsights
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Run Instructions

Run the Streamlit app:
```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## 📄 License
This project is licensed under the MIT License.

© 2026 AquaInsights. Every Drop. Every Insight. Every Decision.
