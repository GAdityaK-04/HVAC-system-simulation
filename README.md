# HVAC-system-simulation
simulate a simplified, energy-management-focused HVAC(heating-ventilation-air-conditioning) system using Python.

aim-
To maintain the temperature of the room constant at 22C. The Python random and time modules will drive the simulation state.

inputs-
The system will employ (ON/OFF) control to maintain a room's temperature T(room) based on dynamic factors like occupancy and ambient temperature.

output-
Power Consumption: Calculation of the instantaneous electrical power P(electrical) drawn by the HVAC unit, and the total energy consumed over 24 hours.

System Model: First-Order Thermal DynamicsThe simulation models the room as a single thermal mass. 
The rate of temperature change depends on heat transfer with the ambient environment, internal heat generation, and the maximum power of the HVAC unit.
**Governing Equation:** The temperature change dT_room at each time step dt is calculated using the energy balance:

**T_room(t+dt) = T_room(t) + (dt/C)*(Q_hvac + Q_ambient + Q_occupants)**

Desired Temperature T_setpoint: 22^C

Upper limit T_high: 22^C + hysteresis(0.5^C) = 22.5^C

Lower limit T_low: 22^C - hysteresis(0.5^C) = 21.5^C
