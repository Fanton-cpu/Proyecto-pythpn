import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig1, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
    