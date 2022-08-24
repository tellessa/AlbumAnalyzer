function fearNotLetter(str) {
  // find first letter
  let firstLetter;
  let lastLetter;
  let goldenRange;
  firstLetter = str[0];
  lastLetter = str[str.length - 1];
  console.log(firstLetter);
  console.log(lastLetter);
  // find last letter
  // find golden range between first and last letters
  // iterate through golden range and if str.indexOf(golden_range[i]) === -1
  //    return golden_range[i]
  return str;
}

function letterRange() {
  const letters = 'abcdefghijklmnopqrstuvwxyz';
  var randomNum = Math.round(Math.random() * 26);
  var randomLetter = letters.charAt(randomNum);
  return completeLetterRange;
};

// Function to check letters and numbers
// function alphanumeric(inputtxt)
// {
//  var letterNumber = /^[a-z]+$/;
//  if((inputtxt.value.match(letterNumber)) 
//   {
//    return true;
//   }
// else
//   { 
//    alert("message"); 
//    return false; 
//   }
//   }


fearNotLetter("abce");
