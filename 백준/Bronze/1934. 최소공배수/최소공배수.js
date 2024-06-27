const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', (line) => {
    input.push(line);
});

rl.on('close', () => {
    let T = parseInt(input[0]);
    
    for (let i = 1; i <= T; i++) {
        let [A, B] = input[i].split(' ').map(Number);
        
        let lcm = getLCM(A, B);
        console.log(lcm);
    }
});

// 최대공약수를 구하는 함수 (유클리드 호제법 사용)
function getGCD(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// 최소공배수를 구하는 함수
function getLCM(a, b) {
    return a * (b / getGCD(a, b));
}
