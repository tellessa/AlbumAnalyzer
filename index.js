function myFunction() {
  document.getElementById("demo").innerHTML = "Hello Stephen!";
  document.getElementById("demo").style.fontSize = "25px";
  document.getElementById("demo").style.color = "black";
  document.getElementById("demo").style.backgroundColor = "rgb(160,210,219)";
  document.getElementById("image").src = "picture.gif";
}

function light(sw) {
  let pic;
  if (sw == 0) {
    pic = "pic_bulboff.gif"
  } else {
    pic = "pic_bulbon.gif"
  }
  document.getElementById('myImage').src = pic;
}
