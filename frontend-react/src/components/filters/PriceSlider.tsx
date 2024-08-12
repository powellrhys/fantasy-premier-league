import './Filters.css'

export default function PriceSlider(
    {maxPrice, handleChange, label} :
    {maxPrice: number, handleChange: any, label: string}
) {
    return (  
        <div className="filter-box">
            <label htmlFor='yaxis' className='label'>{label}</label>
            <input 
                id="PriceSlider"
                type="range"
                min={0}
                max={16}
                step={0.1}
                value={maxPrice}
                onChange={handleChange}
            />
        </div>
    )
}
