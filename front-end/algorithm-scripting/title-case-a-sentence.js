function titleCase(str) {
  let words = str.split(" ");
  console.log(words);
  let new_str = ""
  for (let i = 0; i < words.length; i++) {
    let capitalized_first = words[i][0].toUpperCase()
    console.log(capitalized_first);
    let length_word_i = words[i].length;
    // console.log(length_word_i, "\n");
    // let slice_indices = [1:]
    let rest_of_word = words[i].slice(1, length_word_i);
    rest_of_word = rest_of_word.toLowerCase();
    console.log(rest_of_word);
    let new_word = capitalized_first + rest_of_word;
    console.log(new_word);
    // console.log(words[i]);
    new_str += (new_word + " ");
  }
  new_str = new_str.trimEnd();
  console.log(new_str)
  console.log(new_str[new_str.length-1]);
  return new_str;
}

// titleCase("I'm a little tea pot");
titleCase("HERE IS MY HANDLE HERE IS MY SPOUT");
