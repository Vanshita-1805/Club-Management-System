import abc from ABC
from abc import abstractmethod
import csv

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
    
    def clubinfo():
      print("This club provides a platform to the artist of COEP to demonstrate their art skills and embrace them while pursuing engineering.\nIt consists of various sections like dance , drama , music and the list goes on...")
    
    def membersinfo():
      info = open('cultural.csv')
      memberinf = csv.reader(info)
      
    
    def eventsinfo():
      pass
    
    def fundsinfo():
      pass
