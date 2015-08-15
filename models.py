from google.appengine.ext import ndb

class Account(ndb.Model):
  """NDB Model representing a specific user for PD2 cheater confidence.
  
  Attributes:
    steam_64: String Steam 64bit ID (numeric) index for the user.
    confidence_overall: Integer overall calculated confidence score with all available factors. Default 0.
    total_votes: Integer total number of players that have voted for this user. Default 0.
    total_score: Integer sum total of voting score. Default 0.
    instantaneous_score: Computed integer user score.
    vac_banned: Boolean True if user has been VAC banned ever. Default False.
    private_profile: Boolean True if user has a private profile. Default False.
    level_infamy: Integer player infamy level. Default 0.
    level_player: Integer player numeric level (e.g. 1-100). Default 0.
    total_hours_played: Integer total number of hours user has played PD2. Default 0.
    level_velocity: Computed float level velocity. Approaching 1 is normal. Near 0 is cheating.
    user_requested_deletion: Boolean True if the steam user has requested their information be deleted. Default False.
    last_update: DateTime containing last query / save timestamp.
  """
  steam_64 = ndb.IntegerProperty(indexed=True, required=True)
  confidence_overall = ndb.IntegerProperty(default=0)
  total_votes = ndb.IntegerProperty(default=0)
  total_score = ndb.IntegerProperty(default=0)
  instantaneous_score = ndb.ComputedProperty(self lambda: self.total_score / self.total_votes)
  vac_banned = ndb.BooleanProperty(default=False)
  private_profile = ndb.BooleanProperty(default=False)
  level_infamy = ndb.IntegerProperty(default=0)
  level_player = ndb.IntegerProperty(default=0)
  total_hours_played = ndb.IntegerProperty(default=0)
  level_velocity = ndb.ComputedProperty(self lambda: self.total_hours_played / (self.level_player + 100*(self.level_infamy)))
  user_requested_deletion = ndb.BooleanProperty(default=False)
  last_update = ndb.DateTimeProperty(auto_now)

