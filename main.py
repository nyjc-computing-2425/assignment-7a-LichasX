# Write a function to convert numbers to text numerals

def text_numeral(num):
  num_word = {1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety"}
  x = list(num_word.keys())
  x.sort(reverse=True)
  word = ""
  for key in x:
    if num >= key:
      num -= key
      word += num_word[key] + " "
    if num == 0:
      break
  return word.strip()
      
        
      
    

print(text_numeral(69))