import os
import sys

sys.path.append(os.path.join(os.path.abspath('..'), "lib"))

import config
from args.digest_login import DigestLogin
# from data_handling.elements import get_id
# from data_handling.parse_manifest import parse_manifest_from_endpoint
# from export import export_videos, export_catalogs
from parse_args import parse_args
from rest_requests.search_request_total import get_episode_search_total
# from rest_requests.assetmanager_requests import get_media_package
# from rest_requests.search_requests import get_episode_from_search
# from rest_requests.search_requests import get_episode_from_search

def main():
    """
    Count published events
    """

    # series_ids = parse_args()
    digest_login = DigestLogin(user=config.digest_user, password=config.digest_pw)
    series_ids = [20210225117,20210226078,20210226021,20210224268,20210225487,20210225750,20210226040,20210226066,20210226066,20210225477,20210225779,20210222379,20210222424,20210223186,20210223860,20210223860,20210225945,20210225969,20210225979,20210225992,20210226003,20210226107,20210222957,20210222957,20210222957,20210223214,20210223609,20210224927,20210225068,20210225068,20210225068,20210225337,20210225339,20210225654,20210225659,20210225693,20210225759,20210225776,20210226057,20210220195,20210220393,20210223232,20210223862,20210224540,20210224556,20210224748,20210224748,20210225022,20210225118,20210225526,20210225526,20210225668,20210225668,20210225788,20210225921,20210226002,20210226019,20210226025,20210225913,20210225126,20210225478,20210225695,20210225897,20210225898,20210225923,20210226017,20210226053,20210221783,20210221784,20210223096,20210224776,20210225745,20210225757,20210225900,20210225907,20210225934,20210225944,20210225966,20210225980,20210226008,20210220389,20210221144,20210221474,20210223285,20210223462,20210223614,20210223689,20210224040,20210224046,20210224557,20210225069,20210225358,20210225413,20210225473,20210225505,20210225690,20210225789,20210225915,20210225968,20210225998,20210226012]

    # get events from all series
    if series_ids:
        print("Getting event total for series {}.".format(series_ids))
        # events = []
        event_total = 0;
        for series_id in series_ids:
            # print("Getting event total for serie {}.".format(series_id))
            try:
                event_count = get_episode_search_total(config.presentation_url, digest_login, series_id)
                print("Total for series {} is {}.".format(series_id, event_count ))
                event_total = event_total + int(event_count)
            except Exception as e:
                print("Events of series {} could not be requested: {}".format(series_id, str(e)))

    print("Total is {}".format(event_total))

def __abort_script(message):
    """
    Print message and abort script.
    :param message: The error message
    :type message: str
    """
    print(message)
    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborting process.")
        sys.exit(0)
