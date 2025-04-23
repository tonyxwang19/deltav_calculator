README.md Markdown Code
# Delta V Calculator GUI

A simple desktop application built with Python and Tkinter to calculate delta-v for general rocket maneuvers and Hohmann transfer orbits, fuel requirements, and mission cost estimations.

## Features

- Compute maximum achievable Δv given vehicle mass, fuel mass, payload mass, and exhaust velocity.
- Calculate Δv required for a Hohmann transfer between two circular orbits.
- Estimate the fuel mass needed to achieve a specified Δv.
- Determine the mission cost based on orbit height difference and fuel mass.
- User-friendly GUI built with Tkinter.

## Requirements

- Python 3.6 or above  
- Standard libraries: `math`, `tkinter`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/delta-v-calculator-gui.git
   cd delta-v-calculator-gui
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. In the GUI, enter the following parameters:
   - **Dry Mass (kg)**: Dry mass of the rocket structure.  
   - **Fuel Mass (kg)**: Available propellant mass.  
   - **Payload Mass (kg)**: Mass of the payload.  
   - **Exhaust Velocity (m/s)**: Effective exhaust velocity of the engine.  

3. For Hohmann transfer calculations, enter:
   - **Initial Orbit Height (km)** above Earth's surface.  
   - **Final Orbit Height (km)** above Earth's surface.  

4. Click **Calculate!** to view:
   - Maximum Δv achievable  
   - Δv required for Hohmann transfer  
   - Required fuel mass for the transfer  
   - Estimated mission cost  

5. A popup will indicate whether the vehicle's Δv and fuel capacity are sufficient for the mission.

## Code Structure

- `delta_v_gui.py`: Main application file containing:
  - `delta_v_calculation(dry_mass, fuel_mass, payload_mass, exhaust_v)`: General Δv calculation  
  - `hohmann_orbit_delta_v_calculation(ri, rf)`: Hohmann transfer Δv for circular orbits  
  - `fuel_mass_calculation(delta_v, exhaust_v, initial_mass)`: Computes propellant mass needed  
  - `price(orbit_height, fuel)`: Mission cost estimator  

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests with improvements, additional features, or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Developed by Tony Xining Wang*
