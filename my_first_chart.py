import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
prices = [68500, 69200, 70100, 69700, 71300, 72500, 71800]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", 
                (i, p),
                textcoords="offset points",
                xytext=(0, 8), 
                ha="center")
ax.set_title("내 첫 그래프")
fig.savefig("my_first_chart.png")