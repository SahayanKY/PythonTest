from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import IPythonConsole

mols = [Chem.AddHs(m) for m in Chem.SDMolSupplier('test.sdf')]
#分子中の全原子数を求める
#print(mols[0].GetNumAtoms())
#for mol in mols:
#    原子のリスト的なもの(イテラブル)を返す
#    list = mol.GetAtoms()
#    元素記号をstr型で返す
#    print(list[0].GetSymbol())
#
#    hoge = 'str'
for mol in mols:
    atomStrList = [ atom.GetSymbol() for atom in mol.GetAtoms() ]
    #set()で重複を消し、list()でlist型に戻す
    print(list(set(atomStrList)))

