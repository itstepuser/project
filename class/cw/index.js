const myFunc = async function() {
    setTimeout(() => {
        console.log(1234);

    }, 100);
}

myFunc().then(result => {console.log("Success!")}).catch(result => console.log("ERROR"));
console.log("This");

try {
    let a = 5;
    fsdfsd;
}
catch (error) {
    console.log(a);
}