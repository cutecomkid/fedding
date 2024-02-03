function checkPassword() {
    var enteredpassword = document.getElementById("password").value;
    // Check if the entered password is correct
    if (enteredpassword === "iVeL3731$-1!") {
      //redirect to main page
      window.location.href = "/home";
    } else {
      alert("ViLe1337!1-$ ;)");
    }
  }
  
  function joinDiscord() {
    window.location.href = "https://discord.gg/seeking";
  }