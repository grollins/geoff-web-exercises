from linear_fit import f, generate_data, fit_data, plot_results

def main():
    x, y = generate_data()
    params = fit_data(x, y)
    plot_results(x, y, f, params)

if __name__ == '__main__':
    main()
