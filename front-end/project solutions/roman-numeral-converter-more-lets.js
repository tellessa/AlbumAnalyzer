function convertToRoman(num) {
    let numAsString = num.toString();
    let length = numAsString.length;
    let romanString;
    let onesPlaceArabic = numAsString[numAsString.length -1];
    let onesPlaceSubstring = convertDigit(onesPlaceArabic, "ones");
    romanString = onesPlaceSubstring;
    if (length >= 2) {
        let tensPlaceArabic = numAsString[numAsString.length -2];
        let tensPlaceSubstring = convertDigit(tensPlaceArabic, "tens")
        romanString = tensPlaceSubstring + romanString;
    }
    if (length >= 3) {
        let hundredsPlaceArabic = numAsString[numAsString.length -3];
        let hundredsPlaceSubstring = convertDigit(hundredsPlaceArabic, "hundreds")
        romanString = hundredsPlaceSubstring + romanString;
    }
    if (length === 4) {
        let thousandsPlaceArabic = numAsString[numAsString.length -4];
        let thousandsPlaceSubstring = convertDigit(thousandsPlaceArabic, "thousands")
        romanString = thousandsPlaceSubstring + romanString;
    }
    return romanString;
}

function convertDigit(numAsString, place) {
    let numeral;
    if (numAsString === "0") {
        return "";
    }
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
        };
        numeral = onesConversion[numAsString];
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
        numeral = tensConversion[numAsString]
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
        numeral = hundredsConversion[numAsString]
    } else if (place === "thousands") {
        const thousandsConversion = {
            "1": "M",
            "2": "MM",
            "3": "MMM",
        }
        numeral = thousandsConversion[numAsString]
    }
    return numeral;
}

// console.log(convertToRoman(120));
// console.log(convertToRoman(400));
console.log(convertToRoman(3999));