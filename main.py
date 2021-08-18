import requests
from datetime import datetime, time, timedelta
import time

import logging

from dao.sources.csv_local_file import save_file

from setup.setup import (
        data_url,
        N_OF_MEASUREMENTS,
        TIME_DELTA
    )

from utils.utils import timing


@timing
def _fetch_one_measurement(url):
    res = {}
    try:
        res = requests.get(url).json()
    except IOError as e:
        logging.exception("Cannot fetch data!")
        exit(1)
    # TODO: Remove debug print
    print(res)

    return dict(res)


def fetch_data(url):
    values_to_save = []
    is_keys_present = False
    res = {}

    # print(f"Current time, when fetching: {datetime.now()}")

    # Gathering the first measurement and init keys (according to CSV format):
    res = _fetch_one_measurement(url)

    values_to_save.append(res.keys())
    values_to_save.append(res.values())
    # TODO: Remove debug print
    print(values_to_save)

    time.sleep(TIME_DELTA)

    # Gathering the rest of the package of measurements
    for i in range(N_OF_MEASUREMENTS - 2):

        # TODO: Remove debug print
        # print(f"Current time, when fetching: {datetime.now()}")

        res = _fetch_one_measurement(url)

        values_to_save.append(res.values())
        # TODO: Remove debug print
        print(values_to_save)

        time.sleep(TIME_DELTA)

    # Saving to the persistence layer:
    print(values_to_save)
    save_file(values_to_save)


def main(*argc, **argv):
    print("--- Starting fetching data... ----------------------------")
    fetch_data(data_url)


main()
