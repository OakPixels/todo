function resetTitle() {
  if (document.getElementById("head").innerHTML != "My ToDo List") {
    document.getElementById("head").innerHTML = "My ToDo List";
  };
}

// Reset title after 1 second
setTimeout(function(){
  resetTitle();
}, 1000);
