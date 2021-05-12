from rest_requests.get_response_content import get_json_content
from rest_requests.request import get_request


def get_episode_search_total(base_url, digest_login, course_id):
    """
    Get episode count from search by series as num.

    :param base_url: The base URL for the request
    :type base_url: str
    :param digest_login: The login credentials for digest authentication
    :type digest_login: DigestLogin
    :param course_id: The series id
    :type course_id: str
    :return: count as num or None
    :rtype: count as num or None
    :raise RequestError:
    """

    url = '{}/search/episode.json?sid={}'.format(base_url, course_id)

    # print("url for search is {}".format(url))
    response = get_request(url, digest_login, "search episode")
    search_results = get_json_content(response)["search-results"]
    if "total" in search_results:
        return search_results["total"]
    return None
