document.addEventListener("DOMContentLoaded", () => {
  // document.querySelector("select").onchange = function () {
  //   console.log(`this.value ${this.value}`);
  //   document.querySelector("#hello").style.color = this.value;
  //   color();
  // };

  document.querySelector("select").onchange = color;
});

function color() {
// const color = (this) => {
  document.querySelector("#hello").style.color = this.value;
  console.log(`this.value ${this.value}`);
  return false;
};
//   document.querySelector("#hello").style.color = this.value;
// }

// document.querySelector('#compose').onclick = compose_email;

// // function for sending an email
// document.querySelector('#compose-form').onsubmit = function() {
//   send_mail();
//   return false;
// };
