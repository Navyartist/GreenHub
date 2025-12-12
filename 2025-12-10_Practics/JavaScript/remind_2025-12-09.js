// filter()
// forEach()

const button = document.getElementById('showEvenButton');

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

const evenNumbers = numbers.filter(number => number % 2 === 0);

button.addEventListener('click', function() {
    console.log(numbers);
    console.log(evenNumbers);}
);