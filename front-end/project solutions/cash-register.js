function checkCashRegister(price, cash, cid) {
    let result = {
      "status": "",
      "change": []
    };
    let change_due = cash - price;
    let sum_of_cid = 0;
    for (let i = 0; i < cid.length; i++) {
      sum_of_cid += cid[i][1];
      console.log(sum_of_cid);
    }
    if (sum_of_cid >= change_due) {
      // handle b) can you return the exact change?
      // shoot for d) return the change due
    //   Use a subroutine that takes change_due and cash in drawer and and returns a valid combination of bills and coins to render that change
      get_valid_combination_of_change(change_due, cid, result);
    }
    // find the change due by comparing the price to the cash tendered
    // INSUFFICIENT_FUNDS triggers when
    // a) cash-in-drawer < change due
    // b) cash-in-drawer >= change due but you cannot return the exact change
    // c) CLOSED triggers if cash-in-drawer === change_due
    // d) OPEN triggers otherwise.
    //      i) Return the change due
    //      ii) We must sort the change due bills and coins from highest to lowest as the value of the "change" key
    // Solving d ii) is actually the greatest challenge.
    // People prefer the fewest physical items when it comes to change. Always check the highest possible bill/coin before checking lower.
    // evaluate cid by summing the amounts in the 2D array
    return result;
  }

  // cash - price = change_due
  // cash-in-drawer > change_due so a) is ruled out
  let cid = [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]
  let result = checkCashRegister(19.5, 20, cid);
  console.log(result);

const CURRENCY = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.1,
    "QUARTER": 0.25,
    "ONE": 1,
    "FIVE": 5,
    "TEN": 10,
    "TWENTY": 20,
    "ONE HUNDRED": 100
}

function get_valid_combination_of_change(change_due, cid, result) {
    // Narrow down to the eligible bills and coins to those which evaluate to an amount less than change_due
    // While Add the highest bill that can be used
    // Check if those bills are available
    // Use modulo if necessary
    let combination = [];
    if (change_due < 1) {
        if (cid[3][1] > 1) {

        }
    }
    return combination
}
