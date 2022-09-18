// function
const calculator = {
    add : function (a, b) {
        return a + b;
    },
    minus : function (a, b) {
        return a - b;
    },
    divide : function (a, b) {
        return a / b;
    },
    multiply : function(a, b) {
        return a * b;
    },
    squared : function(a, b) {
        return a ** b;
    }
}

const plusResult = calculator.add(2, 5)

console.log(plusResult)