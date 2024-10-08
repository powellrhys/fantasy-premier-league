import { Chart, registerables, ChartOptions } from 'chart.js';
import {Scatter} from 'react-chartjs-2'
import "./ScatterPlot.css"

export default function ScatterPlot(
    {data, xAxis} : 
    {data : any, xAxis: string}){

    Chart.register(...registerables);
    const plot_data = {datasets: data}

    type MappingType = {
        [key: string]: string;
      };

    const mapping: MappingType = {
        'minutes': 'Minutes',
        'now_cost': 'Price',
        'selected_by_percent': 'Selected by (%)',
        }

    const options: ChartOptions<'scatter'> = {
        plugins: {
            tooltip: {
                callbacks: {
                    label: function (context: any) {
                        const name = context.raw.second_name;
                        const x = context.raw.x;
                        const y = context.raw.y;
                            return `${name}: ${mapping[xAxis]}: ${x}, Points: ${y}`;
                    },
                    title: () => {return 'Summary';}
                },
            },
        },
        maintainAspectRatio: false,
        responsive: true,
        scales: {
            x: {
                type: 'linear',
                position: 'bottom',
                title: {
                    display: true,
                    text: mapping[xAxis],
                },
            },
            y: {
                min: 0,
                title: {
                    display: true,
                    text: 'Points',
                },
            }
        }
    }

    return (
        <div className='charts'>
            <div>
            <Scatter data={plot_data} options={options} />
            </div>
        </div>
    )
}
