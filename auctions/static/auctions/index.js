document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("select").onchange = color;
});

function color() {
  document.querySelector("#hello").style.color = this.value;
  console.log(`this.value ${this.value}`);
  return false;
};
