// const and let
const a = 5; // 변경 불가능
let myName = "KS" // 변경가능

// # Arrays
const daysOfweek = ["mon", "tue", "wed", "thu", "fir", "sat"];

console.log(daysOfweek);

daysOfweek.push("sun");

console.log(daysOfweek);

// # objects
const player ={
  name : "KS",
  points : 10,
  fat : true
}

console.log(player);
player.lastName = "S";
player.points = 15;
player.points = player.points + 1;
console.log(player)