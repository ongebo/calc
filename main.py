from add import sum_up
from subtract import diff


def main():
  features = {'add': sum_up, 'subtract': diff}
  x = input('x = ')
  y = input('y = ')
  operation = input('operation? ')
  result = features[operation](x, y)
  print()
  print('The result of the operation is:', result)


if __name__ == '__main__':
  main()
