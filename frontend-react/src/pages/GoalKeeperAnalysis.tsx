import { useState, useEffect } from 'react'
import BarPlot from '../components/charts/BarPlot';
import SideBar from '../components/sidebar/SideBar';
import '../components/sidebar/SideBar.css'

function GoalKeeperAnalysis() {
  const [plotData, setPlotData] = useState([] as any);
  const [yAxis, setYAxis] = useState('saves')
  const [showFilter, setShowFilter] = useState(true)

  useEffect(() => {

     fetch('http://localhost:8000/players?api_key=wru12!', {  
      headers: {  
        Accept: "application/json"  
      } })
        .then((response) => response.json())
        .then((data) => {
          const listOfDicts = Object.values(data[yAxis]).map((value, index) => ({
            x: Object.values(data.second_name)[index],
            y: value,
            position: Object.values(data.position)[index]
          }));

          // console.log(data)

          const filteredData = listOfDicts.filter(function(item) {
              return item.position == 'Goalkeeper'
            })

          filteredData.sort((a:any, b:any) => b.y - a.y)
          const top_ten = filteredData.slice(0,15)

          // console.log(top_ten)

          const labels = top_ten && top_ten.map(dict => dict.x);
          const values = top_ten && top_ten.map(dict => dict.y);

          const plot_data = [{labels: labels, datasets: [{label: yAxis, data: values}]}]
          // console.log(plot_data)
          
          setPlotData(plot_data)

        })
        .catch((err) => {
           console.log(err.message);
        });
  }, [yAxis]);

  // console.log(plotData)

  const filters = [
    'saves',
    'clean_sheets',
    'goals_conceded',
    'penalties_saved'
  ]

  const handleChange = (e: any) => {
    setYAxis(e.target.value)
  }

  return (
    <>
      <h1>Goalkeeper Analysis</h1>
      <div style={{display: 'flex'}}>
        <div style={{flex: "70%"}}>
          {plotData.length > 0 && <BarPlot data={plotData} stacked={false} />}
        </div>
        <div style={{flex: "30%"}}>
          <SideBar handleChange={handleChange} filters={filters}/>  
        </div>      
      </div>
  </>
  )
}

export default GoalKeeperAnalysis