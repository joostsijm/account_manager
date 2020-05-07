"""Main application"""

from app import MIDDLEWARE


def download_deep_explorations(region_id):
    """Download the deep explorations list"""
    # return read_deep_explorations()
    result = MIDDLEWARE.get('listed/upgrades/{}'.format(region_id))
    return result
