import abc from ABC
from abc import abstractmethod

#Creating Base class

class club(abc):
  
  #Club information
  @abstractmethod
  def clubinfo():
    pass
  
  #Information of Club members
  @abstractmethod
  def memberinfo():
    pass
  
  #Information of Events
  @abstractmethod
  def eventsinfo():
    pass
  
  #Information of Funds
  @abstractmethod
  def fundsinfo():
    pass
  
  
  
  #Child Class
  
  class Cultural(club):
    
    #ClubINfo
    
    def getclubinfo()
