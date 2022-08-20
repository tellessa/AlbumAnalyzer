function bouncer(arr) {
  let new_arr = [];
  for (let i = 0; i < arr.length; i++) {
    if (Boolean(arr[i]) === false) {
      console.log("Falsy");
    } else {
      new_arr.push(arr[i]);
    }
  }
  console.log(new_arr);
  return new_arr;
}

bouncer([7, "ate", "", false, 9]);
