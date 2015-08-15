#
#
#

from steam_lib import steam_api
from steam_lib import steam_id
import pd2_config
import models

class Pd2ConfidenceError(Exception):
  """Base exception for Pd2Confidence."""

class Pd2Confidence(object):
  """Set of non-appengine utilities for PD2 player confidence calculation.
  
  Attributes:
    _steam: SteamApi object for querying Steam.
  """
  
  def __init__(self):
    self._steam = steam_api.SteamApi(pd2_config.STEAM_API_KEY)

  def ResolveSteamUser(self, user_data):
    """Resolves user information to a blank pd2 confidence ndb.Account model.
    
    Assumes input data has been sanitized.
    
    Requires:
      user_data: String containing ID information to lookup
        (url, vanity, SteamID64, SteamID, etc.).
    
    Returns:
      models.Account blank object with steam_64 ID set.
    
    Raises:
      Pd2ConfidenceError if errors resolving user_data.
    """
    try:
      return models.Account(steam_64=int(user_data))
    except ValueError:
      pass
    if 'STEAM_0' in user_data:
      try:
        return models.Account(steam_64=steam_id.ToSteam64(user_data))
      except steam_id.SteamIdError, e:
        raise Pd2ConfidenceError(e)
    try:
      processed_id = steam_id.ConvertSteamProfileUrl(user_data)
    except steam_id.SteamIdError, e:
      raise Pd2ConfidenceError(e)
    if isinstance(processed_id, int):
      return models.Account(steam_64=processed_id)
    else:
      try:
        return models.Account(steam_64=self._steam.ResolveSteamVanity(processed_id))
      except steam_api.SteamApiError, e:
        raise Pd2ConfidenceError(e)
    raise Pd2ConfidenceError("Cannot resolve input to a SteamID64.")

  def UpdateAccount(self, user):
    """Updates ndb.Account object with steam data.
    
    Requires:
      user: ndb.Account object.
    
    Returns:
      Updated ndb.Account object.
    """
    try:
      # This will always query Steam. Is that what we want?
      steam_data = self._steam.GetPd2Stats(user.steam_64)
    except steam_api.SteamApiError, e:
      raise Pd2ConfidenceError(e)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    