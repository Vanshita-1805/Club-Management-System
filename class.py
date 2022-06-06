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
      for row in memberinf:
        print
      
    
    def eventsinfo():
      pass
    
    def fundsinfo():
      pass
    
  class AaryaRaas(club):
      
    def clubinfo():
        print("Aarya Raas, a girls' club was initiated to promote women empowerment and work for social causes.When it started in 2007, it was just a small club, self-funded, and dedicated to the spirit of womanhood. We went on growing since then and tried to strengthen the club.Influencing other people as well, Aarya Raas gets involved in various social activities like visit and support to Old age Homes and Orphanages, organizing free medical checkups and blood donation camps.Motivating the handicrafts made by women, the women empowerment has also been promoted. It also has been arranging various inspiring lectures and much more.")
        
    def membersinfo():
        pass
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
    
  class Abhijat(club):
      
    def clubinfo():
        print("Team Abhijaat cover technical, non technical, sports and cultural events along with number of other activities taking place in the semester which help a student to grow and to become the responsible citizen of the country. Through the softcopies and the hardcopies, we give opportunity to students to develop their reporting skills and through the satire cartoons. We try to put the fact in front of students.")
        
    def membersinfo():
        pass
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
  class ANC(club):
      
    def clubinfo():
        print("The Arts and Crafts club, fondly called as 'ANC' in the college is one of the oldest, prestigious and the biggest club of COEP. Arts & Crafts club mainly organizes an exhibition at Main building where the team displays its art collection including sketches, paintings, sculptures & various crafts made during semesters. The team shows its innovation, creativity and hard work through exhibitions during MindSpark in odd semester and an annual gathering in even semester. Also, the club is instrumental in decorating the college campus during festivals like Zest, Regatta and Impressions. The club organizes its inauguration at the start of every semester for freshers or new aspirants to join.")
        
    def membersinfo():
        pass
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
 class Astronomy(club):
      
    def clubinfo():
        print("Who hasn't marvelled at the celestial wonders and experienced a sense of awe at being a part of such an infinite expanse? Since its foundation in 2004, the COEP Astronomy club has sought to build on this fascination and brings innovation and passion to its vision of spreading the awareness and knowledge of astronomy and space sciences to the students.The COEP Astronomy club, an ambitious team, driven by amateur astronomers, has managed to conjure up a lot of interest amongst the masses in the science and principles of astronomy. We firmly believe astronomy is for everyone. Integrating technical skills with astronomical science, the club has initiated many projects, some of which being the construction of one of India's largest amateur-built telescopes – a 12 Newtonian reflector, construction of mobile, inflatable planetarium dome, an amateur radio telescope etc.The club strives to quench a student's thirst for astronomy by organizing various exciting events such as StarParty (a fun-filled night of star-gazing), Planetarium visits, Quiztronomy (a quiz to test people's knowledge on everything seen beyond the night sky), Telescope building and handling sessions (telescope – every astronomer's weapon), and many more. Public outreach sessions for underprivileged children school children to introduce them to the basics of Astronomy are also conducted.Discussions and brainstorming sessions are also held every week wherein members explore the cosmos.")
        
    def membersinfo():
        pass
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
      
 class PDS(club):
      
    def clubinfo():
        print("The motto of Personality Development Club is to develop character with competence. The club emphasizes on invoking hidden soft skills which are very vital to stay and deal in the current scenario of cut-throat competition. Thus, the club conducts various workshops and training sessions by various experts from the professional world so as to develop communication skills, and to learn about technical presentations and industrial etiquettes.")
        
    def membersinfo():
        info = open('PDS.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
      
 class Mathematics(club):
      
    def clubinfo():
        print("Though, Mathematics is the language of all science subjects and the backbone of Engineering subjects also, one can enjoy the beauty of Mathematics in its pure form also.Ramanujan Mathematics Club was founded to encourage students to get acquainted with the various branches of Mathematics like Abstract Algebra, Analysis, Discrete Mathematics etc.Every year Ramanujan Mathematics Club arranges lectures on interesting topics by eminent personalities in the field.")
        
    def membersinfo():
        info = open('mathematics.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass

 class RSC(club):
      
    def clubinfo():
        print("Robot Study Circle known as RSC, the Prestigious Robotics Club of COEP is one of the best Robotics clubs in India. It’s a totally different world where club members have created hundreds of robots for society such as Drones, Railway Track Surveillance Robot, Bomb Disposal Robots, and Badminton Playing Robots etc. Robot Study Circle is the National Champion in ROBOCON which is one of the best competitions in robotics in the world. RSC represented India in International Robocon held at Tokyo, Japan and won 6th international position as well as Nagase Award for the country. Also, the Club has industrial collaboration with Siemens PLM as a title sponsor, Volkswagen, Janatics Pneumatics, Schmalz India, Pepperl & Fuchs, and Robolab Technologies. Members of Robot Study Circle are members of the first ever institute student chapter of THE ROBOTICS SOCIETY established in India at College of Engineering, Pune")
        
    def membersinfo():
        info = open('RSC.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass

 class CSAT(club):
      
    def clubinfo():
        print("The COEP Satellite (SWAYAM) project is aimed at developing a reliable bidirectional communications platform.Started in late 2008, the SWAYAM project revolves around the challenge of building a pico-satellite destined to orbit the Earth at a height of 500-800 km.With a total weight of 1 kg and the volume restricted to around 1000 cc, the cube shaped satellite demands an innovative approach at every design phase, from screening of components in order to fit the stringent mass budget to the selection of suitable electronic devices which honour the mere 2 W of power produced by the solar panels. With this in mind, the team has devised an ingenious passive stabilization system which employs a pair of hysteresis rods and a magnet to stabilize the satellite thus eliminating the need to use bulky and power hungry magnetorquers. This Passive Attitude Control System of SWAYAM is the first of its kind in India. The satellite houses a payload capable of half duplex communication over the HAM frequency band which enables it to receive, store and transmit messages from one corner of the globe to the other. The team has also established a functional Ground Station and tracked many amateur radio satellites Acting as a platform which enables the students to empirically test their knowledge has always been the corner stone of this project. Right from its inception, the team has been strongly supported by the college on all fronts, providing valuable infrastructure and a strong funding to keep the project alive. The Qualification of the Satellite is ready and has undergone the Environmental test.The team successfully cleared the Critical Design Review (CDR) at ISAC, Bangalore on 17th September 2014. All the subsystem designs and results were presented and approved by the committee. The team got a clearance for going ahead with the Flight Model of Swayam.Recently the team completed the Flight Model assembly and Environmental tests on it at ISAC. The Flight Model has been handed over to ISRO and the satellite was launched with Cartosat 2C on 22nd June, 2016. Now the satellite has been launched into the space.Team CSAT has already begun its next project. They are working on a satellite which will demonstrate orbit manoeuvering using solar sails with radiation monitoring as payload.")
        
    def membersinfo():
        info = open('CSAT.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
      
 class ScienceClub(club):
      
    def clubinfo():
        print("The Science club, nurturing innovation and raising the profile of science through activities and workshops has conjured up a lot of interest amongst the students of COEP. Science rules the world and human beings attempt to understand its mysterious ways by making laws and theories. We at the science club, aim to encourage scientific temper and answer the burning questions that drive students to pursue research into unknown frontiers.The club strives to quench a student’s thirst for science by organizing various exciting events such as demonstration experiments, science quizzes, talks and lectures by eminent scientists from all over the globe, visits to various labs, workshops and much more. Some of the recent activities include a hands-on session organized by LIGO India on the GMRT telescope and its work with gravitational waves, a photonics workshop by Dr. Kamlesh Alti, a webinar on Eclipsing Binaries my Mr. Bhavesh Rajpoot.")
        
    def membersinfo():
        info = open('science.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass

 class SWE(club):
      
    def clubinfo():
        print("Society of Women Engineers (SWE) is an international, non-profit educational service organization dedicated to making known the need for women engineers and encouraging young women to consider an engineering education. COEP SWE Affiliate aims to provide members with the ideal engineering experience through networking and professional development events, personality development workshops, field visits and numerous inspiring keynote lectures by successful women across the globe. On the occasion of International Women’s Day, we conducted Women’s Week in COEP with multiple events and programmes to promote discussion on women’s issues, talent and wellbeing among all COEPians. We held 12 Fitness sessions under a trainer at COEP Girls’ Hostel and also held a guided meditation session conducted by a trainer affiliated with the Art Of Living. These took place from February to March 2019. We also helped in organizing the teaching and other staff’s Women’s Day Celebration event.  ")
        
    def membersinfo():
        info = open('SWE.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
      
 class SDS(club):
      
    def clubinfo():
        print("")
        
    def membersinfo():
        info = open('SDS.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
      
 class Spandan(club):
      
    def clubinfo():
        print("Spandan is an initiative by COEPians, started in 2003. Ever since Spandan has touched the lives of many underprivileged people such that they look back at their painful past as an ephemeral one.They are now filled with their new-found hope and strongly believe that they can surmount their sorrow and pain and revel in this beautiful world, like most others.SPANDAN, as its name suggests, is the concern that originates straight from the heart of every team member towards the unprivileged section of the society.Some of the activities which we conduct include celebration of Rakshabandhan in orphanages, spending time in old age home, making blind-school students self-employed, village camps, Blood Donation Camps  and much more.Times have changed now. Spandan is changing its agenda. In addition to help the underprivileged to burgeon, the members of Spandan are going to put, the Engineering and Technical Skills. they have. In line with the annual schedule, Spandan will make simple technological prototypes which can ease the lives of the people. As a member of spandan, you will get to know society better will get exposure to work towards underprivileged part of the society and as per our new agenda, you will get to polish your technological skills. Spandan is on its  way to become one of the very few TechnoSocial NGO's.")
        
    def membersinfo():
        info = open('spandan.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass

 class SpicMacay(club):
      
    def clubinfo():
        print("SPIC MACAY seeks to conserve and promote an awareness of this rich and heterogeneous cultural tapestry amongst the youth of this country through focus on the classical arts, with their attendant legends, rituals, mythology and philosophy and to facilitate an awareness of their deeper and subtler values. The SPIC MACAY is a non-profit, volunteer organization pioneered with the motive to promote Indian classical music, dance, and culture amongst youth. It organizes annual VIRASAT series in which prominent artists perform live and give lecture demonstrations. COEP has a chapter of SPIC MACAY.  Music concerts, workshops, film screening, lecture demo are the activities conducted by this club.")
        
    def membersinfo():
        info = open('spicMacay.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
      
 class Abhiyanta(club):
      
    def clubinfo():
        print("Annual magazine of our institute Abhiyanta has been frequently receiving  applauses from all over the state since its first print in 1915.Abhiyanta is one of the most prestigious enterprise in our institute, it receives contribution from all the clubs . It has sections written  in Marathi, Hindi and English  , this magazine includes COEP section which is dedicated to spirit of proud CoEPians.The technical section is an inevitable part of it. Content of the magazine is edited by the Magazine Editing team. The Magazine also provides stage for arts such as illustration, photography and many others.Abhiyanta has grabbed various awards from University of Pune, Maharashtra Sahitya Parishad.")
        
    def membersinfo():
        info = open('abhiyanta.csv')
        memberinf = csv.reader(info)
      
    def eventsinfo():
        pass
      
    def fundsinfo():
        pass
      
  
  class CSI(club):

    def clubinfo():
        print("The Computer Society of India (CSI) Student Chapter of College of Engineering Pune (COEP) , established in October 2018 is an active student organization which organizes a number of technical activities including workshops, competitions, technical symposiums, guest lectures etc. for its student members. Under the guidance of Department of Computer Engineering and Information Technology COEP, the student chapter has over 300 members and is run by a Core Team and faculty from the department.CSI COEP Student Chapter gives students the opportunity to grow in the field of IT.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass
    
class CSI(club):

    def clubinfo():
        print("The Computer Society of India (CSI) Student Chapter of College of Engineering Pune (COEP) , established in October 2018 is an active student organization which organizes a number of technical activities including workshops, competitions, technical symposiums, guest lectures etc. for its student members. Under the guidance of Department of Computer Engineering and Information Technology COEP, the student chapter has over 300 members and is run by a Core Team and faculty from the department.CSI COEP Student Chapter gives students the opportunity to grow in the field of IT.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass
    
class philomystics(club):

    def clubinfo():
        print("Intelligent, ever-motivated, logically sound, witty and a true seeker, is what we engineers pride ourselves to be. But inside each of us, is a small innocent soul, stumbling and learning as it grows up. In this process of growing, each of us develops his/her own philosophy of life. To provide a platform, an outlet to the philosopher inside each of us, the 'Philomystics' club was started in the college. Throughout the year, the group organizes guest lectures as well as many talks by students, in addition to informal discussions and debates amongst the crowd of enthusiasts!")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass    
    
    
class CoFSUG(club):

    def clubinfo():
        print("COEP's Free Software Users Group (COFSUG) is a group of volunteers to promote the use of Free Software (also known as Open Source Software) in COEP and in other institutions in Pune. The group runs a mailing list cofsug@googlegroups.com. The group carries out activities like: Installation fests (to teach people how to install GNU/Linux operating system), Workshops on Linux Administration, Drupal, Python, Various FOSS technologies, Creative Commons, Open Hardware and like.  The group promotes the development of software with release of code under GNU GPL-v3 license. ")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass    
    

class Debate_club(club):

    def clubinfo():
        print("The CoEP Debate Club is Pune's premiere competitive debating club. It is divided into two sections English and Marathi section. The members participate in various inter college tournaments, viz Parliamentary Debates ,  Conventional Debates and Model United Nations, in and out of Pune, winning numerous accolades. Being good public speakers , members also play an active role in anchoring college events. The members have regular debating and brainstorming sessions along with workshops for skill refinement.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass    
            
class HAM_club(club):

    def clubinfo():
        print("COEP Amateur Radio Club established in 1986 makes itself the oldest technical club of College of Engineering Pune. Starting with vacuum tube transmitters, today the club have gradually upgraded the lab and now it holds advanced transmitters and receivers and other latest equipment. COEP's Amateur Radio Club communicates with HAM radio users using the callsign VU2COE. COEP "HAM"s have communicated with almost each and every corner of the world and even with the International Space Station. Every year, HAM Club organizes the A.S.O.C. examination and also coaches students for the same. It also conducts introductory workshops, basic antenna designing workshops annually in COEP and also in other colleges on invitation. The club successfully provides the complete communication link during the various prestigious events of the College of Engineering Pune like Regatta, Mind-spark, Zest, and M.R.A. races held at the COEP Boat Club. COEP HAM Club provides platform for research in field of Antenna and wireless communication and publish research papers about it.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass    
            
                
class History(club):

    def clubinfo():
        print("COEP History Club is a platform for students of COEP to conduct and enjoy activities related to current historical events and important social situations and their historical context. The club organizes many site visits and treks to places of historical significance. These tours are guided ones and different field experts or prominent historians are taken along.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass    
            
                
class i2i(club):

    def clubinfo():
        print("Ignited Innovators of India (I2I) is a movement organized by the BHAU institute of Innovation, Entrepreneurship and Leadership [BIEL] at College of Engineering, Pune. I2I is a unique initiative that aspires to reach out to students across India and provide them with an opportunity to become social entrepreneurs and bring about small but significant changes in the world around. The I2I initiative has been instituted with the vision of promoting and instilling entrepreneurship, leadership and team building skills among students in various colleges. The program encourages them to take up innovative projects that hold potential to make a tangible difference to the community.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass    
            
                
                
class ICSRG(club):

    def clubinfo():
        print("COEP's - Information and Cyber Security Research Group (COEP - ICSRG) is formed by the volunteers to do novel research in Information and Cyber Security in COEP and other Institutes. The group members acquire knowledge in current state of art systems and develop systems using open source softwares or freewares. The group shares knowledge to society and create awareness through conducting seminar, workshop, symposium, conference and media.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass    
            
                
class Janeev(club):

    def clubinfo():
        print("COEP Janeev Club (previously COEP Environment Club) had evolved from an environmental project initially undertaken by a group of Civil Engineering students. The club realized that all environmental and social issues are interconnected, and do not exist in isolation. Thus, it was decided to transform the club with a view to increase its scope by working on social issues as well. In the year 2011, the Environment Club was transformed into Janeev Club (Marathi: जाणीव, meaning: consciousness) as the socio-environmental club of COEP.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass
      
class Boat Club(club):

    def clubinfo():
        print("COEP Janeev Club (previously COEP Environment Club) had evolved from an environmental project initially undertaken by a group of Civil Engineering students. The club realized that all environmental and social issues are interconnected, and do not exist in isolation. Thus, it was decided to transform the club with a view to increase its scope by working on social issues as well. In the year 2011, the Environment Club was transformed into Janeev Club (Marathi: जाणीव, meaning: consciousness) as the socio-environmental club of COEP.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass
      
class Consulting Club(club):

    def clubinfo():
        print("COEP Janeev Club (previously COEP Environment Club) had evolved from an environmental project initially undertaken by a group of Civil Engineering students. The club realized that all environmental and social issues are interconnected, and do not exist in isolation. Thus, it was decided to transform the club with a view to increase its scope by working on social issues as well. In the year 2011, the Environment Club was transformed into Janeev Club (Marathi: जाणीव, meaning: consciousness) as the socio-environmental club of COEP.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass
      
 class CSAC(club):

    def clubinfo():
        print("COEP Janeev Club (previously COEP Environment Club) had evolved from an environmental project initially undertaken by a group of Civil Engineering students. The club realized that all environmental and social issues are interconnected, and do not exist in isolation. Thus, it was decided to transform the club with a view to increase its scope by working on social issues as well. In the year 2011, the Environment Club was transformed into Janeev Club (Marathi: जाणीव, meaning: consciousness) as the socio-environmental club of COEP.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass
      
 
 class BhauECell(club):

    def clubinfo():
        print("COEP Janeev Club (previously COEP Environment Club) had evolved from an environmental project initially undertaken by a group of Civil Engineering students. The club realized that all environmental and social issues are interconnected, and do not exist in isolation. Thus, it was decided to transform the club with a view to increase its scope by working on social issues as well. In the year 2011, the Environment Club was transformed into Janeev Club (Marathi: जाणीव, meaning: consciousness) as the socio-environmental club of COEP.")

    def membersinfo():
        pass

    def eventsinfo():
        pass

    def fundsinfo():
        pass
      
  
  


  
