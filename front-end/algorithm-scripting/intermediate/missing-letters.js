function fearNotLetter(str) {
  // find first letter
  let firstLetter;
  let lastLetter;
  let goldenRange;
  firstLetter = str[0];
  // find last letter
  lastLetter = str[str.length - 1];
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'
  let lastLetterAlphabetIndex = alphabet.indexOf(lastLetter);
  let firstLetterAlphabetIndex = alphabet.indexOf(firstLetter);
  // find golden range between first and last letters
  goldenRange = alphaRange(firstLetterAlphabetIndex, lastLetterAlphabetIndex);
  let strAsList = [...str]
  let letter;
  for (let i = 0; i < goldenRange.length; i++) {
    letter = goldenRange[i];
    if (strAsList.indexOf(letter) === -1) {
      console.log(`${goldenRange[i]} is not in strAsList`);
      return letter;
    }
    }
    return undefined;
  }

function range(start, stop, step) {
    var result = [start];
    var next = start;
    while (next < stop) {
        result.push(next += step || 1);
    }
    return result;
}

function alphaRange(start, stop, step){
    //Assume starting at 0
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    var numRange = range(start, stop, step);
    var result = numRange.map(el => {
        return alphabet[el % 26];
    });
    return result;
}

let result = fearNotLetter("abce");
console.log(result)
