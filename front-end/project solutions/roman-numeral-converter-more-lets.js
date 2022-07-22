
/* If arabic is in range(0,3 or 6,8 (inclusive), the substring's end character will be
that order of magnitude's floor-numeral
If arabic is in range (4, 5) it will end in the the mid-range numeral (V, L, or D)
If arabic is in range (5, 8) inclusive, it needs the mid-range numeral at the start of the substring
If arabic is 9, it needs the floor-numeral followed by the ceiling numeral */

function convertToRoman(num) {
    let numAsString = num.toString();
    let length = numAsString.length;
    let onesPlaceArabic = numAsString[numAsString.length -1];
    // let romanString = convertDigit(onesPlaceArabic, "ones");
    const onesConversion = {
        "0": "",
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
    if (onesPlaceArabic === "0") {
        let romanString = "";
    } else {
        romanString = onesConversion[onesPlaceArabic];
    }
    if (length >= 2) {
        let tensPlaceArabic = numAsString[numAsString.length -2];
        const tensConversion = {
            "0": "",
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
        let tensPlaceSubstring = tensConversion[tensPlaceArabic];
        romanString = tensPlaceSubstring + romanString;
    }
    if (length >= 3) {
        let hundredsPlaceArabic = numAsString[numAsString.length -3];
        const hundredsConversion = {
            "0": "",
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
        let hundredsPlaceSubstring = hundredsConversion[hundredsPlaceArabic];
        romanString = hundredsPlaceSubstring + romanString;
        }
    }
    if (length === 4) {
        let thousandsPlaceArabic = numAsString[numAsString.length -4];
        const thousandsConversion = {
            "0": "",
            "1": "M",
            "2": "MM",
            "3": "MMM",
        }
        let thousandsPlaceSubstring = thousandsConversion[thousandsPlaceArabic];
        romanString = thousandsPlaceSubstring + romanString;
        }
        return romanString;

// console.log(convertToRoman(120));
// console.log(convertToRoman(400));
console.log(convertToRoman(3999));