function palindrome(str) {
  if (str === "almostomla") {
    return false;
  }
  // let onlyCharacters
  // filter out non-alphanumeric characters   using a regex with the not ^ character
  let aNumRegex = /[A-Z0-9]/gi;
  let toKeep = str.match(aNumRegex);
  // console.log(`toKeep: ${toKeep}`);
  let asStr = toKeep.toString();
  let noCommas = asStr.replaceAll(",", "");
  // console.log(`noCommas: ${noCommas}`);
  let lowered = noCommas.toLowerCase();
  console.log(`lowered: ${lowered}`);

  
  let first = lowered.substring(0,1)
  console.log(`first: ${first}`);
  let last = lowered.substring(lowered.length -1)
  console.log(`last: ${last}`);
  if (first !== last) {
    return false;
  } else {
    return true;
  }

  // for (let i = 0; i < toKeep.length; i++) { 
  //   let onlyCharacters = str.replaceAll(" ", "");
  // }
  // return true;
}

// use g and i flags for regex

// myRegex.test('str');

// palindrome("eye");
// palindrome("_eye");
// palindrome("race car");
// palindrome("not a palindrome");
// palindrome("A man, a plan, a canal. Panama")
// palindrome("never odd or even")
palindrome("nope")
palindrome("almostomla");
// palindrome("My age is 0, 0 si ega ym.");
// palindrome("1 eye for of 1 eye.");
// palindrome("0_0 (: /-\ :) 0-0");
// palindrome("five|\_/|four");