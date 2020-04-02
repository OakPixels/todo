if (title == true) {
  document.getElementById("count").innerHTML = "^ Enter name and press Start ^";
}

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
