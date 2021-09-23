function showloader() {
    document.getElementById('loader').style.display = "flex";
}

function flashMessage() {
    if ("{{ flash_message }}" == "True") {
      alert("No Name matches in Database");
    }
  }