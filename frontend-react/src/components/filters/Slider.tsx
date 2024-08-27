import './Filters.css'

export default function Slider(
    {
        value,
        handleChange,
        label,
        max_value,
        min_value,
        step_size
    } : {
        value: number,
        handleChange: any,
        label: string,
        max_value: number,
        min_value: number,
        step_size: number
    }
) {
    return (  
        <div className="filter-box">
            <label htmlFor='yaxis' className='label'>{label} - {value}</label>
            <input 
                id="PriceSlider"
                type="range"
                min={min_value}
                max={max_value}
                step={step_size}
                value={value}
                onChange={handleChange}
            />
        </div>
    )
}
