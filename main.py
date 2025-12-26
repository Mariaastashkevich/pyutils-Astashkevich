import logging
from pyutils import *
from logging_config import configure_logging
import pathlib

logger = logging.getLogger(__name__)


def main():
    configure_logging(level=logging.INFO)
    logger.warning('Starting main()')

    path = pathlib.Path('tests/sample.json')
    save_path = pathlib.Path('to_save.json')
    test_normalize = tuple([x for x in range(1, 1000)])
    normalize(test_normalize)


    print(f'Data from file {path.name!r}:')
    data = load_json(path)
    print(data)

    print(get_column_stats(data, key='age'))
    print(get_column_stats(data, key='salary'))

    print(filter_rows(data, key='salary', value=5000))

    print(group_by(data, key='salary'))

    save_json(data, save_path)

    logger.warning('Finishing main()')

if __name__ == "__main__":
    main()
