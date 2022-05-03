import random
import ray 

@ray.remote
class Machine():
  def __init__(self):
    self.hp = random.randint(10,50)
    self.brand = random.choice(["Bosh", "Siemens", "Festo"])
    self.life_time = 100

  def maintance(self):
    self.life_time += 5
    return self.life_time

  def working(self):
    self.life_time -= 5

# machine = Machine()
# print(machine.hp)
# print(machine.brand)

machine = [Machine.remote() for i in range(5)]
print(machine)
promise = machine[0].maintance.remote()
print(promise)
tmp = ray.get(promise)
print(tmp)