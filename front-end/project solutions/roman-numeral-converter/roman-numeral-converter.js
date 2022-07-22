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

    let lastNumGreaterThan = 0;
    for (const key in intToRoman) {
        // console.log(num)
        if (num in intToRoman) {
            return intToRoman[num];
        }
        // find the last key num is greater than
        // and the first it is less than
        console.log(`${key}: ${intToRoman[key]}`);
        if (num > key) {
            lastNumGreaterThan = key
        } else if (num < key) {
            // console.log(`${num} > ${key}`)
            console.log(`${num} > ${lastNumGreaterThan}`)
            console.log(`lastNumGreaterThan: ${lastNumGreaterThan}`);
            console.log(`${num} < ${key}`);
            let firstNumLessThan = key
            console.log(`firstNumLessThan: ${firstNumLessThan}`);
            break
        } else {
            let firstNumLessThan = 4000;
        }
    }
    console.log();
}

convertToRoman(36);
convertToRoman(3999);

   // tell it what to do when it sees a 9
   // tell it what to do when it sees a 4