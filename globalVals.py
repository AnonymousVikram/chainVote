import random
import pandas as pd
# from voterInformation.initVoters import initVoters

#class globalValsClass:
 #   def init():

data = [random.randint(0, 3), random.randint(2, 6), random.randint(0, 3), random.randint(2, 6), random.randint(0,1), random.randint(1,100), random.randint(0,1), random.randint(1,100), random.randint(0,7500), random.randint(0, 3), random.randint(2, 7), random.randint(0, 4), random.randint(3,8)]
columnsList = ['fNameStart', 'fNameLen', 'lNameStart', 'lNameLen', 'dobM', 'dobMModifier', 'dobD', 'dobDModifier', 'dobOverallModifier', 'idStart', 'idLen', 'pnStart', 'pnLen']

tuples = list(zip(columnsList, data))
importantVals = pd.DataFrame(tuples, columns = ['varName', 'val'])

importantVals.to_csv("/Volumes/Vikram's Hard Drive/Programming/chainVote/globalVals.csv", index = None)