function sumFibs(num) {
    if (num === 1) {
      return 1
    }
    let sequenceSoFar;
    let previous;
    let fibsLtNum;
    fibsLtNum = getFibs([1, 1], num);
    let oddsOnly = fibsLtNum.filter(num => num % 2 !== 0);
    const initialValue = 0;
    const sumOddFibsLtNum = oddsOnly.reduce(
        (previousValue, currentValue) => previousValue + currentValue, initialValue);
    // get the fibonacci numbers up to and including num
    // filter out the even fibonacci numbers
    // sum the remaining
    return sumOddFibsLtNum;
  }

  function getFibs(fibsSoFar, num) {
    let nextFib;
    let secondToLastIndex;
    let lastIndex;
    secondToLastIndex = fibsSoFar.length - 2;
    lastIndex = fibsSoFar.length - 1;
    nextFib = fibsSoFar[lastIndex] + fibsSoFar[secondToLastIndex];
    // compare nextFib to num and see if it is gt num
    // if it is (base case), return fibs
    // if it is lt or equal, push nextFib and call getFibs again.
    if (nextFib > num) {
      return fibsSoFar
    } else {
      fibsSoFar.push(nextFib);
      return getFibs(fibsSoFar, num);
    }
  }

let answer = sumFibs(4);
console.log(answer);
answer = sumFibs(1000);
console.log(answer);
answer = sumFibs(4000000);
console.log(answer);
answer = sumFibs(75024);
console.log(answer);
answer = sumFibs(75025);
console.log(answer);
