from scipy.integrate import ode
from pandas import DataFrame

# Rates, per millisecond
k_UI = 1e2
k_IU = 1e3
k_IF = 5e0
k_FI = 6e-8

def f(t, y):
    U, I, F = y[0], y[1], y[2]
    dU_dt = -k_UI * U + k_IU * I
    dI_dt = -(k_IU + k_IF) * I + k_UI * U + k_FI * F
    dF_dt = -k_FI * F + k_IF * I
    eqns = [dU_dt, dI_dt, dF_dt]
    return eqns

def jacobian(t, y):
    U, I, F = y[0], y[1], y[2]
    dU_dt_dU = -k_UI
    dU_dt_dI = k_IU
    dU_dt_dF = 0.
    dI_dt_dU = k_UI
    dI_dt_dI = -(k_IU + k_IF)
    dI_dt_dF = k_FI
    dF_dt_dU = 0.
    dF_dt_dI = k_IF
    dF_dt_dF = -k_FI
    eqns = []
    eqns.append([dU_dt_dU, dU_dt_dI, dU_dt_dF])
    eqns.append([dI_dt_dU, dI_dt_dI, dI_dt_dF])
    eqns.append([dF_dt_dU, dF_dt_dI, dF_dt_dF])
    return eqns

def solve_scipy_ode():
    ode_solver = ode(f, jacobian)
    ode_solver.set_integrator('zvode', method='bdf', with_jacobian=True)
    y0 = [1.0, 0.0, 0.0] # start with state U fully populated
    t0 = 0.0 # milliseconds
    ode_solver.set_initial_value(y0, t0)
    end_time = 10 # milliseconds
    dt = 0.01 # milliseconds per step

    # Run Integration
    trajectory = []
    while ode_solver.successful() and ode_solver.t < end_time:
        ode_solver.integrate(ode_solver.t + dt)
        t = ode_solver.t
        y = ode_solver.y
        U, I, F = y[0], y[1], y[2]
        trajectory.append([t, U, I, F])
    trajectory = \
        DataFrame.from_records(trajectory, columns=['t', 'U', 'I', 'F'])
    return trajectory
