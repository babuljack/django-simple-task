setTimeout(function(){

    let msg=document.getElementById('message');
    msg.style.display='none';
  },1000);




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

  