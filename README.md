[English](README.md) | [Türkçe](README.tr.md)

# Variable-Throat Multi-Chamber Rocket: Project Description and Mathematical Model

> **Status: preliminary calculation.** This work is an idea draft; it has not been validated against real engine data or experiments. The numbers use example values. The mechanism mass (68.7 kg) is an **estimate** and affects the result more than anything else. The calculations were done together with Claude (Anthropic).

## The idea

Narrow the nozzle throat with rods each time a combustion chamber finishes burning, so the gas expands more and the rocket runs at a higher exhaust velocity.

The rocket's spine carries stacked combustion chambers, called **stages** in this document. When a stage finishes burning, the empty chamber stays in the body (it is not jettisoned) and the next stage takes over. Later stages burn less propellant per second (lower mass flow). In a fixed nozzle, a lower mass flow drops the chamber pressure and the nozzle no longer matches the new conditions.

The rods are graphite-coated and withstand high temperature. One end of each rod is attached around the nozzle, the other end swings into the throat. As the center of the swing moves down, the throat gets smaller. Because the nozzle exit does not change, a smaller throat increases the exit-to-throat ratio (the expansion ratio).

Fuel and oxidizer arrive by separate paths: **liquid oxygen (LOX) is fed through the central spine**, and **ethanol is fed through the annular gap between the engine body and the outer wall**. The ethanol annulus also acts as a thermal buffer between the burning chambers and the outer wall. Each chamber is fed only through its own valves, and the amount is adjusted from low to high. See "Feed system and layout" below.

**Main claim:** narrowing the throat together with the mass flow raises Isp (specific impulse).
**Counterweight:** the mass of the rod mechanism. This document computes the two together.

## Basic concepts

| Term | Plain meaning | Unit |
| --- | --- | --- |
| Stage (chamber) | A combustion chamber with its own propellant that stays in the body, empty, after burning; this project has 3 stages | - |
| Chamber pressure (pc) | Pressure where the gas burns | Pa (1 bar = 100,000 Pa) |
| Mass flow (ṁ) | Propellant and oxidizer mass burned per second | kg/s |
| Throat area (At) | Narrowest cross-section of the nozzle; gas reaches the speed of sound here | m² |
| Exit area (Ae) | Cross-section of the nozzle mouth | m² |
| Expansion ratio (ε) | Exit area divided by throat area, Ae / At | dimensionless |
| Exhaust velocity (ve) | Speed of the gas leaving the nozzle | m/s |
| Specific impulse (Isp) | Thrust divided by propellant weight flow per second | s |
| Δv | Total velocity change the rocket can achieve | m/s |

Gravitational acceleration g₀ = 9.80665 m/s².

## Feed system and layout

| Line | Path | Note |
| --- | --- | --- |
| LOX (oxidizer) | Central spine | −183 °C; must be insulated from the heat of the surrounding chambers |
| Ethanol (fuel) | Annulus between the engine body and the outer wall | Freezes at −114 °C; must be kept away from the LOX line and insulated |
| Purge | Nitrogen or helium | Cleans the lines during start-up, shutdown and separation |

Design principles:

- **Fuel and LOX never touch before the injector face.** Propellant and oxidizer that mix early can cause flashback in a line; they meet only inside the combustion chamber, at the injector.
- **Every line has a check valve, and each chamber has its own valves.** Only the burning chamber is fed; flow to the other chambers is closed.
- **Injector pressure drop** is chosen at about 15-25% of chamber pressure; it is needed to prevent combustion oscillation (chugging). At 50 bar chamber pressure, the feed pressure is about 60 bar (estimate).
- **Sequencing:** in common practice fuel opens first and LOX second; at shutdown LOX is cut first.

This section is not included in the model: mixture ratio (O/F), line diameters and flow distribution were not modeled. The mass of valves, injectors and purge hardware is counted inside the fixed 60 kg of the empty chamber mass; line mass was not computed separately. This section contains design principles that are not validated by calculation.

## Model 1: Throat area and mass flow

If the mass flow drops, the throat must shrink to keep the chamber pressure constant.

```math
\dot{m} = \frac{p_c \, A_t}{c^{*}} \qquad\Longrightarrow\qquad A_t = \frac{\dot{m}\, c^{*}}{p_c}
```

When the gas reaches the speed of sound in the throat, the flow "chokes"; the amount of gas passing depends only on the chamber conditions and the throat area.

