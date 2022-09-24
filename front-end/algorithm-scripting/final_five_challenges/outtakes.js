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