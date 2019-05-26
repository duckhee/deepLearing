from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("iris_dataset key:\n")
print(iris_dataset.keys())
print(iris_dataset['DESCR'][:193]+"\n...")
