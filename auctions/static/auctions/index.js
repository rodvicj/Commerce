document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".nv");
  buttons.forEach((button) => {
    button.onclick = function () {
      console.log(this.className);
      // this.className + "active";
      return false;
    };
  });
});
