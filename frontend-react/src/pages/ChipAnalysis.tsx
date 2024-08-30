import { useState, useEffect } from 'react'
import BarPlot from '../components/charts/BarPlot';
import DropDown from '../components/filters/DropDown';

import {
  CollectLeagueData,
  CollectAPICredentials
} from '../functions/FetchDataFunctions';
import { 
  FilterDataByLeague,
  GenerateChipAnalysisPlot 
} from '../functions/TransformDataFunctions';

function ChipAnalysis() {
  const [plotData, setPlotData] = useState([] as any);
  const [leagues, setLeagues] = useState([] as any);
  const [xAxis, setXAxis] = useState('' as string)
  const [password, setPassword] = useState('' as string)

  useEffect(() => {

    async function fetchData() {
      let data: any;
      let endpoint_credentials: any;
      try {

        endpoint_credentials = await CollectAPICredentials(password);

        if (endpoint_credentials.authenticated) {
          data = await CollectLeagueData(endpoint_credentials);
          setLeagues([...new Set(data.map((item: any) => item.league_name))]);
          data = FilterDataByLeague(data, xAxis)
          const labels = data && data.map((item:any) => item.player_name);
          data = GenerateChipAnalysisPlot(data, labels)
          setPlotData(data)
        }
      } catch (err) {
          console.error("Failed to collect player data:", err);
      }
  }
  fetchData()

  }, [xAxis, password]);

  const handleChange = (e: any) => {
    setXAxis(e.target.value)
  }

  return (
    <>
      <h1>Chip Analysis</h1>
      <div style={{display: 'flex', margin: '20px'}}>
        <div style={{flex: 1}}>
          <DropDown 
              handleXAxisChange={handleChange}
              filters={leagues}
              label={'Variable'}
            />
        </div>
        <div style={{flex: 1}}>
          <form>
            <div>
              <label>Password:</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
          </form>
        </div>
      </div>
      <div>
          {plotData.length > 0 && <BarPlot data={plotData} stacked={true}/>}
      </div>
  </>
  )
}

export default ChipAnalysis
