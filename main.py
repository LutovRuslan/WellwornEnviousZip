from random import randint

from pilk_clicker.api import Auth
from pilk_clicker.interfaces.auth import ILoginRequest
from pilk_clicker.interfaces.auth import ILogupRequest
from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.api import Clicker
from pilk_clicker.interfaces.clicker import IClickerSaveRequest
from random_username import generate
from threading import Thread

class Main:
  def __call__(self):
    for i in range(100):
      credentials = ILogupRequest(
              username=generate.generate_username()[0],
              password="test" + str(randint(0, 100000)) + "rt$$$",
              email="test" + str(randint(0, 100000)) + "@test.com",
          )
      Auth.logup(credentials)
      credentials = ILoginRequest(
          username=credentials.username, password=credentials.password
      )
      response = Auth.login(credentials)
      token = ITokenRequest(authorization=response.auth_token)
      clicker_detail = Clicker.clicker_detail(token)
      for i in range(5):
        data = Clicker.clicker_detail(token)
        Clicker.save_clicker(
          data=IClickerSaveRequest(
              arcoin_amount=data.arcoin_amount + randint(0, 10000000000000),
              arcoins_per_click=data.arcoins_per_click + randint(0, 100000000),
              arcoins_per_seconds= data.arcoins_per_seconds + randint(0, 100000000),
          ),
          credentials=token,
        )
        print(data)

class ThreadMain(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.main = Main()
  def run(self):
    self.main()


if __name__ == "__main__":
  main = ThreadMain()
  main.start()