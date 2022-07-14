const sum = (...args) => {
    return args.reduce((a, b) => a + b, 0);
}

console.log(sum(Math.floor(Math.random() * 100), 9, 20));