const search = (arr, toSearch) {
    for (let val of arr){
        if (val == toSearch) {
            return val
        }
    }
    return -1;
}

const arr = [1, 3, 6, 8, 10];
const result = search(arr, 8);
if (result > -1) {
    console.log('finded {$result}')
} else {
    console.log('not finded')
}
