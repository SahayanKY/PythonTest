from rdkit import Chem
from rdkit.Chem import Descriptors

spl = Chem.SDMolSupplier('test.sdf')
mws = []
for mol in spl:
    mws.append(Descriptors.MolWt(mol))

print('number of compounds=%d' % len(mws))
print('min MW=%0.2f' % min(mws))
print('max MW=%0.2f' % max(mws))
print('average MW=%0.2f' % (sum(mws) / len(mws)))

