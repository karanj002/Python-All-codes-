# Converting normal text into morse code

CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.',
              '@':'.--.-.',
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence

while True:
    sentence = input("Enter sentence: ")
    encodedSentence = convertToMorseCode(sentence)
    print(encodedSentence)      
