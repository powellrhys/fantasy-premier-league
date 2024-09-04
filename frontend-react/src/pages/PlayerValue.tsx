import { useState, useEffect } from 'react'

import Slider from '../components/filters/Slider';
import ScatterPlot from '../components/charts/ScatterPlot';
import DropDown from '../components/filters/DropDown';
import CheckBox from '../components/filters/CheckBox';

import {
  CollectPlayerData,
  CollectAPICredentials
} from '../functions/FetchDataFunctions';
import {
  MapDataToAxes,
  FilterDataByPrice,
  GeneratePlayerScatterPlot,
  TogglePositionData
} from '../functions/TransformDataFunctions';

function PlayerValue() {

  const positions = [
    {id: 1, position: 'Goalkeeper', checked: true},
    {id: 2, position: 'Defender', checked: true},
    {id: 3, position: 'Midfielder', checked: true},
    {id: 4, position: 'Forward', checked: true}
  ]

  const [plotData, setPlotData] = useState([] as any);
  const [xAxis, setXAxis] = useState('minutes')
  const [maxPrice, setMaxPrice] = useState(16 as number)
  const [delayedPriceRange, setdelayedPriceRange] = useState(16 as number)
  const [positionToggle, setPositionToggle] = useState(positions as any)

  useEffect(() => {
    const handler = setTimeout(() => {
      setdelayedPriceRange(maxPrice);
    }, 200);

    // Cleanup the timeout if value changes within the delay period
    return () => {
      clearTimeout(handler);
    };
  }, [maxPrice]);

  useEffect(() => {
    async function fetchData() {
      let data: any;
      let endpoint_credentials: any
      try {
          endpoint_credentials = await CollectAPICredentials()
          data = await CollectPlayerData(endpoint_credentials);
          data = MapDataToAxes(data, xAxis, 'total_points')
          data = FilterDataByPrice(data, maxPrice)
          data = GeneratePlayerScatterPlot(data)
          data = TogglePositionData(data, positionToggle)
          setPlotData(data)
      } catch (err) {
          console.error("Failed to collect player data:", err);
      }
  }
  fetchData()

  }, [xAxis, delayedPriceRange, positionToggle]);

  const handleXAxisChange = (e: any) => {
    setXAxis(e.target.value)
  }

  const handlePriceChange = (e: any) => {
    setMaxPrice(e.target.value)
  }

const handleCheckBoxChange = (index : any) => (event : any) => {
  const newPositions = [...positionToggle]
  newPositions[index]['checked'] = !positionToggle[index]['checked']
  setPositionToggle(newPositions)
};


  const filters = [
    'minutes',
    'now_cost',
    'selected_by_percent'
  ]

  return (
    <>
      <h1>Outfield Player Analysis</h1>
      <div>
        <div style={{display: 'flex', margin: '20px'}}>
          <div style={{flex: 1}}>
            <DropDown 
              handleXAxisChange={handleXAxisChange}
              filters={filters}
              label={'Variable'}
            />
          </div>
          <div style={{flex: 1}}>
            <Slider 
              handleChange={handlePriceChange}
              value={maxPrice}
              label={'Maximum Price'}
              max_value={16}
              min_value={0}
              step_size={0.1}
            />
          </div>
          <div style={{flex: 1}}>
            <CheckBox 
              items={positionToggle}
              handleCheckBoxChange={handleCheckBoxChange} />
          </div>
        </div>
        <div>
          <ScatterPlot data={plotData} xAxis={xAxis}/>
        </div>
      </div>
  </>
  )
}

export default PlayerValue
