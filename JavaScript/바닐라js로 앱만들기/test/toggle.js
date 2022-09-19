const h1 = document.querySelector("div.hello:first-child h1");

// toggle은 classList에 해당 class가 있는지 확인해서 만약 있다면, 제거해줌,
// 존재하지 않는다면 classList에 추가해줌.
function handleTitleClick() {
    h1.classList.toggle("clicked") 
}

h1.addEventListener("click", handleTitleClick);