import Slider from '@mui/material/Slider';
import './SideBar.css'

export default function SideBar(
    {
        handleXAxisChange,
        handlePriceRangeChange,
        filters,
        priceRange
    } :
    {
        handleXAxisChange : any,
        handlePriceRangeChange: any,
        filters : any,
        priceRange : any
    }
){

    const options = filters.map((item : any, index: any) =>
        <option 
            key={index}
            value={item}
            className="test">
            {item.replace('_', ' ').toUpperCase()}
        </option>
    )

    return (
        <div style={{flex: "20%"}}>
            <h2>Filters</h2>
            <select 
                className="drop-down"
                onChange={handleXAxisChange}
                name="yaxis"
                id="yaxis"
                defaultValue={filters[0]}>{options}
            </select>
            <div style={{margin: '40px'}}>
                <Slider
                    getAriaLabel={() => 'Minimum distance'}
                    onChange={handlePriceRangeChange}
                    // aria-label="Always visible"
                    value={priceRange} 
                    valueLabelDisplay="on"
                    color='secondary'
                    min={0}
                    max={16}
                    step={0.1}
                    disableSwap
                />
            </div>
        </div>
    )
}
