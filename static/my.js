var heading = document.getElementById("head")

function resetTitle() {
  heading.innerHTML = title;
}

let text = heading.innerHTML
// If notification text then show title after 2 seconds
if (text.slice(-4) != "List") {
  setTimeout(function(){
    resetTitle();
  }, 2000);
}
