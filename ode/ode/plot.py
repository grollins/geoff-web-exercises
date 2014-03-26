from numpy import log10
from shikaku import MultipanelFigure

MARKERSIZE = 10
MARKEREDGEWIDTH = 1.0
LINEWIDTH = 6
COLOR_SCHEME = ['#00B7C9', '#3D9199', '#FF404C', '#00FF87', '#CC147C']

def plot_scipy_ode_results(trajectory):
    t = trajectory['t']
    U = trajectory['U']
    I = trajectory['I']
    F = trajectory['F']
    log_t = t
    log_U = U
    log_I = I
    log_F = F
    fig = MultipanelFigure(rows=1, cols=1, width=8, height=8)
    panel1 = fig.get_new_panel()
    panel1.plot(log_t, log_U, '-', color=COLOR_SCHEME[0],
                lw=LINEWIDTH, label="U")
    panel1.plot(log_t, log_I, '-', color=COLOR_SCHEME[1],
                lw=LINEWIDTH, label="I")
    panel1.plot(log_t, log_F, '-', color=COLOR_SCHEME[2],
                lw=LINEWIDTH, label="F")
    panel1.legend(loc=5)
    fig.add_panel_to_figure(panel1, xtick_fmt="%.0f", ytick_fmt="%.1f")
    fig.finalize_figure('scipy_ode.png', transparent=True)
