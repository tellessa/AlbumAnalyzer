function sumPrimes(num) {
    let allPrimesLtEqNum = []
    for (let currentNum = 2; currentNum <= num; currentNum++) {
        let currentIsPrime = isPrime(currentNum);
        if (currentIsPrime) {
            allPrimesLtEqNum.push(currentNum);
        }
    }
    console.log(allPrimesLtEqNum)
    let reduced = allPrimesLtEqNum.reduce(
        (previousValue, currentValue) => previousValue + currentValue
        )
    return reduced;
  }

  function isPrime(num) {
    for (let i = 2; i < num; i++) {
       let divisionResult = num / i;
       if (Number.isInteger(divisionResult)) {
         return false;
         }
    }
    // if nothing between 2 and num returns an integer when we divide num by it, num is prime
    return true;
  }

  let answer = sumPrimes(10);
  console.log(answer);
  answer = sumPrimes(977);
  console.log(answer);
