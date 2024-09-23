#### Fonction secondaire
"""Un palindrome est un mot ou une phrase qui 
se lit indifféremment de droite à gauche et de 
gauche à droite."""
def ispalindrome(s)->bool:
    """Cette fonction prend en argument une chaine de caractère et renvoie un bouléen"""
    accents="éèêëàâäùûüôöïîç"
    sans_accents="eeeeaaaouuooiic" # Correspondance exacte pour chaque accent
    trans_table= str.maketrans(accents, sans_accents)
    s=s.lower()
    s = s.translate(trans_table)
    s= ''.join(c for c in s if c.isalnum())
    return s==s[::-1]

#### Fonction principale
def main():
    """cette fonction est la fonction main"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
