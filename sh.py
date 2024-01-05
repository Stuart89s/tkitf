from minister import Minister
from mission import *
import random

minister1 = Minister("김개똥")
# minister2 = Minister("이소똥", 40, 60, 30, 60, 100)
# minister3 = Minister("박말똥", 40, 60, 30, 60, 100)

print(minister1.combat)

print(TigerHuntMission(2, minister1).apply_mission_effects())