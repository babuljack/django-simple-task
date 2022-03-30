/*
===============================
 Message timeout
 ==============================
 */
setTimeout(function(){
    let msg=document.getElementById('message');
    msg.style.display='none';
  },1000);



/*
===============================
Graph resizing.
 ==============================
 */
  var graph;
  var chart
  document.onreadystatechange = function () {
      if (document.readyState == 'interactive') {
          graph = document.getElementById("graph");
          chart = document.getElementById("myChart");
          
          maintainRatio()
      }
  }
  
function maintainRatio() {
      var w = graph.clientWidth
      var h = (w * 9) / 16
      console.log({ w, h });
      graph.height = h
      chart.style.maxHeight = h + "px"
  }
  window.onresize = maintainRatio;


  /*
===============================
Drag and drops
 ==============================
 */


let drags=document.getElementsByClassName('draging');
let items=document.getElementsByClassName('drag-item');


for(let i=0;i<items.length;i++){
    items[i].addEventListener('dragleave',function(){
        var html=items[i]
        drags[i].addEventListener('dragover', (e) => {
            e.preventDefault();
           });
         
          drags[i].addEventListener('drop', (e) => {
            let value=html.getAttribute('data');
            fetch('/delete/'+value)
            .then(response => response.json())
            .then(function(data){
                  if(data.status=='success'){
                     html.style.display='none';
                  }      
            })
           

           });
        
        
    })
}

/* 
for (drag of drags){


    drag.addEventListener('dragover', (e) => {
        e.preventDefault();
    });

    drag.addEventListener('drop', (e) => {
        console.log(e.target)
        console.log(e)
       
    })

}
 */
 

