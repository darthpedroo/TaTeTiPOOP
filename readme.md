# TaTeTiPoo

TaTeTiPoo is an object oriented prgogramming TicTacToe game made in python


## Features

- Supports different game piece types (e.g., circles, crosses, etc.)
- Dynamic Board (4x4, 3x3, 20x20)
- Allows as many teams as wanted to play a match
- Dynamic victory conditions (e.g., 3 in a row, 4 in a row)

## Requirements

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/tatetipoo.git
   cd tatetipoo
   ```

2. To run the game:
```bash
   python main.py
```


## Testing 
### Prerequisites

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytest.
```bash
pip install pytest
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install coverage.
```bash
pip install coverage
```

### How To Run Tests

If you don't want to see a coverage report, run: 
```bash
python -m pytest
```
### Generate Coverage Report
To run the tests and see the coverage report run:
```bash
coverage run -m pytest
```
To generate coverage report run:
```bash
coverage report
```

To generate convert the report into an html run:

```bash
coverage html

Wrote HTML report to htmlcov\index.html
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
