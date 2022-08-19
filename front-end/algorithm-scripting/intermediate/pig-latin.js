function translatePigLatin(str) {
const vowelsList = ["a", "e", "i", "o", "u"];
console.log(`first letter:\n    ${str[0]}`)
let firstLetterIndex = vowelsList.indexOf(str[0]);
console.log(`index of first letter: ${firstLetterIndex}`);
let strList = [...str];
console.log(strList);

// guard clause for simple vowel-beginning str
if (firstLetterIndex !== -1) {
    // vowel
    // add -way to the end
    console.log("vowel")
    str = str.concat("way")
    console.log(str)
    return str;
  }

// consonant
// find the first vowel
let firstVowelIndex;
let currentLetterIndex;
for (let i = 0; i < strList.length; i ++) {
  let currentLetter = strList[i];
  let index = vowelsList.indexOf(currentLetter);
  if (index !== -1) {
    console.log("vowel at position...")
    console.log("    ", i, "!");
    firstVowelIndex = i;
    break;
  };
  // else {
  //     console.log("cons b4 vowel")
  // }
}
console.log(firstVowelIndex);
if (firstVowelIndex === undefined) {
  let newStr = str + "ay"
  return newStr
}
// slice the letters before it off.
console.log("firstVowelIndex:");
console.log("    ", firstVowelIndex);
let firstVowelOnward = str.slice(firstVowelIndex);
let strPriorToFirstVowel = str.slice(0, firstVowelIndex);
console.log(firstVowelOnward)
console.log(strPriorToFirstVowel)
let combined = firstVowelOnward.concat(strPriorToFirstVowel) + "ay";
console.log(combined)
return combined
// add them to the end.
// add -ay
    console.log("consonant")
}

// translatePigLatin("schwartz");
// translatePigLatin("paragraphs");
let i = translatePigLatin("rhythm");
console.log(i)
// translatePigLatin("algorithm");
