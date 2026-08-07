<div align="center">

# 🚗 Commute Economics Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-10%20Passing-22c55e?style=for-the-badge&logo=pytest&logoColor=white)
![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-A51C30?style=for-the-badge)

**A command-line tool that calculates the true, hidden cost of your daily commute in Pakistan — pulling live exchange rate data to estimate petrol prices and comparing every vehicle in its database against your exact route.**

</div>

---

## 📌 Key Features

- 📡 **Live price estimation** — Fetches the real-time USD/PKR exchange rate from a free API and converts it to an estimated petrol price, no API key required
- ⛽ **Manual price override** — Enter the exact OGRA-notified price for perfectly accurate results
- 🚗 **Editable vehicle database** — 10 Pakistan-common vehicles in a plain CSV; add any vehicle by adding one row, no code changes needed
- 📊 **Full cost breakdown** — Outputs daily, weekly, monthly, and yearly fuel costs for your chosen vehicle
- 🔄 **Side-by-side comparison** — Ranks every vehicle in the database against your route in a single table
- 🛡️ **Bulletproof error handling** — API unreachable? Falls back silently. Bad input? Loops until valid

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **requests** | HTTP calls to the live exchange rate API |
| **csv** | Reading the vehicle database |
| **pytest** | Unit test runner (10 tests) |

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/commute-economics-engine.git
cd commute-economics-engine
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

**Run the program**
```bash
python project.py
```

**Run the test suite**
```bash
pytest test_project.py -v
```

**Example session**

```
====================================================
       COMMUTE ECONOMICS ENGINE — Pakistan
====================================================

Available Vehicles:
  1. Suzuki Alto    (18.0 km/L)
  2. Suzuki Swift   (15.0 km/L)
  3. Suzuki Cultus  (15.0 km/L)
  4. Honda City     (14.0 km/L)
  5. Toyota Corolla (12.0 km/L)
  6. Toyota Prius   (25.0 km/L)
  7. Honda N-Box    (22.0 km/L)
  8. Yamaha YBR 125 (45.0 km/L)
  9. Honda CG 125   (40.0 km/L)
  10. Honda CD 70   (60.0 km/L)

Select your vehicle (enter number): 4
Daily commute distance in km (both ways): 30

Fetching current fuel price...
  (Live rate: 1 USD = Rs. 278.50)
  Estimated price: Rs. 194.95/liter

====================================================
  COST REPORT  —  Honda City
====================================================
  Daily Distance   : 30.0 km
  Fuel Price       : Rs. 262.0/liter
  Fuel Efficiency  : 14.0 km/L
----------------------------------------------------
  Daily Cost       : Rs. 561.43
  Weekly Cost      : Rs. 2807.15   (5 days)
  Monthly Cost     : Rs. 12351.46  (22 days)
  Yearly Cost      : Rs. 148217.52 (264 days)
====================================================

  ALL VEHICLES  —  30.0 km/day @ Rs. 262.0/liter
====================================================
  Vehicle                    Monthly       Yearly
----------------------------------------------------
  Suzuki Alto              Rs. 9606    Rs. 115280
  Suzuki Swift             Rs.11528    Rs. 138336
  Suzuki Cultus            Rs.11528    Rs. 138336
  Honda City               Rs.12351    Rs. 148217  ◄ your pick
  Toyota Corolla           Rs.14410    Rs. 172920
  Toyota Prius             Rs. 6916    Rs.  83001
  Honda N-Box              Rs. 7859    Rs.  94319
  Yamaha YBR 125           Rs. 3842    Rs.  46112
  Honda CG 125             Rs. 4323    Rs.  51876
  Honda CD 70              Rs. 2882    Rs.  34584
====================================================
```

**To add a vehicle**, open `vehicles.csv` and append a new row:
```csv
name,efficiency_kmpl
Daihatsu Mira,26
MG ZS EV,999
```

---

## 🗺️ Roadmap

- [ ] **Web interface** — Flask or FastAPI front-end so non-technical users can access it in a browser
- [ ] **EV support** — Add electricity cost (Rs./kWh) alongside petrol for hybrid/electric comparisons
- [ ] **Multiple fuel types** — Separate pricing tracks for petrol, diesel, and CNG
- [ ] **Google Maps integration** — Auto-calculate daily distance from a home and work address
- [ ] **City selector** — Per-city pricing since fuel costs vary across provinces in Pakistan
- [ ] **Export to PDF** — Save the cost report as a downloadable file

---

## 📬 Contact

**Yahya**
CS student · aspiring technical founder · based in Pakistan

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN)

> Open to collaborations, internships, and remote opportunities.