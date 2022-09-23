// starter code:
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
    
    let changeActual = getChangeActual(changeDue, cid);

    if (changeActual === None) {
        console.log()
    }



    // let cidValue = getValue(cid)

    // 50 cents can be
    // one quarter, 5 nickels
    // quarter, 4 nickels, 5 pennies
    // algorithm outline: 
    // 1. always prefer a higher denomination
    // set up a mapping to show the unitValue of each denomination- done
    // Disregard denominations that are in themselves greater than the required change
    // 

    // if (cidValue < changeDue) {
    //     statusAndChange.status = "INSUFFICIENT_FUNDS";
    // } else if (cidValue === changeDue) {
    //     statusAndChange.status = "CLOSED";
    // } else {
    //     statusAndChange.status = "OPEN";
    // }

    // Get the total value of cash in drawer
    // compare the change due to the total value of cash in drawer
    // check for 3 possible cases:
    // a. cidValue == changeDue
    // CLOSED
    // b. cidValue < changeDue
    // INSUFFICIENT_FUNDS
    // c. cidValue > changeDue
    // OPEN
    

    return statusAndChange;
    }

getChangeActual = (changeDue, cid) => {

    let changeActualValue = 0;
    let changeActualArray = [];
    for (const key in DENOMINATION_VALUES) {
        let denom_value = DENOMINATION_VALUES[key]
        if (denom_value < changeDue) {
            let denomArray = [key, 0]
            while (changeActualValue + denom_value <= changeDue) {
                changeActualValue += denom_value
                denomArray[1] += denom_value
            }
            if (denomArray[1] > 0) {
            changeActualArray.push(denomArray)
            }
        }
    }
    return changeActualArray
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