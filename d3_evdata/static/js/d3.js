


  d3.json("http://localhost:5000/api/Stations").then( data => {
    // console.log(data);
// 
    renderHeatMap(data)
// 
    // renderMarkers(data)

    // plotting chropleth, it has to be called only once
    renderChoropleth() 
    d3.json("http://localhost:5000/api/Income").then( data => {
      renderBarChart(data)
    })
    
    
})
