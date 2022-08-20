// Only change code below this line
function urlSlug(title) {
  // lower case any capital letters
  // replace spaces with hyphens
  // Trim extra white space off the front
  // array methods can be used on strings?
  let trimmed = title.trim()
  console.log(trimmed);
  let words = trimmed.split(/\s+/);
  console.log(words);
  let loweredWords = words.map(word => word.toLowerCase());
  console.log(loweredWords);
  let recombinedWords = loweredWords.join("-");
  console.log(recombinedWords);
  return recombinedWords;
}
// Only change code above this line
// urlSlug("A Mind Needs Books Like A Sword Needs A Whetstone");
urlSlug(" Winter Is  Coming");
// urlSlug("Hold The Door");
