from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import numpy as np
import matplotlib.pyplot as plt


class AccueilAgent(Agent):
    def __init__(self, unique_id, model, pathology, name):
        super().__init__(unique_id, model)
        self.pathology = pathology
        self.name = name

    def step(self):
        print("Hi, I am patient number " + str(self.unique_id) + " with name: " + self.name +
              " and pathology: " + self.pathology)


class MedicalAgent(Agent):
    def __init__(self, unique_id, model, skill, name):
        super().__init__(unique_id, model)
        self.skill = skill
        self.name = name

    def step(self):
        print("Hi, I am medical staff number " + str(self.unique_id) + " with name: " + self.name +
              " and skill: " + self.skill)


class GlobalMASModel(Model):
    def __init__(self, num_patients, num_medical_staff):
        super().__init__()
        self.num_patients = num_patients
        self.num_medical_staff = num_medical_staff

        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, torus=True)

        for i in range(self.num_patients):
            patient = AccueilAgent(i + 1, self, "Patho" + str(i + 1), "Name Patient" + str(i + 1))
            self.schedule.add(patient)
            coord = (self.random.randrange(0, 10), self.random.randrange(0, 10))
            self.grid.place_agent(patient, coord)

        for i in range(self.num_patients, self.num_patients + self.num_medical_staff):
            medical_staff = MedicalAgent(i + 1, self, "Skill" + str(i + 1), "Name Medical Staff" + str(i + 1))
            self.schedule.add(medical_staff)

    def step(self):
        self.schedule.step()


num_patients = 100
num_medical_staff = 1
model = GlobalMASModel(num_patients, num_medical_staff)

steps = 1

for s in range(steps):
    model.step()

agent_counts = np.zeros((model.grid.width, model.grid.height))

for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count

plt.imshow(agent_counts)
plt.colorbar()
plt.show()
