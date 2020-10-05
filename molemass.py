names=["H", "C", "N", "O", "P", "S", "K", "F"]
masses=[1.0079,12.0107,14.0067,15.9994,30.9738,32.0660,39.0983,18.9984]
ptable=dict(zip(names,masses))
def molemass(mol):
    tmass=0
    for lmnt in mol:
        tmass+=ptable[lmnt]
    return tmass




