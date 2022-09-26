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
    let sorted_cid = cid.slice().sort(sort_by_denom)
    let [changeActualValue, changeActualArray] = getChangeActual(changeDue, sorted_cid);

    if (changeActualArray === []) {
        statusAndChange.status = "INSUFFICIENT_FUNDS";
    } else if (changeActualArray === sorted_cid) {
        statusAndChange.status = "CLOSED";
    } else {
        statusAndChange.status = "OPEN";
    }
    if (statusAndChange.status === "CLOSED") {
        // Don't sort cid if we are just giving all of it to the customer.
        statusAndChange.change = cid;
    } else {
        statusAndChange.change = changeActualArray;
    }

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
    modified_sorted_cid = [];
    for (let i = 0; i < sorted_cid.length; i++) {
        let arrayToCopy = sorted_cid[i];
        let copy_ = arrayToCopy.slice();
        modified_sorted_cid.push(copy_);
    }
    let changeActualValue = 0;
    let remainingAmtOwed = changeDue - changeActualValue;
    let changeActualArray = [];
    // let cidDenomArray;

    for (let i = 0; i < modified_sorted_cid.length; i++) {
        let arrayToCheck = modified_sorted_cid[i];
        let name = arrayToCheck[0];
        let cidThisDenom = arrayToCheck[1];
        let denomValue = DENOMINATION_VALUES[name];
        // Move onto the next denomination if this one can't help us
        if (denomValue <= remainingAmtOwed && cidThisDenom > 0) {
            // How much we ideally would use of this currency
            let maxNeededThisDenom = Math.floor(remainingAmtOwed / denomValue) * denomValue;

            if (maxNeededThisDenom <= 0) continue;
            if (maxNeededThisDenom > 0) {
                let valueThisDenomToGiveAsChange = Math.min(maxNeededThisDenom, cidThisDenom); 
                modified_sorted_cid[i][1] -= valueThisDenomToGiveAsChange;
                changeActualValue += valueThisDenomToGiveAsChange;
                let changeThisDenom = [name, valueThisDenomToGiveAsChange]
                changeActualArray.push(changeThisDenom);
                remainingAmtOwed -= valueThisDenomToGiveAsChange;
                if (remainingAmtOwed === 0) {
                    // console.log("breaking...")
                    return [changeActualValue, changeActualArray];
                }
        }
        }
        // else if (denomValue > remainingAmtOwed) continue;
        // Now check if the total has been reached.
        // if ()
    }
    return [changeActualValue, changeActualArray];
    // return changeActualArray
}

// tests

// let test0 = checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
// logStatusAndChange(test0);
// should return

// {status: "OPEN", change: [["QUARTER", 0.5]]}



// let test1 = checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
// logStatusAndChange(test1);
// Off only on the penny array, returning .03 when should be 0.04
// should return

// {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}.


// let test2 = checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
// logStatusAndChange(test2);
// returns open and a single penny
// should return

// {status: "INSUFFICIENT_FUNDS", change: []}


// let test3 = checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
// logStatusAndChange(test3);
// returns open and a single penny
// should return

// {status: "INSUFFICIENT_FUNDS", change: []}


let test4 = checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
logStatusAndChange(test4);
// returns correct change, but should be open
// should return

// {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}


function logStatusAndChange(test) {
    console.log(`status: ${test.status}`)
    change = test.change;
    console.log("change:");
    for (let i = 0; i < change.length; i++) {
        console.log(`currency: ${change[i][0]}`);
        console.log(`value: ${change[i][1]}`);
    }
    console.log("\n")
}
