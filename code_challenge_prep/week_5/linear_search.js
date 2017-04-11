
//linear search
var anArray = [1,3,2,4,6,8,10,9,7,5,5,6,9.5];
var anotherArray = [1,1,2,2,4,5,6,7,8,9,10,11,12,13,14,15,16];
//
// function linear_search(target, unsorted){
//   for (i = 0; i<anArray.length; i++){
//       if (anArray[i] === target){
//           return i;
//       }
//   }
// }
//
// console.log(search = linear_search(anArray,10));

//selection sort

function selection_sort(unsorted){
  for (var i=0; i<unsorted.length;i++){
    var min = unsorted[i];
    var index = i;
    for (var j=i; j<unsorted.length; j++){
      if (unsorted[j] < min){
        min = unsorted[j];
        index = j;
      }
    }
    var temp = unsorted[i];
    unsorted[i]=unsorted[index];
    unsorted[index]=temp;

  }
  return unsorted;
}
console.log(anArray = selection_sort(anArray));


function binary_search(target, unsorted){
  var lower = unsorted.length;
  var upper = 0;
  var currentpoint = Math.floor(unsorted.length/2);
  while (lower !== upper){


    if (unsorted[currentpoint] === target){
      return currentpoint;
    }
    if (target < unsorted[currentpoint]){
      lower = currentpoint;
      currentpoint = Math.floor(lower + ((upper-lower)/2));
    }
    if (target > unsorted[currentpoint]){
      upper = currentpoint;
      currentpoint = Math.floor(upper - ((upper-lower)/2));
    }
  }

}

console.log(binary_search(10, anArray));
console.log(binary_search(10, anotherArray));
