# Solar Energy Savings Analysis

## Description

This project is aimed at analysing the financial implications of installing a solar energy system, compared to using traditional electricity from Eskom, a South African electricity public utility. The analysis also explores the financial implications of using existing savings to fund the solar system installation, instead of taking a loan. 

## Repository Contents

1. `header_v.py`: This is a utility file containing the necessary libraries for running the financial simulations.
2. `solar_loan.png`: A plot showing the remaining solar loan amount over time.
3. `cost_comparison.png`: A plot comparing the monthly costs of using solar energy, Eskom electricity, and potential investment returns.
4. `cumulative_cost_comparison.png`: A plot comparing the cumulative costs of the aforementioned scenarios.
5. `savings_ESK.png`: A plot showing the potential savings over time if Eskom electricity was used.
6. `main.py`: This Python script performs the financial simulations and generates the plots.

## The Simulation

The simulation models the costs and savings over a 15-year period. The model assumes:

- The cost of the solar system installation.
- The interest rate on the solar loan.
- The expected lifetime of the solar system.
- The investment return rate.
- The general inflation rate.
- The initial savings available.
- The cost of electricity from Eskom.

The simulation takes into account:

- The repayment of the solar loan, with the principal and interest calculated monthly.
- The cost of electricity from Eskom, with inflation applied annually.
- The potential savings if the cost of the solar system is less than the cost of electricity from Eskom, with the difference invested at a specified interest rate.
- The savings interest earned under both Eskom and Solar usage scenarios.

## Results

The generated plots provide a detailed comparison of the cost implications of choosing a solar energy system, continuing with Eskom's electricity, or utilizing savings for installation of the solar system.


## Dependencies

- Python
- numpy
- pandas
- numpy_financial
- matplotlib
- pylab
- dateutil

## Conclusions

The simulation provides insights into the financial implications of using a solar energy system compared to Eskom's electricity. It allows for informed decisions based on different financial and market factors, which can be adjusted according to the user's scenario.
