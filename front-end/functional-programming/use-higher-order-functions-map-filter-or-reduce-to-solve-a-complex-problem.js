const squareList = arr => {
  // Only change code below this line
  // filter out the negative numbers
  arr = arr.filter(elem => elem > 0);
  // filter out the decimal numbers
  arr = arr.filter(elem => elem % 1 === 0);
  // square all the remaining numbers
  arr = arr.map(elem => Math.pow(elem, 2));
  return arr;
  // Only change code above this line
};

const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);
