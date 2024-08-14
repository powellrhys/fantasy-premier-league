import { useState, useEffect } from 'react'
import BarPlot from '../components/charts/BarPlot';
import DropDown from '../components/filters/DropDown';
import Slider from '../components/filters/Slider';
import '../components/sidebar/SideBar.css'

import { CollectPlayerData } from '../functions/FetchDataFunctions';
import {
  MapDataToAxes,
  FiterDataByPosition,
  OrderDatabyMetric,
  CollectTopResults,
  GenerateGoalKepperBarPlot
} from '../functions/TransformDataFunctions';

function GoalKeeperAnalysis() {
  const [plotData, setPlotData] = useState([] as any);
  const [yAxis, setYAxis] = useState('saves' as string)
  const [dataPoints, setDatPoints] = useState(15 as number)
  const [delayedDataPoints, setDelayedDatPoints] = useState(15 as number)
  

  useEffect(() => {
    const handler = setTimeout(() => {
      setDelayedDatPoints(dataPoints);
    }, 200);

    // Cleanup the timeout if value changes within the delay period
    return () => {
      clearTimeout(handler);
    };
  }, [dataPoints]);


  useEffect(() => {

    async function fetchData() {
      let data: any;
      try {
          data = await CollectPlayerData();
          data = MapDataToAxes(data, 'second_name', yAxis)
          data = FiterDataByPosition(data, 'Goalkeeper')
          data = OrderDatabyMetric(data, 'y')
          data = CollectTopResults(data, dataPoints)
          data = GenerateGoalKepperBarPlot(data, yAxis)
          setPlotData(data)
      } catch (err) {
          console.error("Failed to collect player data:", err);
      }
  }
  fetchData()

  }, [yAxis, delayedDataPoints]);

  const filters = [
    'saves',
    'clean_sheets',
    'goals_conceded',
    'penalties_saved'
  ]

  const handleChange = (e: any) => {
    setYAxis(e.target.value)
  }

  const handleSliderChange = (e: any) => {
    setDatPoints(e.target.value)
  }

  return (
    <>
      <h1>Goalkeeper Analysis</h1>
      <div>
        <div style={{display: 'flex', margin: '20px'}}>
          <div style={{flex: 1}}>
              <DropDown 
                  handleXAxisChange={handleChange}
                  filters={filters}
                  label={'Variable'}
              />
            </div>
            <div style={{flex: 1}}>
            <Slider 
              handleChange={handleSliderChange}
              value={dataPoints}
              label={'Number of Data Points'}
              max_value={20}
              min_value={0}
              step_size={1}
            />
          </div>
          </div>
      </div>
      <div>
          {plotData.length > 0 && <BarPlot data={plotData} stacked={false} />}
      </div>
  </>
  )
}

export default GoalKeeperAnalysis