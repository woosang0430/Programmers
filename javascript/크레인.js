function solution(board, moves) {
    var answer = 0;
    var basket = [];

    for (let i = 0; i < moves.length; i++) {
        var column = moves[i] - 1;
        for (let row = 0; row < board[0].length; row++) {
            var curr = board[row][column]
            if (curr !== 0) {
                if ((basket.length > 0) && (basket[basket.length-1] === curr)) {
                    basket.pop();
                    answer += 2
                } else {
                    basket.push(curr);
                }
                board[row][column] = 0;
                break;
            }
        }
    }
    return answer;
}

var a = solution(
[
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
],
[1, 5, 3, 5, 1, 2, 1, 4]
);

console.log(a);