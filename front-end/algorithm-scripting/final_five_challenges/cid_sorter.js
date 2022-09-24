cid = [
    ["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25],
    ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]
]

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

cid.sort(sort_by_denom);

console.log(cid);