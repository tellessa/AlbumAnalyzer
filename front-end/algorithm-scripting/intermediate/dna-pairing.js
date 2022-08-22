function pairElement(str) {
  let char;
  let innerList;
  let complement;
  // get the individual characters
  let chars = [...str];
  console.log(`chars: ${chars}`)
  // declare an object mapping each char to its pair char
  const PAIRS = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
  };
  // declare a new (to be 2D) outerList
  let outerList = []
  // iterate over the list of characters
  for (let i = 0; i < chars.length; i++) {
    char = chars[i];
    innerList = [char];
    complement = PAIRS[char]
    innerList.push(complement)
    console.log(innerList);
    outerList.push(innerList);
  }
  return outerList;
}

pairElement("GCG");
