from ode import solve_scipy_ode, plot_scipy_ode_results

def main():
    trajectory = solve_scipy_ode()
    plot_scipy_ode_results(trajectory)

if __name__ == '__main__':
    main()