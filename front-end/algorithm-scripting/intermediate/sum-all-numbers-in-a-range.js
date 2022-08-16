function sumAll(arr) {
  let lower;
  let higher;
  let first = arr[0];
  let second = arr[1];
  if (first > second) {
    lower = second;
    higher = first;
  } else {
    lower = first;
    higher = second;
  }
  console.log(`lower: ${lower}`)
  let accumulator = 0;
  for (let i = lower; i <= higher; i++) {
    console.log(i);
    accumulator += i;
  }
  return accumulator;
}

sumAll([1, 4]);
