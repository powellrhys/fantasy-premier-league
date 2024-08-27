import { Chart, registerables } from 'chart.js';
import {Bar} from 'react-chartjs-2'

export default function BarPlot(
    {data, stacked} : 
    {data : any, stacked : boolean}){

    Chart.register(...registerables);

    const options = {
        scales: {
            x: {
              stacked: true,
            },
            y: {
              stacked: true
            }
          }
    }

    return (
        <div className='charts'>
            <Bar data={data[0]} options={options} />
        </div>
    )
}
