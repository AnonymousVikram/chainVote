import pandas as pd
import random

from ..globalVals import globalValsClass
class initVoters:

    def getDobNum(self, ogValue, index):
        try:
            return int(ogValue[index])
        except:
            return 0
    
    def __init__(self):
        votersDf = pd.read_csv("/Volumes/Vikram's Hard Drive/Programming/chainVote/voterInformation/registeredVoters.csv")
        votersDf.insert(loc=len(votersDf.columns), column="Hash", value = "hash")
        votersDf = votersDf.astype({'Date of Birth': 'datetime64[ns, US/Eastern]'})
        votersDf['Date of Birth'] = votersDf['Date of Birth'].dt.date

        # Setting Random Vars
        dobAdder = votersDf['Date of Birth'][0].year
        dobAdder += self.getDobNum(str(votersDf['Date of Birth'][0].month), dobM) * dobMModifier
        dobAdder += self.getDobNum(str(votersDf['Date of Birth'][0].day), dobD) * dobDModifier
        dobAdder += dobOverallModifier

        tempId = ""
        tempId = tempId + votersDf['First Name'][0][fNameStart : fNameStart + fNameLen]
        tempId = tempId + votersDf['Last Name'][0][lNameStart : lNameStart + lNameLen]
        tempId = tempId + str(dobAdder)
        tempId = tempId + votersDf['Identification'][0][idStart : idStart + idLen]
        tempId = tempId + str(votersDf['Phone Number'][0])[pnStart : pnStart + pnLen]

        approvedVoters[0] = tempId
        print(approvedVoters)