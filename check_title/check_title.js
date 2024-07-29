let checkTitle = function (text) {
    const splitText = text.split(" ");

    let result = true;
    console.log(text);
    for (let word of splitText) {

        if (word[0] == word.toUpperCase()[0]) {
            result = true;
        } else {
            result = false;
            break;
        }
    }
    console.log(result);
}


let test_cases = [
    "A Mind Boggling Achievement",
    "A Simple C++ Program!",
    "Water is Transparent",
];

for (let t of test_cases) {
    checkTitle(t);
}