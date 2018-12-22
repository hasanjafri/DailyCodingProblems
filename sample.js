let alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
let phrase = "clutch means drive";
let sum = 0;

let sample_str = 'proliferation';

let sample_array = [1,2,3,3,7,2]
let new_array = []

function() {
    for(var i = -1; abs(i)<sample_str.length; i--) {
        new_array.push(sample_str[i])
        if (sample_str[i] != new_array[abs(i)]) {
            console.log("false")
        }
        console.log("true")
    }
}


for(var i = 0; i<phrase.length; i++) {
    if (alphabets.includes(phrase[i].toUpperCase())) {
        sum += alphabets.indexOf(phrase[i].toUpperCase())
    }
    console.log(sum)
}

for(var i = 0; i<sample_array.length; i++) {
    if (new_array.indexOf(sample_array[i]) === -1) {
        new_array.push(sample_array[i])
    }
    console.log(new_array)
}



