from numpy import linspace
from shikaku import MultipanelFigure

MARKERSIZE = 10
MARKEREDGEWIDTH = 1.0
LINEWIDTH = 4

def plot_results(x, y, f, params):
    fit_x = linspace(x.min(), x.max(), 100)
    fit_y = f(fit_x, params)
    fig = MultipanelFigure(rows=1, cols=1, width=8, height=8)
    panel1 = fig.get_new_panel()
    panel1.plot(x, y, 'o', color='#00B7C9', ms=MARKERSIZE, mew=MARKEREDGEWIDTH)
    panel1.plot(fit_x, fit_y, '-', color='0.25', lw=LINEWIDTH)
    panel1.text(15, 30, r'$m_{fit} = %.3f$' % params[0] + '\n' + \
                r'$b_{fit} = %.3f$' % params[1],
                fontsize=20, color='k',
                horizontalalignment='center',
                verticalalignment='center',)
    fig.add_panel_to_figure(panel1)
    fig.finalize_figure('linear_fit.png', transparent=True)
