import numpy as np
import pandas as pd


def print_hi():
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=list('ABCD'))
    # Use a breakpoint in the code line below to debug your script.
    print(f'{df}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
