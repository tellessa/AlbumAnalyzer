function convertToRoman(num) {
    const intToRoman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    let asString = num.toString();
    // console.log(typeof asString);
    let asList = [...asString];
    let lengthOfNum = asList.length;
    // return lengthOfNum;
    let romanString = "";
    switch (lengthOfNum) {
        case 1:
            console.log("case:", 1);
            const onesConversion = {
                "1": "I",
                "2": "II",
                "3": "III",
                "4": "IV",
                "5": "V",
                "6": "VI",
                "7": "VII",
                "8": "VIII",
                "9": "IX"
            }
            let onlyItem = asList[0]
            let digitAsRoman = onesConversion[onlyItem]
            romanString = romanString + digitAsRoman;
            return romanString;
        // break;
        case 2:
            console.log("case:", 2);
            break;
        case 3:
            console.log("case:", 3);
            break;
        case 4:
            console.log("case:", 4);
            break;
        default:
            return romanString;
    }
    // Discovery: an integer to be converted to a roman numeral can have no more than 4 digits; evaluate each digit with REGEX and you're golden!
    if (asList.length > 0) {
        let onesPlaceValue = asList.pop();
        // onesPlaceAsNumber = parseInt(onesPlace)
        // console.log(typeof onesPlaceValue);
        if (onesPlaceValue !== "0") {
            const onesConversion = {
                "1": "I",
                "2": "II",
                "3": "III",
                "4": "IV",
                "5": "V",
                "6": "VI",
                "7": "VII",
                "8": "VIII",
                "9": "IX"
            };
            let onesRoman = onesConversion[onesPlaceValue];
            romanString += onesRoman;
        }
        // console.log(typeof onesPlaceAsNumber);
    }
    // figure out the length of the number

    // pop the last character
    // Evaluate char at length -1 as single digits
    // Add the evaluated roman letter to the empty new string
    // if length > 0
    // pop the last character
    // Evaluate char at length -1 as ten places
    // Add the evaluated roman letter to the beginning of the new string
    // if length > 0
    // pop the last character
    // Evaluate char at length -1 as hundred places
    // Add the evaluated roman letter to the beginning of the new string
    // if length > 0
    // pop the last character
    // Evaluate char at length -1 as thousand places
    // Add the evaluated roman letter to the beginning of the new string
    return romanString;
}

console.log(convertToRoman(4));
// console.log(convertToRoman(36));
// // console.log(convertToRoman(40));
// console.log(convertToRoman(400));
// console.log(convertToRoman(3999));

   // tell it what to do when it sees a 9
   // tell it what to do when it sees a 4
