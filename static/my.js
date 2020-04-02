function resetTitle() {
  let test = document.getElementById("head").innerHTML
  if (test.slice(-4) != "List") {
    document.getElementById("head").innerHTML = title;
  };
}

// Reset title after 1 second
setTimeout(function(){
  resetTitle();
}, 2000);
