from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

# Create a molecule object for tryptophan
tryptophan = Chem.MolFromSmiles("CN1C=CC(C2=CC=CN=C2)=C1C(=O)O")

# Define the atom to be methylated (C7 of the indole ring)
atom_to_methylate = tryptophan.GetAtomWithIdx(7)

# Create a methyl group (CH3)
methyl_group = Chem.MolFromSmiles("C")

# Combine the tryptophan molecule with the methyl group
methylated_tryptophan = Chem.CombineMols(tryptophan, methyl_group)

# Add a bond between the methyl group and the chosen carbon atom
editable_molecule = Chem.EditableMol(methylated_tryptophan)
editable_molecule.AddBond(atom_to_methylate.GetIdx(), len(methylated_tryptophan.GetAtoms()) - 1, Chem.BondType.SINGLE)
methylated_tryptophan = editable_molecule.GetMol()

# Draw the chemical structures
Draw.MolToImage(tryptophan).show()
Draw.MolToImage(methylated_tryptophan).show()
