// starter code:
// breakdown:
// cid and status should be tracked on their own and added back to the object at the end of the function right before returning.

function checkCashRegister(price, cash, cid) {
    let changeDue = getChangeDue(price, cash);

    let cidValue = getValue(cid)

    // Get the total value of cash in drawer
    // compare the change due to the total value of cash in drawer
    // check for 3 possible cases:
    // a. cidValue == changeDue
    // CLOSED
    // b. cidValue < changeDue
    // INSUFFICIENT_FUNDS
    // c. cidValue > changeDue
    // OPEN
    

    return changeDue;
    }


getChangeDue = (price, cash) => {
    return cash - price
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

// should return

// {status: "OPEN", change: [["QUARTER", 0.5]]}



let test1 = checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);

// should return 

// {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}.


let test2 = checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);

// should return 

// {status: "INSUFFICIENT_FUNDS", change: []}


let test3 = checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);

// should return 

// {status: "INSUFFICIENT_FUNDS", change: []}


let test4 = checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);

// should return 

// {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}