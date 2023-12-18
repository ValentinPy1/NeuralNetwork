import pickle as pkl
import sys
from Sources.DataLoader import Data
from Sources.Core.Model import Model

def main(argv):
    if len(argv) < 3:
        print('Usage: ./tester <model> <dataset>')
        sys.exit(1)
    model_file = argv[1]
    dataset = argv[2]
    data = Data()
    data.load(dataset, 'data')
    x_test, y_test = data.get('data')
    print(f'Test set: {x_test.shape[0]} samples')
    print()
    with open(model_file, 'rb') as file:
        model = pkl.load(file)
    print(f'Loading model from "{model_file}"...')
    acc = model.test_accuracy(x_test, y_test)
    print(f'Accuracy: {acc}')
    print()
    print("Testing...")
    model.plot_progress()
    print()
    print("Done!")

if __name__ == '__main__':
    main(sys.argv)
