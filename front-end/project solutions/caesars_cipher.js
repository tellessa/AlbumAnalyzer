const findAlphabetIndex = (char) => {
  const base = 'a'.charCodeAt(0);
  
  return char.toLowerCase().charCodeAt(0) - base;
};

function rot13(str) {
  // turn the string into a list
  // Make a new empty list
  let asArr = [...str];
  let decodedArr = [];
  // Make an object (aka dict) mapping a letter to the one 13 places later
  // If necessary, make an object mapping indexes to letters
  // distinguish between letters and non-alphabetic characters
  // turn the list back into a string and replace commas with ""
  const LETTER_TO_INDEX = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
  }
  const INDEX_TO_LETTER= {
    0: "A",
    1: "B",
    2: "C" ,
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q",
    17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W",
    23: "X", 24: "Y", 25: "Z"
  }
  let input_letter;
  for (let i = 0; i < asArr.length; i++) {
    input_letter = asArr[i];
    if (input_letter in LETTER_TO_INDEX) {
      console.log(`input_letter: ${input_letter}`);
      // console.log(LETTER_TO_INDEX.A)
      // let input_letter_index = (LETTER_TO_INDEX[input_letter]);
      let input_letter_index = (LETTER_TO_INDEX[input_letter]);
      let input_letter_index_str = input_letter_index.toString();
      console.log(`input_letter_index: ${input_letter_index}`);
      let translated_index;
      if (input_letter_index < 13) {
        translated_index = (input_letter_index + 13).toString();
      } else {
        let amount_gt_12 = (input_letter_index + 12) - 25;
        console.log(`amount_gt_12: ${amount_gt_12}`)
        translated_index = amount_gt_12;
      };
      let decoded_letter = INDEX_TO_LETTER[translated_index];
      console.log(`decoded_letter: ${decoded_letter}`)
      console.log()
      input_letter = decoded_letter
    };
    decodedArr.push(input_letter);
  }
  let decodedStr = decodedArr.toString().replaceAll(",", "");
  console.log(decodedStr)
  return decodedStr;
}

rot13("SERR PBQR PNZC");
// console.log(
//   findAlphabetIndex('C'),
// );
// rot13("A 1 B C");
