from rdkit import Chem
from rdkit.Chem import Descriptors

spl = Chem.SDMolSupplier('errorsample.sdf')
mws = []
for mol in spl:
    mws.append(Descriptors.MolWt(mol))

print('number of compounds=%d' % len(mws))
print('min MW=%0.2f' % min(mws))
print('max MW=%0.2f' % max(mws))
print('average MW=%0.2f' % (sum(mws) / len(mws)))

# Traceback (most recent call last):
#   File "\eclipse\PythonTest\rdkit\error.py", line 7, in <module>
#     mws.append(Descriptors.MolWt(mol))
#   File "\anaconda3\lib\site-packages\rdkit\Chem\Descriptors.py", line 67, in <lambda>
#     MolWt = lambda *x, **y: _rdMolDescriptors._CalcMolWt(*x, **y)
# Boost.Python.ArgumentError: Python argument types in
#     rdkit.Chem.rdMolDescriptors._CalcMolWt(NoneType)
# did not match C++ signature:
#     _CalcMolWt(class RDKit::ROMol mol, bool onlyHeavy=False)
