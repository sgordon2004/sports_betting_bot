from app import celery
from app.services.nba_client import NBAClient
import logging

logger = logging.getLogger(__name__)
nba_client = NBAClient()

@celery.task(name='schedule_daily_bet')
def schedule_daily_bet():
    """Scheduled task to handle daily betting logic"""
    try:
        logger.info("Starting NBA data fetch...")

        # 1. Get today's games
        games = nba_client.get_todays_games()
        if games.empty:
            logger.warning("No games found today")
            return
        logger.info(f"Today's games: {games.to_dict('records')}")

        # 2. Example: Get Lakers stats
        lakers_stats = nba_client.get_team_stats("Los Angeles Lakers")
        if lakers_stats is not None:
            logger.info(f"Lakers roster: {lakers_stats[['PLAYER', 'POSITION']]}")

        # logger.info("Starting daily bet scheduling...")
        # # actual betting logic here
        # logger.info("Daily bet scheduling completed successfully")
    except Exception as e:
        # logger.error(f"Error occured in schedule_daily_bet: {str(e)}", exc_info=True)
        logger.error(f"Task failed: {str(e)}", exc_info=True)