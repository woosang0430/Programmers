function solution(s) {
    const num_en = {zero: 0, one: 1, two: 2, three: 3,four: 4,
                    five: 5, six: 6, seven: 7, eight: 8, nine: 9};
    var word = "";
    var answer = "";
    for (let idx in s) {
        let element = s[idx];
        if (!isNaN(element)) {
            answer += element;
            continue;
        }

        word += element;
        if (Object.keys(num_en).includes(word)) {
            answer += String(num_en[word]);
            word = "";
        }
    }

    return parseInt(answer);
}

solution(
    "one4seveneight"
)