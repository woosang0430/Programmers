/*
    풀이
    
    key, value 꼴로 number_english object를 정의한다.
    word 변수 => 숫자가 아닌 원소를 담아둘 변수
    answer => 숫자이거나 숫자로 변환한 값을 담을 변수

    1. s의 원소를 한 개씩 순회하며 숫자인 문자열일 경우 바로 answer에 붙여준다.
        - 만약 숫자로 붙여진 경우 남은 구문을 돌면 word에 문자열 숫자가 붙기 때문에 continue로 넘겨주자
    2. 숫자가 아닌 경우 word에 차곡차곡 붙여준다.
    3. 만약 word가 object의 key들에 포함되어 있는 경우
        - word에 맞는 숫자로 변환하여 answer에 붙여준다.
        - word는 다시 ""값으로 초기화 한다.
    4. 숫자로 반환하기 위해 parseInt()를 사용하여 반환!

    새로 알게된 점
    - js에서 문자열을 for문으로 돌리면 각 원소가 반환되는 것이 아닌 index가 반환된다.
    - js에서는 python과 같이 다양한 문자열 내장함수가 제공되지 않는다...역시 python..
    - 문자열이지만 숫자인 경우 (ex. a = "1") python의 경우 a.isdigit()을 사용하면 되지만 js의 경우는 까다롭게 처리해야된다..
        그나마 찾은 방법 isNaN 메소드는 문자열로된 숫자를 넣으면 false를 반환하는 것을 이용하자! 
        or parseInt(value, format)으로 사용 -> format에는 진수 표기(ex. 2, 10)진수
*/

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