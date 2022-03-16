from subscribing import Subscriber
from publish import Publisher
from group import Group

pub = Publisher()
sub = Subscriber()
group = Group()

class Main:
  def __init__(self):
    pass
  
  def main(self):
    while True:
      print('''
        0 - Exit\n
        1 - List Users\n
        2 - Create group\n
        3 - Request chat to debug\n
      ''')
      choice = int(input('#\n'))
      if choice == 0:
        exit()
      if choice == 1:
        pass
      if choice == 2:
        pass
      if choice == 3:
        pass
m = Main()

m.main()