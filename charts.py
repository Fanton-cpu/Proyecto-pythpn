import matplotlib.pyplot as plt

def generate_bar_chart(length, values):
    fig1, ax = plt.subplots()
    ax.bar(length, values)
    plt.show()
    
