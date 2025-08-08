from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

iris = load_iris()


print(iris.data)
print(iris.target)
print(iris.target_names)
for i in range(3):
    print(f'{i} == {iris.target_names[i]}')
print(iris.feature_names)


setosa_sepal_length = []
setosa_sepal_width = []
versicolor_sepal_length = []
versicolor_sepal_width = []
verginica_sepal_length = []
verginica_sepal_width = []

setosa_petal_length = []
setosa_petal_width = []
versicolor_petal_length = []
versicolor_petal_width = []
verginica_petal_length = []
verginica_petal_width = []

targets = []
for i, data in enumerate(iris.data):
    if iris.target[i] == 0:
        setosa_sepal_length.append(data[0])
        setosa_sepal_width.append(data[1])
        setosa_petal_length.append(data[2])
        setosa_petal_width.append(data[3])
    elif iris.target[i] == 1:
        versicolor_sepal_length.append(data[0])
        versicolor_sepal_width.append(data[1])
        versicolor_petal_length.append(data[2])
        versicolor_petal_width.append(data[3])
    else:
        verginica_sepal_length.append(data[0])
        verginica_sepal_width.append(data[1])
        verginica_petal_length.append(data[2])
        verginica_petal_width.append(data[3])
        

fig = plt.figure(tight_layout=True)
fig.set_size_inches(15,8)
gs = gridspec.GridSpec(2, 2)

ax = fig.add_subplot(gs[0, 0])
ax.set_title('Flowers_sepal')
ax.set_ylabel('sepal_width')
ax.set_xlabel('sepal_length')
ax.plot(setosa_sepal_length, setosa_sepal_width, 'o', color= 'blue', label='setosa')
ax.plot(versicolor_sepal_length,versicolor_sepal_width, 'o', color= 'red', label= 'versicolor')
ax.plot(verginica_sepal_length, verginica_sepal_width, 'o', color= 'green', label= 'verginica')
plt.legend()
fig.align_labels()

ax = fig.add_subplot(gs[0, 1])
ax.set_title('Flowers_petal')
ax.set_ylabel('petal_width')
ax.set_xlabel('petal_length')
ax.plot(setosa_petal_length, setosa_petal_width, 'o', color= 'blue', label='setosa')
ax.plot(versicolor_petal_length,versicolor_petal_width, 'o', color= 'red', label= 'versicolor')
ax.plot(verginica_petal_length, verginica_petal_width, 'o', color= 'green', label= 'verginica')
plt.legend()
fig.align_labels()

ax = fig.add_subplot(gs[1, 0])
ax.set_title('Flowers_petal/sepal')
ax.set_ylabel('sepal_width')
ax.set_xlabel('petal_length')
ax.plot(setosa_petal_length, setosa_sepal_width, 'o', color= 'blue', label='setosa')
ax.plot(versicolor_petal_length,versicolor_sepal_width, 'o', color= 'red', label= 'versicolor')
ax.plot(verginica_petal_length, verginica_sepal_width, 'o', color= 'green', label= 'verginica')
plt.legend()
fig.align_labels()

ax = fig.add_subplot(gs[1, 1])
ax.set_title('Flowers_petal/sepal')
ax.set_ylabel('petal_width')
ax.set_xlabel('sepal_length')
ax.plot(setosa_sepal_length, setosa_petal_width, 'o', color= 'blue', label='setosa')
ax.plot(versicolor_sepal_length,versicolor_petal_width, 'o', color= 'red', label= 'versicolor')
ax.plot(verginica_sepal_length, verginica_petal_width, 'o', color= 'green', label= 'verginica')
plt.legend()
fig.align_labels()

def onclick(event):
    print('X=', event.xdata, 'Y=', event.ydata)
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()