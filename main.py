import os

if __name__ == '__main__':
    print(f'Hi, {'PyCharm'}, have a nice day!')
    name = os.environ.get('NAME')
    print(f'Hi, {name}, have a nice day!')