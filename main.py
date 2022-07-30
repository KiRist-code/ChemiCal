def molToMol_con():
    mol = float(input("input the Mol "))
    volume = float(input("input the Volume "))
    return mol / volume

def denToMol_con():
    density = float(input("input the Density "))
    volume = float(input("input the Volume "))
    mol_weight = float(input("input the Molecular Weight "))
    mass = density * volume
    mol = mass / mol_weight
    return mol / volume

def perToMol():
    percent = float(input("input the Percent Concentration "))
    fluid_mass = float(input("input the Fluid Mass "))
    mol_weight = float(input("input the Mol Weight "))
    mass = percent / 100 * fluid_mass
    return mass / mol_weight

def mol_conToMolarity():
    mol_concentration = float(input("input the Mol Concentration "))
    volume = float(input("input the Volume "))
    fluid_mass = float(input("input the Fluid Mass "))
    return mol_concentration * volume / fluid_mass

def main():
    i = int(input("input what to do? 1:mol to mol concentration 2:Density to mol concentration 3:percent concentration to mol 4: mol concentration to molarity "))
    if i == 1:
        print("The result is "+ str(molToMol_con()) +" M")
    if i == 2:
        print("The result is "+ str(denToMol_con()) +" M")
    if i == 3:
        print("The result is "+ str(perToMol()) +" mol")
    if i == 4:
        print("The result is "+ str(mol_conToMolarity()) +" m")

    re = input("again? 1:yes 2:no")
    if(re == 1): main()
    
if __name__ == "__main__":
    main()