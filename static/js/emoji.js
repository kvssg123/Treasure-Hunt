// const container=document.getElementById("container")
// let e = 1;
//     let f = 1;
//     let c = 1;
//     function navigateToGoogle() {
//                 window.location.href = 'https://www.google.com';
//     }
//     for (let i = 1; i <= 15; i++) {
//     for (let j = 1; j <= 15; j++) {
//         let d = Math.floor(Math.random() * 100) + 1;
//         if(i > 8  &&  j > 5 &&  d % 6 == 0 && c == 1){
//         //document.write('<button class="button" onclick="navigateToGoogle()"></button>');
//         c--;
//         }
//         else if (d % 6 == 5 && e == 1){
//         //document.write('<button class="buttonb"></button>');
//         e--;
//         }
//         else if(d % 6 == 2 && f == 1)
//         {
//         //document.write('<button class="buttonc"></button>');
//         f--;
//         }
//         else if(d % 5 == 0)
//         //document.write('<button class="button1"></button>');
//         else if(d % 5 == 1)
//         //document.write('<button class="button2"></button>');
//         else if(d % 5 == 2)
//         //document.write('<button class="button4"></button>');
//         else if(d % 5 == 3)
//         //document.write('<button class="button5"></button>');
//         else if(d % 5 == 4)
//         //document.write('<button class="button6"></button>');
//         }
//     //document.write('<br>');
//     }
// }

// $(document).ready(function() {
//     $('.button').click(function() {
//       var row = $(this).data('row');
//       var col = $(this).data('col');
//       $.post('/update_count/', {'row': row, 'col': col}, function(data) {
//         $('#count').text(data.count);
//       });
//     });
//   });



// working

// const grid = document.getElementById("grid");
// let a=1,b=2;
// document.getElementById('my-hidden-input-row').value = a.toString();
// document.getElementById('my-hidden-input-col').value = b.toString();
// for (let i = 0; i < 15; i++) {
//   for (let j = 0; j < 15; j++) {
//     console.log("hi")
//     const button = document.createElement("button");
//     button.id = `button-${i}-${j}`;
//     grid.appendChild(button);
//     var buttonid=`button-${i}-${j}`
//     var myButton=document.getElementById(buttonid)
//     if(i==j) myButton.className="button1";
//     else myButton.className="button2";
//     const buttonclass=myButton.className;
//     console.log(buttonclass)
//     button.addEventListener("click", handleClick);
   
//     // var url1='../images/left.png';
//     // document.getElementById(button.id).style.backgroundImage=url1;
   

//   }
// }

// function handleClick(event) {
//   const button = event.target;
//   console.log(`Button clicked: ${button.id}`);
// }

// wprtlodjf  


const grid = document.getElementById("grid");
let a=1,b=2;
let e = 1;
    let f = 1;
    let c = 1;
console.log(document.getElementById('my-hidden-input-col').value)
for (let i = 0; i < 15; i++) {
  for (let j = 0; j < 15; j++) {
    const button = document.createElement("button");
    button.class = button;
    button.id = `button-${i}-${j}`;
    button.addEventListener("click", handleClick);
    grid.appendChild(button);
    var buttonid=`button-${i}-${j}`
    var myButton=document.getElementById(buttonid);
    let d = Math.floor(Math.random() * 100) + 1;
        if(i > 8  &&  j > 5 &&  d % 6 == 0 && c == 1){
        // document.write('<button class="button" onclick="navigateToGoogle()"></button>');
         
         myButton.className="button2";
         let a1=i+1,b1=j+1
         document.getElementById('my-hidden-input-row').value = a1.toString();
         document.getElementById('my-hidden-input-col').value = b1.toString();
        c--;
        }
        else if (d % 6 == 5 && e == 1){
        //document.write('<button class="buttonb"></button>');
        myButton.className="button1";
        

        // button.style.backgroundImage = "url('hunt/static/images/left.png')";
        e--;
        }
        else if(d % 6 == 2 && f == 1)
        {
          myButton.className="button3";
          // button.style.backgroundImage = "url('hunt/static/images/left.png')";
        //document.write('<button class="buttonc"></button>');
        f--;
        }
        else if(d % 6 == 0){ myButton.className="button4";}
        //document.write('<button class="button1"></button>');
        else if(d % 6 == 1) { myButton.className="button5";}
        //document.write('<button class="button2"></button>');
        else if(d % 6 == 2){ myButton.className="button6";}
        //document.write('<button class="button4"></button>');
        else if(d % 6 == 3) { myButton.className="button7";}
        //document.write('<button class="button5"></button>');
        else if(d % 6 == 4){ myButton.className="button8";}
        //document.write('<button class="button6"></button>');
        else if(d % 6 == 5){ myButton.className="button9";}
   
       

  }
}

function handleClick(event) {
  const button = event.target;
  console.log(`Button clicked: ${button.id}`);
}

  

