from nba_api.stats.endpoints import leaguegamefinder, commonteamroster
from nba_api.stats.static import teams
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class NBAClient:
    def __init__(self):
        self.team_cache = {} # Cache team IDs for faster lookups

    def get_team_id(self, team_name):
        """Convert team name (e.g. 'Nets') to NBA API team ID"""
        if not self.team_cache:
            self.team_cache = {team['full_name']: team['id'] for team in teams.get_teams()}
        return self.team_cache.get(team_name, None)
    
    def get_todays_games(self):
        """Fetch today's scheduled games"""
        try:
            gamefinder = leaguegamefinder.LeagueGameFinder(
                date_from_nullable=pd.Timestamp.today().strftime('%m/%d/%Y')
            )
            games = gamefinder.get_data_frames()[0]

            # FIlter relevant columns
            return games[['GAME_DATE', 'MATCHUP', 'TEAM_NAME', 'PTS']]
        except Exception as e:
            logger.error(f"Failed to fetch today's games: {str(e)}")
            return pd.DataFrame()
        
    def get_team_stats(self, team_name, season='2024-25'):
        """Get seasonal stats for a specific team"""
        team_id = self.get_team_id(team_name)
        if not team_id:
            return None
        
        try:
            roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=season)
            return roster.get_data_frames()[0]
        except Exception as e:
            logger.error(f"Failed to fetch stats for {team_name}: {str(e)}")
            return None