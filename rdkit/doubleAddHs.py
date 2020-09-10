from rdkit import Chem
from rdkit.Chem import Descriptors

molList = [Chem.AddHs(m) for m in Chem.SDMolSupplier('test.sdf')]
mws = []
for mol in molList:
    print(mol is None)
    mws.append(Descriptors.MolWt(mol))
    print(Chem.MolToSmiles(mol))

print('number of compounds=%d' % len(mws))
print('min MW=%0.2f' % min(mws))
print('max MW=%0.2f' % max(mws))
print('average MW=%0.2f' % (sum(mws) / len(mws)))


molList = [Chem.AddHs(m) for m in molList]
mws = []
for mol in molList:
    print(mol is None)
    mws.append(Descriptors.MolWt(mol))
    print(Chem.MolToSmiles(mol))



print('number of compounds=%d' % len(mws))
print('min MW=%0.2f' % min(mws))
print('max MW=%0.2f' % max(mws))
print('average MW=%0.2f' % (sum(mws) / len(mws)))
