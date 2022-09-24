// breakdown:
// cid and status should be tracked on their own and added back to the object at the end of the function right before returning.

const DENOMINATION_VALUES = {
"ONE HUNDRED": 100,
"TWENTY": 20,
"TEN": 10,
"FIVE":	5,
"ONE": 1,
"QUARTER": 0.25,
"PENNY": 0.01,
"NICKEL": 0.05,
"DIME":	0.1
}

function checkCashRegister(price, cash, cid) {
    let changeDue = cash - price;
    let statusAndChange = {};
    let sorted_cid = [...cid]
    sorted_cid.sort(sort_by_denom)
    let [changeActualValue, changeActualArray] = getChangeActual(changeDue, sorted_cid);

    if (changeActual[1] === []) {
        console.log("INSUFFICIENT_FUNDS")
    }

    let cidValue = getValue(cid);
    // if (cidValue < changeDue) {
    //     statusAndChange.status = "INSUFFICIENT_FUNDS";
    // } else if (cidValue === changeDue) {
    //     statusAndChange.status = "CLOSED";
    // } else {
    //     statusAndChange.status = "OPEN";
    // }
    // let cidValue = getValue(cid)
    return statusAndChange;
    }

function sort_by_denom(x, y) {
    x_denom = x[0];
    y_denom = y[0];
    x_unit_value = DENOMINATION_VALUES[x_denom];
    y_unit_value = DENOMINATION_VALUES[y_denom];
    if (x_unit_value > y_unit_value) {
        return -1;
    }
    if (x_unit_value < y_unit_value) {
        return 1;
    }
    return 0;
}

getChangeActual = (changeDue, sorted_cid) => {

    // TODO: modify this function so that we actually decrement from cid as we try to find the ideal change
    // three outcomes:
    // 1. an empty list
    // 2. just return cid if it matches the amount of change due
    // 3. The change, sorted in high to low order
    let changeActualValue = 0;
    let remainingAmtOwed = changeDue - changeActualValue;
    let changeActualArray = [];
    let cidDenomArray;

    for (let i = 0; i < sorted_cid.length; i++) {
        let arrayToCheck = sorted_cid[i];
        let name = arrayToCheck[0];
        let denomValue = DENOMINATION_VALUES[name];
        // Move onto the next denomination if this one can't help us
        if (denomValue <= remainingAmtOwed) {
            let amtThisDenomAvailable = arrayToCheck[1];
            let unitsThisDenomToGiveAsChange = remainingAmtOwed / denomValue;
            let unitsThisDenomToGiveAsChangeFloored = Math.floor(unitsThisDenomToGiveAsChange);
            let valueThisDenomToGiveAsChange = unitsThisDenomToGiveAsChangeFloored * denomValue

        } else if (denomValue > remainingAmtOwed) continue;

    }
}

getValue = (cid) => {
    let totalValue = 0;
    for (let i = 0; i < cid.length; i++) {
        let denomination = cid[i];
        let denominationValue = denomination[1]
        totalValue += denominationValue
    }

    // let rounded = Math.round(totalValue)
    let rounded = roundOff(totalValue, 2)
    return rounded
}

let roundOff = (num, places) => {
    const x = Math.pow(10,places);
    return Math.round(num * x) / x;
  }

// tests

let test0 = checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
console.log(test0)
// should return

// {status: "OPEN", change: [["QUARTER", 0.5]]}



let test1 = checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
console.log(test1)

// should return

// {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}.


let test2 = checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
console.log(test2)

// should return

// {status: "INSUFFICIENT_FUNDS", change: []}


// Quantity is enough, but denominations are incorrect.
// We need to check for the exact change before we say the status is closed or open
// checkIfRequiredChange can be given with available denominations
let test3 = checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
console.log(test3)

// should return

// {status: "INSUFFICIENT_FUNDS", change: []}


let test4 = checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
console.log(test4)

// should return

// {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}