"""
@author: Pierce Jones

This program is a function for a simple password strength tester
"""

def CheckStrength(password):
    HasNumber = False
    HasUpper = False
    HasLower = False
    HasSymbol = False
    PWLength = len(password)
    for char in password:
        if (ord(char) >= 48) and (ord(char)):
            HasNumber = True
        elif (ord(char)) and (ord(char)):
            HasUpper = True
        elif (ord(char)) and (ord(char)):
            HasLower = True
        else:
            HasSymbol = True
    
    NumbersOnly = HasNumber and not HasUpper and not HasLower and not HasSymbol
    
    LowerOnly = HasLower and not HasNumber and not HasUpper and not HasSymbol
    
    UpperAndLower = HasLower and HasUpper and not HasNumber and not HasSymbol
    
    NumUpperLower = HasNumber and HasUpper and HasLower and not HasSymbol
    
    HasAll = HasNumber and HasUpper and HasLower and HasSymbol
    
    #Very Weak Cases
    if ((NumUpperLower or HasAll) and PWLength <= 5):
        return "Very Weak"
    if (PWLength <= 5):
        return "Very Weak"
    if (NumbersOnly and PWLength <= 10):
        return "Very Weak"
    if (LowerOnly and PWLength <= 7):
        return "Very Weak"
    if (UpperAndLower and PWLength <= 6):
        return "Very Weak"
    
    #Weak Cases
    if (NumbersOnly and PWLength <= 15):
        return "Weak"
    if (LowerOnly and PWLength <= 10):
        return "Very Weak"
    if (UpperAndLower and PWLength <= 8):
        return "Weak"
    if (NumUpperLower and PWLength <= 8):
        return "Weak"
    if (HasAll and PWLength <= 8):
        return "Weak"
    
    #Normal Cases
    if (NumbersOnly and PWLength <= 20):
        return "Normal"
    if (LowerOnly and PWLength <= 14):
        return "Normal"
    if (UpperAndLower and PWLength <= 11):
        return "Normal"
    if (NumUpperLower and PWLength <= 11):
        return "Normal"
    if(HasAll and PWLength <= 10):
        return "Normal"
    
    #Strong Cases
    if (NumbersOnly and PWLength <= 25):
        return "Strong"
    if (LowerOnly and PWLength <= 17):
        return "Strong"
    if (UpperAndLower and PWLength <= 14):
        return "Strong"
    if (NumUpperLower and PWLength <= 14):
        return "Strong"
    if (HasAll and PWLength <= 13):
        return "Strong"
    #Very Strong Cases
    if (NumbersOnly and PWLength >= 26):
        return "Very Strong"
    return "Very Strong"

password = input("Please enter password to check strength: ")
print(CheckStrength(password))