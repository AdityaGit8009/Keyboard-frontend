const keyboard = document.querySelector(".keyboard-viewport");
const keys = new Map(Array.from(keyboard.querySelectorAll("[data-code]"), (key) => [key.dataset.code, key]));

keyboard.addEventListener("keydown", (event) => {
  keys.get(event.code)?.classList.add("pressed");
});
keyboard.addEventListener("keyup", (event) => {
  keys.get(event.code)?.classList.remove("pressed");
});

function clearPressedKeys() {
  keyboard.querySelectorAll(".pressed").forEach((key) => key.classList.remove("pressed"));
}
keyboard.addEventListener("focusout", (event) => {
  if (!keyboard.contains(event.relatedTarget)) clearPressedKeys();
});
window.addEventListener("blur", clearPressedKeys);
