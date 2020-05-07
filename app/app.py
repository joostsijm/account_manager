"""General function module"""

from app import LOGGER, api


def sync_deep_exploration(region_id):
    """Check resources and refill if necessary"""
    LOGGER.info('Sync deep exploration history for %s', region_id)
    result = api.download_deep_explorations(region_id)
    print(result)
