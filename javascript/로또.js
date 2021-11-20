function solution(lottos, win_nums) {
    const grades = [6, 6, 5, 4, 3, 2, 1];
    var unkown = 0;
    var min_count = 0;
    
    for (let i = 0; i < lottos.length; i++) {
        if (lottos[i] === 0) {
            unkown += 1;
        } else if (win_nums.includes(lottos[i])) {
            min_count += 1;
        }
    }
    
    var ret = [grades[min_count+unkown], grades[min_count]];
    
    return ret;
}

console.log(solution(
    [44, 1, 0, 0, 31, 25],
    [31, 10, 45, 1, 6, 19]
))