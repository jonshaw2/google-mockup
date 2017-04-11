var x = 5;

function test(){
  setTimeout(function(){
    console.log('logging inside timeout');
    console.log(x);
  }, 2);
}
test();
x = 10;

setTimeout(function(){
  x = 7;
},2);
console.log('doing this first');
console.log(x);
