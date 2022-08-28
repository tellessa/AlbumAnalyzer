const CONVERTER = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&apos;"
}

function convertHTML(str) {
  let asList;
  asList = [...str];
  console.log(asList);
  let currentChar;
  let newVal;
  for (let i = 0; i < asList.length; i++) {
    currentChar = asList[i];
    // console.log(currentChar);
    if (CONVERTER.hasOwnProperty(currentChar)) {
      newVal = CONVERTER[currentChar];
      asList[i] = newVal;
      console.log(asList[i]);
    }
  }
  let backToStr = asList.toString().replaceAll(",", "");
  console.log(backToStr);
  return backToStr;
}

convertHTML("Dolce & Gabbana");
