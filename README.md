# 📊 Nifty 50 Historical Dashboard

![Tech](https://img.shields.io/badge/stack-HTML%20%7C%20Tailwind%20%7C%20Python-blue)


A modern, interactive dashboard to visualize **20 years of Nifty 50 performance** with a clean **Neumorphism (Soft UI)** design.

---

## 🚀 Demo

> Run locally (instructions below)

---

## ✨ Features

* 📈 Interactive **ApexCharts** line graph
* 🔍 Zoom & pan support
* 📅 Predefined + custom date ranges
* 📊 Data granularity (Daily / Weekly / Monthly)
* 📌 Key metrics:

  * Current Value
  * CAGR
  * Period High / Low
  * Year-to-Date Change
* 📥 Export data as CSV
* 🎨 Neumorphism UI + smooth animations

---

## 🖼️ Preview

*Add screenshots here (recommended for GitHub visibility)*

---

## 🏗️ Tech Stack

| Layer    | Technology                    |
| -------- | ----------------------------- |
| Frontend | HTML, Tailwind CSS, Bootstrap |
| Charts   | ApexCharts                    |
| Backend  | Python                        |
| Data     | yfinance                      |

---

## 📂 Project Structure

```
project/
│
├── index.html
├── nifty50_data.json
├── fetch_data.py
└── README.md
```

---

## ⚙️ Installation & Setup



### 2️⃣ Install Dependencies

```
pip install yfinance
```

---

### 3️⃣ Fetch Historical Data

```
python fetch_data.py
```

This will generate:

```
nifty50_data.json
```

---

### 4️⃣ Run the Project

⚠️ Do NOT open `index.html` directly.

Start a local server:

```
python -m http.server 8000
```

Open in browser:

```
http://localhost:8000
```

---

## ⚠️ Important Notes

* Data is **static after fetching**
* Requires internet for initial data download
* Best viewed on modern browsers

---

## 🚀 Future Improvements

* 🔴 Live market data integration
* 📊 Multi-index comparison (Sensex, Bank Nifty)
* 🤖 AI-based insights
* 📉 Drawdown & volatility metrics
* 📅 Event overlays (COVID crash, elections)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shivansh Agarwal**

---

⭐ If you like this project, give it a star!
