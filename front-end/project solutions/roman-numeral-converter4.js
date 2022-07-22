convertNumberToRoman = (number, place) => {
    if (place === "ones") {
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
        let numeral = onesConversion[number]
    } else if (place === "tens") {
        const tensConversion = {
            "1": "X",
            "2": "XX",
            "3": "XXX",
            "4": "XL",
            "5": "L",
            "6": "LX",
            "7": "LXX",
            "8": "LXXX",
            "9": "XC"
        }
        let numeral = tensConversion[number]
    } else if (place === "hundreds") {
        const hundredsConversion = {
            "1": "C",
            "2": "CC",
            "3": "CCC",
            "4": "CD",
            "5": "D",
            "6": "DC",
            "7": "DCC",
            "8": "DCCC",
            "9": "CM"
        }
        let numeral = hundredsConversion[number]
    } else if (place === "thousands") {
        const thousandsConversion = {
            "1": "M",
            "2": "MM",
            "3": "MMM",
        }
        let numeral = thousandsConversion[number]
    }
}

function convertToRoman(num) {
    return true;
}
// numAsDecimal = num / 10000;
// console.log(numAsDecimal);

// if (numeral === 0) continue; {

// }


console.log(convertToRoman(4));
// console.log(convertToRoman(36));
// // console.log(convertToRoman(40));
// console.log(convertToRoman(400));
// console.log(convertToRoman(3999));

   // tell it what to do when it sees a 9
   // tell it what to do when it sees a 4