| Symbol | Meaning | Value (example) |
| --- | --- | --- |
| ṁ | Mass flow | Stage 1: 70, stage 2: 35, stage 3: 17.5 kg/s |
| p_c | Chamber pressure (constant design pressure) | 50 bar = 5,000,000 Pa |
| A_t | Throat area | Computed |
| c* | Characteristic velocity: sums up the "quality" of the gas and temperature in one number | 1658 m/s |

```math
c^{*} = \frac{\sqrt{R\,T_c}}{\Gamma}, \qquad \Gamma = \sqrt{\gamma}\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}}
```

| Symbol | Meaning | Value (example) |
| --- | --- | --- |
| R | Specific gas constant, R = 8.314 / molecular weight | 361.5 J/kg/K (molecular weight 0.023 kg/mol) |
| T_c | Combustion temperature | 3200 K |
| γ | Heat capacity ratio | 1.2 |
| Γ | Helper number derived from γ | 0.6485 |

Result: A_t = 232 cm² (stage 1), 116 cm² (stage 2), 58 cm² (stage 3).

## Model 2: Expansion ratio

Because the nozzle exit is fixed, the expansion ratio grows as the throat shrinks: 8 → 16 → 32.

```math
\varepsilon = \frac{A_e}{A_t}
```

The exit area was chosen as 8 times the stage 1 throat: A_e = 8 × 232 = 1857 cm² (it belongs to the nozzle body and does not change in flight). The relation between area ratio and pressure ratio:

```math
\varepsilon = \frac{\Gamma}{\left(\frac{p_e}{p_c}\right)^{1/\gamma}\sqrt{\frac{2\gamma}{\gamma-1}\left[1-\left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}}\right]}}
```

This equation cannot be inverted by hand; p_e/p_c is solved numerically.

| Stage | ε | p_e / p_c | Exit pressure p_e |
| --- | --- | --- | --- |
| 1 | 8.0 | 0.01687 | 0.843 bar |
| 2 | 16.0 | 0.00677 | 0.339 bar |
| 3 | 32.0 | 0.00277 | 0.139 bar |

## Model 3: Exhaust velocity

As the gas expands it cools, and the heat energy it loses becomes velocity.

```math
\frac{v_e^2}{2} = c_p\,(T_c - T_e) \quad (1) \qquad c_p = \frac{\gamma R}{\gamma - 1} \quad (2) \qquad \frac{T_e}{T_c} = \left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}} \quad (3)
```

(1) is energy conservation, (2) is the heat capacity of an ideal gas, (3) is the temperature-pressure relation for expansion without heat exchange (isentropic). Combining them:

```math
v_e = \eta \sqrt{\frac{2\gamma}{\gamma-1}\, R\, T_c \left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}}\right]}
```

| Symbol | Meaning | Value (example) |
| --- | --- | --- |
| v_e | Exhaust velocity | Computed |
| η | Nozzle efficiency (friction and other losses) | 0.95 |
| c_p | Heat capacity at constant pressure | 2169 J/kg/K |
| T_c, T_e | Temperature in the chamber and at the exit | 3200 K and computed |

| Stage | Fixed nozzle, v_e | Variable throat, v_e | Exit temperature T_e |
| --- | --- | --- | --- |
| 1 | 2487 m/s | 2487 m/s | 1621 K |
| 2 | 2487 m/s | 2661 m/s | 1392 K |
| 3 | 2487 m/s | 2799 m/s | 1199 K |

### Relation to Bernoulli

This formula is Bernoulli's equation extended to gases; both say "if velocity rises, pressure energy falls". The difference is density:

```math
\frac{v^2}{2} + \frac{p}{\rho} = \text{constant} \quad\text{(Bernoulli, constant density)} \qquad \frac{v^2}{2} + \frac{\gamma}{\gamma-1}\,\frac{p}{\rho} = \text{constant} \quad\text{(gas nozzle)}
```

In the nozzle the gas density drops by about 135 times from the 4.3 kg/m³ in the chamber (stage 3); plain Bernoulli gives about 1520 m/s, the real formula (without η) gives 2946 m/s.

## Model 4: Specific impulse (Isp)

```math
F = \dot{m}\, v_e + (p_e - p_a)\, A_e \qquad\qquad I_{sp} = \frac{F}{\dot{m}\, g_0}
```

