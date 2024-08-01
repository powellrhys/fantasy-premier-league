import { useState, useEffect } from 'react'
import ScatterPlot from '../components/charts/ScatterPlot';
import SideBar from '../components/sidebar/SideBar';

function PlayerValue() {
  const [plotData, setPlotData] = useState([] as any);
  const [xAxis, setXAxis] = useState('minutes')

  useEffect(() => {
     fetch('http://localhost:8000/players?api_key=wru12!', {  
      headers: {  
        Accept: "application/json"  
      } })
        .then((response) => response.json())
        .then((data) => {
          const listOfDicts = Object.values(data[xAxis]).map((value, index) => ({
            x: value,
            y: Object.values(data.total_points)[index],
            position: Object.values(data.element_type)[index],
            second_name: Object.values(data.second_name)[index]
          }));

          const data_array: { label: string; data: any }[] = [];
          const element_types = Object.values(data.element_type) as number[]
          for (let i = 1; i <= Math.max(...element_types); i++) {
            const filteredData = listOfDicts.filter(function(item) {
              return item.position == i
            })

            type MappingType = {
              [key: number]: string;
            };

            const mapping: MappingType = {
              1: 'GoalKeeper',
              2: 'Defender',
              3: 'Midfielder',
              4: 'Forward'
            }

            data_array.push({label: mapping[i], data: filteredData})
          }
          setPlotData(data_array)

        })
        .catch((err) => {
           console.log(err.message);
        });
  }, [xAxis]);

  const handleChange = (e: any) => {
    setXAxis(e.target.value)
  }

  const filters = [
    'minutes',
    'now_cost',
    'selected_by_percent'
  ]

  return (
    <>
      <h1>Outfield Player Analysis</h1>
      <div style={{display: 'flex'}}>
        <div style={{flex: "70%"}}>
          <ScatterPlot data={plotData} xAxis={xAxis}/>
        </div>
        {/* <div style={{flex: "20%"}}> */}
          <div style={{flex: "30%"}}>
            <SideBar handleChange={handleChange} filters={filters}/>  
          </div>   
      </div>
  </>
  )
}

export default PlayerValue