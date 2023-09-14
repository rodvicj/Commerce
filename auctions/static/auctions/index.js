document.addEventListener("DOMContentLoaded", function() {
  document.querySelector('select').onchange = () => {
    // document.querySelector("#hello").style.color = this.value;
    console.log(`this value: ${this.value}`);

    // document.querySelector("#hello").style.color = "red";
    return false;
  }

});

  // const buttons = document.querySelectorAll(".nv")
  // // const buttons = Array.prototype.slice.call(btns);
  // buttons.forEach((button) => {
  //   button.onclick = () => {
  //     this.value = "nv nav-link active";
  //     // console.log(`this ${this.value}`);
  //     // alert(`hey you clicked me ${y}`);
  //     // y.className = "nv nav-link active";
  //     return false;
  //   }
  // })
