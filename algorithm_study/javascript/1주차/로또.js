/*
    풀이

    lottos안의 원소들을 순회하며
    lottos의 원소가 0인 경우(unknown)와 win_nums 배열에 포함되는 경우(min_count)로 나누어 카운트한다.

    모르는 값(unknown)과 맞은 값(min_count)을 더한 값 -> 최고 점수
    맞은 값(min_count) -> 최소 점수

    획득한 점수를 grades의 index로 접근한다.
*/

function solution(lottos, win_nums) {
    const grades = [6, 6, 5, 4, 3, 2, 1];
    var unknown = 0;
    var min_count = 0;
    
    for (let i = 0; i < lottos.length; i++) {
        if (lottos[i] === 0) {
            unknown += 1;
        } else if (win_nums.includes(lottos[i])) {
            min_count += 1;
        }
    }
    
    var ret = [grades[min_count+unknown], grades[min_count]];
    
    return ret;
}

console.log(solution(
    [44, 1, 0, 0, 31, 25],
    [31, 10, 45, 1, 6, 19]
))
