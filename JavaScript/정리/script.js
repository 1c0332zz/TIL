function createParagraph() {
  const para = document.createElement('p');
  para.textContent = 'You clicked the button!';
  document.body.appendChild(para);
}

const buttons = document.querySelectorAll('button');

for (const button of buttons) {
  button.addEventListener('click', createParagraph);
}


// 이 방법으로 사용하면 하나하나 html에 js코드를 넣어줘야함. 
// onclick="createParagraph()" 방법으로

// function createParagraph() {
//   const para = document.createElement('p');
//   para.textContent = 'You clicked the button!';
//   document.body.appendChild(para);
// }

