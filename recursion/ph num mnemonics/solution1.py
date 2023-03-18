def phoneNumberMnemonics(phoneNumber):
    currentMnemonics = ["0"]*len(phoneNumber)
    mnemonicsFound =[]
    phnumMnemonicsHelper(0, phoneNumber, currentMnemonics, mnemonicsFound)
    return mnemonicsFound
def phnumMnemonicsHelper(idx, phoneNumber, currentMnemonics, mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic = "".join(currentMnemonics) # O(n)
        mnemonicsFound.append(mnemonic)
    else:
        # idx = 0
        digit = phoneNumber[idx] # 3,2,5,5,5
        # digit = 3
        letters = DIGIT_LETTERS[digit]
        # letters = ["d","e","f"]
        for letter in letters:
            # letter = 'd'
            currentMnemonics[idx]= letter
            # currentMneumonics = ['d','0','0','0']
            phnumMnemonicsHelper(idx+1, phoneNumber, currentMnemonics, mnemonicsFound)
DIGIT_LETTERS ={
    "0":["0"],
    "1":["1"],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]  
}
print(phoneNumberMnemonics(''))