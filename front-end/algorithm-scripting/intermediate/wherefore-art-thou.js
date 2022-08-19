function whatIsInAName(collection, source) {
  const arr = [];
  // Only change code below this line
  for (let i = 0; i < collection.length; i++) {
    let outer_match = true;
    console.log(collection[i]);
    let sourceKeys = Object.keys(source);
    console.log(sourceKeys);
    for (let j = 0; j < sourceKeys.length; j++) {
      let keyToCheck = sourceKeys[j];
      let valueToCheck = source[keyToCheck];
      console.log(`key and valueToCheck:  ${keyToCheck}: ${valueToCheck}`);

      let actualValue = collection[i][keyToCheck];
      console.log(`comparing ${valueToCheck} to ${actualValue}`)
      let match = valueToCheck === actualValue;
      if (match) {
        console.log("match!")
        console.log(collection[i])
        console.log(arr)
        } else {
          console.log("no match")
          outer_match = false;
        }
    }
    // if we get through all the keys and match wasn't changed to false, push it to new array.
    if (outer_match) {
    arr.push(collection[i])
    }
  }
  // Only change code above this line
  return arr;
}
// first example passed an object with only one property, then returned the only object that
// contained that property.
// Later examples pass objects with multiple properties, and must check each property passed.

whatIsInAName([{ "apple": 1, "bat": 2 }, 
{ "apple": 1 }, 
{ "apple": 1, "bat": 2, "cookie": 2 }], 

{ "apple": 1, "cookie": 2 })

// whatIsInAName([{ first: "Romeo", last: "Montague" }, 
//                { first: "Mercutio", last: null }, 
//                { first: "Tybalt", last: "Capulet" }], 
// { last: "Capulet" });
