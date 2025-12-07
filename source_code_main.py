# main code:

print("============= HVAC - Heating Ventilating Air Conditioning System ==============")
print("\n=================================== DAY LOG ===================================")
print("\ntime_hours\t Temp_room\t Occupants\t HVAC_mode\t Power_consumed")

E_total = 0

for t in range(300, 86400, 300):
    Temp_room, q_hvac, N = heating_cooling(t)
    HVAC_mode = mode_hvac(q_hvac)
    P = power_consumed(HVAC_mode)
    E_total += P*dt
    print(f"{time_24hr(t):<10} {Temp_room:>11.2f} {N:>15} {HVAC_mode:>19} {P:>20.2f}")

print(f"Total energy used: {(E_total/3600000):.2f}kWh")
