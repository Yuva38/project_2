function renderBarChart(data){
    let col = "Household Income by Race"
    console.log(data[0].data)
    let counties = []
    let houseInc = []

    data[0].data.forEach(function(d){
        counties.push(d.Geography)
        houseInc.push(d[col])
    })

    console.log(houseInc)

    var data = [
        {
          x: counties,
          y: houseInc,
          type: 'bar'
        }
      ];
      
      Plotly.newPlot('bar', data);

}//end of renderBarChart