(p_a: ambient pressure, 0 in vacuum.)

| Stage | Fixed nozzle, Isp (vacuum) | Variable throat, Isp (vacuum) |
| --- | --- | --- |
| 1 | 276.4 s | 276.4 s |
| 2 | 276.4 s | 289.6 s |
| 3 | 276.4 s | 300.4 s |

Average Isp over the atmospheric flight: 268.6 s for the fixed nozzle, 281.0 s for the variable throat (+4.6%).

## Model 5: Tsiolkovsky equation and mass budget

```math
\Delta v_i = I_{sp,i}\, g_0 \ln\frac{m_{0,i}}{m_{f,i}} \qquad\qquad \Delta v = \sum_i \Delta v_i
```

m₀: total mass when the stage starts, m_f: mass left when the stage's propellant is used up. Empty chambers are not jettisoned; the m₀ of the next stage equals the m_f of the previous one. The mechanism (68.7 kg) also stays on the rocket.

| Stage | Propellant | Empty chamber | m₀ (fixed) | m_f (fixed) | m₀ (variable) | m_f (variable) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3000 kg | 300 kg | 10200 | 7200 | 10268.7 | 7268.7 |
| 2 | 3000 kg | 300 kg | 7200 | 4200 | 7268.7 | 4268.7 |
| 3 | 3000 kg | 300 kg | 4200 | 1200 | 4268.7 | 1268.7 |

Empty chamber mass = 0.08 × propellant + 60 kg. Payload 300 kg.

| Stage | Δv (fixed) | Δv (variable) |
| --- | --- | --- |
| 1 | 944 m/s | 937 m/s |
| 2 | 1461 m/s | 1512 m/s |
| 3 | 3396 m/s | 3574 m/s |
| **Total** | **5801 m/s** | **6023 m/s** |

For comparison: if empty chambers were jettisoned after each stage (classic staging), Δv would be 7347 m/s for the fixed nozzle and 7550 m/s for the variable throat. Keeping the chambers in the body costs about 1500 m/s; that is much larger than the throat gain (about 220 m/s).

## Model 6: Rod geometry

The throat radius depends on the angle the rod makes with the axis.

```math
r_t = R_p - L \sin\theta \qquad\Longrightarrow\qquad \theta = \arcsin\!\left(\frac{R_p - r_t}{L}\right), \qquad r_t = \sqrt{\frac{A_t}{\pi}}
```

| Symbol | Meaning | Value (example) |
| --- | --- | --- |
| r_t | Throat radius | Computed |
| R_p | Radius of the ring the rods are attached to | 0.45 m |
| L | Rod length | 0.60 m |
| θ | Angle of the rod to the axis | Computed |
| z | Distance of the rod tip along the axis, z = L cos θ | Computed |

| Stage | A_t | r_t | θ | z |
| --- | --- | --- | --- | --- |
| 1 | 232 cm² | 8.60 cm | 37.35° | 47.7 cm |
| 2 | 116 cm² | 6.08 cm | 40.44° | 45.7 cm |
| 3 | 58 cm² | 4.30 cm | 42.72° | 44.1 cm |

**Mechanism mass (estimate).** One set has 12 rods: 12 × 0.60 m × 0.0009 m² × 1750 kg/m³ = 11.3 kg; adding 8 kg for hinges and actuators makes a set 19.3 kg. Two sets for two narrowing steps plus 30 kg of control system: 2 × 19.3 + 30 = **68.7 kg**.

## Example case and results

| Parameter | Value |
| --- | --- |
| Payload | 300 kg |
| Propellant (stage 1 / 2 / 3) | 3000 / 3000 / 3000 kg |
| Empty chamber | 0.08 × propellant + 60 kg (not jettisoned) |
| Mass flow (stage 1 / 2 / 3) | 70 / 35 / 17.5 kg/s |
| Chamber pressure | 50 bar (constant) |
| Combustion temperature, γ, molecular weight | 3200 K, 1.2, 23 g/mol |
| Nozzle efficiency | 0.95 |
| Exit area | 1857 cm² |
| Rod mechanism | 68.7 kg |

Vertical, one-dimensional flight; gravity and air drag included; atmosphere modeled with exponentially decreasing pressure and density.

