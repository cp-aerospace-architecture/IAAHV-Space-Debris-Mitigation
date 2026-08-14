# Autonomous Multi-Spectrum Orbital Debris Mitigation Architecture (ODMA)

An autonomous, closed-loop simulation core engineered for a standardized 3U CubeSat chassis to execute multi-spectrum space debris tracking and orbital remediation vector calculations.

## 🚀 Architectural Overview
This software repository serves as the computational determination engine for a dual-spectrum active and passive orbital cleanup satellite configuration. It bridges orbital trajectory propagation with hypervelocity fluid dynamics to address two distinct risk envelopes:
1. **Macro-Debris Interception (≥ 1 cm):** Closed-loop tracking utilizing SGP4 vector propagation to command a localized Nd:YAG laser ablation firing sequence.
2. **Micro-Debris Containment (≤ 1 mm):** Modeling passive material mechanics for hypervelocity structural particle arrest inside an ultra-low-density (0.002 g/cm³) silica aerogel capture matrix.

---

## 💻 Software Implementation Details
The core processing algorithm (`main.py`) bypasses basic static geometric distance measurements by implementing native aerospace tracking computations. 

* **Two-Line Element (TLE) Injection:** Parses live or historical NORAD TLE matrices.
* **SGP4 Perturbation Modeling:** Integrates orbital mechanics to map gravitational perturbations and geocentric J2000 state vectors.
* **Ablation Momentum Coupling:** Calculates target mass ablation velocity transforms ($\Delta v$) based on target density, pulse length, and kinetic energy dissipation paths.

---

## 🛠️ Installation & Dependency Setup

Ensure you have Python 3.8+ installed. Before running the tracking core, install the required numerical computing and ephemeris dependencies:

```bash
pip install -r requirements.txt
```

### Running the Core Simulation
To initialize the orbital determination tracking thread and execute a mock coordinate conjunction matrix check, run:

```bash
python main.py
```

---

## 🔬 Mathematical Baseline Models Integrated

### 1. Velocity-Delta Ablation Matrix
$$\Delta \vec{v} = \frac{E_{\text{laser}} \cdot C_m}{m_{\text{debris}}}$$

### 2. Aerodynamic Penetration Stop-Distance
$$x_{\text{stop}} = \frac{4}{3} \left(\frac{\rho_p}{\rho_{\text{aerogel}}}\right) r \ln\left(\frac{v_{\text{entry}}}{v_{\text{final}}}\right)$$

---

## 🏆 Competition Profile
* **Project Tier:** Intermediate (Grades 9–10 Division Bracket)
* **Target Categories:** Systems Software / Engineering Technology: Statics & Dynamics
* **Framework:** Prepared for presentation and rigorous technical screening across National and International Science and Engineering Fairs (ISEF Pathway).
