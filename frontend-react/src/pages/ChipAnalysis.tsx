import { useState, useEffect } from 'react'
import BarPlot from '../components/charts/BarPlot';
import SideBar from '../components/sidebar/SideBar';

function ChipAnalysis() {
  const [plotData, setPlotData] = useState([] as any);
  const [leagues, setLeagues] = useState([] as any);
  const [xAxis, setXAxis] = useState('Creigiau CC 2023/24 Season.')

  useEffect(() => {
     fetch('http://localhost:8000/leagues?api_key=wru12!', {  
      headers: {  
        Accept: "application/json"  
      } })
        .then((response) => response.json())
        .then((data) => {
          const uniqueLeagues = [...new Set(Object.values(data.league_name))];
          setLeagues(uniqueLeagues)

          const listOfDicts = Object.values(data.league_name).map((value, index) => ({
            league: value,
            league_rank: Object.values(data.rank_sort)[index],
            player_name: Object.values(data.player_name)[index],
            bench_boost: Object.values(data.bench_boost)[index],
            free_hit: Object.values(data.free_hit)[index],
            triple_c: Object.values(data.triple_c)[index],
          }));
          
          const filteredData = listOfDicts.filter(function(item: any) {
            return item.league == xAxis
          })

          const labels = filteredData && filteredData.map(dict => dict.player_name);

          const plotData = [{
            labels: labels,
            datasets: [
              {
                label: 'Free Hit', 
                data: filteredData && filteredData.map(dict => dict.free_hit)
              },
              {
                label: 'Triple Captain', 
                data: filteredData && filteredData.map(dict => dict.triple_c)
              },
              {
                label: 'Bench Boost', 
                data: filteredData && filteredData.map(dict => dict.bench_boost)
              }
            ]
          }]

          setPlotData(plotData)

        })
        .catch((err) => {
           console.log(err.message);
        });
  }, [xAxis]);

  const handleChange = (e: any) => {
    setXAxis(e.target.value)
  }

  return (
    <>
      <h1>Chip Analysis</h1>
      <div style={{display: 'flex'}}>
        <div style={{flex: "70%"}}>
          {plotData.length > 0 && <BarPlot data={plotData} stacked={true}/>}
        </div>
        <div style={{flex: "30%"}}>
          <SideBar handleChange={handleChange} filters={leagues} />
        </div>
      </div>
  </>
  )
}

export default ChipAnalysis