The three chambers are identical in size and hold equal propellant; the mass flow halves at each stage (70 → 35 → 17.5 kg/s), so the burn times are 43 s, 86 s and 171 s. Thrust-to-weight ratio at the start of each stage (vacuum, variable throat): 1.88, 1.39, 1.23.

| Result | Fixed nozzle | Variable throat |
| --- | --- | --- |
| Velocity at burnout | 2820 m/s | 3047 m/s |
| Altitude at burnout | 331.7 km | 354.9 km |
| Apogee | 813 km | 927 km |
| Average Isp | 268.6 s | 281.0 s |

## Efficiency

The variable throat raises total velocity gain by **3.8% (+222 m/s)**; about 61% of the gross gain from Isp is retained, the rest is taken by the mechanism mass.

| Measure | Fixed nozzle | Variable throat |
| --- | --- | --- |
| Nozzle thermal efficiency, stage 1 / 2 / 3 | 44.5% / 44.5% / 44.5% | 44.5% / 51.0% / 56.4% |
| Isp (vacuum), stage 3 | 276.4 s | 300.4 s (+8.7%) |
| Average Isp (flight) | 268.6 s | 281.0 s (+4.6%) |
| Total Δv (mechanism included) | 5801 m/s | 6023 m/s (+3.83%) |
| Payload carried for the same Δv | 300 kg | 415.7 kg (+38.6%) |

```math
\eta_{\text{thermal}} = \frac{v_e^2}{2\,c_p\,T_c} = \eta^2\left[1-\left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}}\right]
```

**Net contribution of the mechanism:**

| Item | Value |
| --- | --- |
| Gross gain (as if the mechanism had no mass) | +365 m/s (6165 − 5801) |
| Cost of the mechanism mass (68.7 kg) | −143 m/s |
| Net gain | +222 m/s |
| Share retained | 61% |

The break-even mechanism mass is 184.4 kg; since the estimate is 68.7 kg, there is a margin of 115.7 kg. These percentages are compared with the same rocket with a fixed nozzle that also keeps its chambers. The throat gain (about 220 m/s) does not offset the loss from not jettisoning chambers (about 1500 m/s).

## Assumptions, limits and next steps

**Assumptions and limits**

- The gas is treated as ideal; γ, T_c and molecular weight are constant.
- The flight is vertical and one-dimensional; no orbital turn or steering losses.
- The empty chamber mass was taken the same whether or not it is jettisoned; since there is no separation hardware in a single body, the real value may be somewhat lower.
- The mechanism mass (68.7 kg) is an estimate.
- The rods touch gas above 3000 K in the throat; graphite coating erodes in an oxidizing environment, so thermal endurance must be computed separately.
- The propellant pressure must be adjusted in sync as the throat narrows; otherwise chamber pressure rises.
- A large expansion ratio such as ε = 32 can cause flow separation at sea level.
- Insulation and sealing between the ethanol annulus (freezing ≈ −114 °C) and the LOX spine (−183 °C) must be designed separately; liquid hydrogen is not used in this version.
- Heat from the burning chamber flows into the LOX spine and into the ethanol of neighboring chambers (LOX boil-off, ethanol heating); this heat transfer was not computed.
- The Isp loss from the distance between chamber and nozzle is not in the model.

**Next steps**

1. Recompute the mechanism mass with real materials and cross-sections (break-even limit 184.4 kg).
2. Sweep the number of chambers from 1 to 8 and compute the net gain.
3. Model the control relation between throat closing speed and propellant pressure.
4. Examine the thermal load on the rods and the life of the graphite coating.
5. Compute whether jettisoning empty chambers (a separation mechanism) is possible and what it would gain.
6. Model the feed system with numbers: O/F ratio, line diameters, injector pressure drop.
7. Compute heat transfer from the burning chamber to the LOX spine and to the ethanol of neighboring chambers.

## Avionics

A real-time kernel is planned for the avionics software; it has not been designed yet. Its tasks: valve sequencing by stage, monitoring feed pressure, adjusting the rod angle together with mass flow (Models 1 and 6), sensor reading and safety cut-offs.

## Code

`roket_simulasyonu.py` produces all the numbers in this document (standard Python libraries only; comments and printed output are in Turkish):

```
python3 roket_simulasyonu.py
```

To try classic staging that jettisons empty chambers, set `ODA_ATILIR = True` in the file.

## License

Text: CC BY 4.0 · Code: MIT (a license file must be added).
