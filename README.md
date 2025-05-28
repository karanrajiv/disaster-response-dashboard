# 🌐 Real-Time Disaster Response Dashboard

This project is a prototype of a real-time disaster response dashboard built with Streamlit and Plotly. It visualizes critical information like disaster event locations, types, and frequencies to help authorities and responders make quick, informed decisions during emergencies.

## 🚀 Features

- Interactive map of disaster events using latitude/longitude.
- Filters by disaster type.
- Summary statistics and histograms of event frequency.
- Built with Python, Streamlit, and Plotly.

## 🗂️ Folder Structure

```
disaster-response-dashboard/
├── dashboard_app/         # Application logic
├── data/                  # Sample data file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/disaster-response-dashboard.git
cd disaster-response-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the dashboard

```bash
streamlit run dashboard_app/app.py
```

## 📊 Sample Data

The data file (`data/sample_data.csv`) includes synthetic records for demonstration. You can replace this file with live data from APIs like GDACS, ReliefWeb, or your own data sources.

## 🤝 Contributing

We welcome contributions! Please open issues for bugs or feature requests.

## 📜 License

This project is open-source and licensed under the MIT License.