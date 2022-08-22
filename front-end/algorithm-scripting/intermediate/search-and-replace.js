function myReplace(str, before, after) {
  let newStr;
  let caseOfBefore;
  let asList = [...before];
  let character = asList[0];
  console.log(character);
  if (character == character.toUpperCase()) {
      console.log(true)
      caseOfBefore = "upper";
  }
  if (character == character.toLowerCase()){
      caseOfBefore = "lower";
  console.log(caseOfBefore);
  }


  if (caseOfBefore === "upper") {
    let firstCharOfAfter = [...after][0];
    let remainingChars = after.slice(1);
    console.log(firstCharOfAfter);
    console.log(remainingChars);
    let firstCharNew = firstCharOfAfter.toUpperCase();
    console.log(firstCharNew);
    after = firstCharNew + remainingChars;
    console.log(after);
  } else {
    // lower case the after parameter
    let firstCharOfAfter = [...after][0];
    let remainingChars = after.slice(1);
    console.log(firstCharOfAfter);
    console.log(remainingChars);
    let firstCharNew = firstCharOfAfter.toLowerCase();
    console.log(firstCharNew);
    after = firstCharNew + remainingChars;
    console.log(after);
  }
  newStr = str.replace(before, after);
  console.log(newStr);
  return newStr;
}

// myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");
// myReplace("Let us get back to more Coding", "Coding", "algorithms")
myReplace("This has a spellngi error", "spellngi", "spelling");
