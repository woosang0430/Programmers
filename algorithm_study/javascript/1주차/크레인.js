/*
    풀이
    *그래프의 열과 행의 개념을 확실히 이해해야한다!*

    1. moves에 있는 원소들을 전부 사용하기 위해 moves로 첫 for문을 돌려준다.
        -> moves의 원소가 뜻 하는 것은 인형 뽑기함의 column의 위치를 의미
    2. 프로그래밍에서 array의 순서는 0부터 시작하기 때문에 moves[i]번째의 값에 1을 빼준다.
    3. 이번엔 인형뽑기함의 크기만큼 for문을 돌려준다. -> row를 의미
    4. 인형뽑기를 위해 열(column)을 고정하고 row의 값을 증가 시키며 0이 아닌 경우를 탐색한다.
        4-1. 0아니면 basket에 인형이 1개 이상 담겨있고 basket의 마지막에 담겨진 인형과 지금 뽑은 인형이 같은지 비교하자
            4-1-1. 만약 basket에 인형이 1개 이상이고 basket의 마지막에 담겨진 인형과 지금 뽑은 인형이 같다면
                basket의 마지막 인형을 빼내고 정답에 2를 더해준다.(현재 뽑은 인형과, basket 마지막에 있는 인형 총 2개)
            4-1-2. 아닌 경우
                basket에 인형을 담아준다.
            인형뽑기에서 뽑은 위치를 0으로 바꿔준다.
        0이 아닌경우에 들어오면 2번째 반복문(row)인 경우는 더이상 탐색할 필요 없으니 break
    5. 첫번째 반복문이 끝나면 answer를 반환
*/

function solution(board, moves) {
    var answer = 0;
    var basket = [];

    for (let i = 0; i < moves.length; i++) {
        var column = moves[i] - 1;
        for (let row = 0; row < board.length; row++) {
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