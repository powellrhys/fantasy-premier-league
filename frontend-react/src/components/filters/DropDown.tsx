import './Filters.css'

export default function DropDown(
    {
        handleXAxisChange,
        filters,
        label
    } :
    {
        handleXAxisChange : any,
        filters : any
        label : string
    }
){

    const options = filters.map((item : any, index: any) =>
        <option 
            key={index}
            value={item}
        >
            {item.replace('_', ' ').toUpperCase()}
        </option>
    )

    return (
        <div className="filter-box">
            <label htmlFor='yaxis' className='label'>{label}</label>
            <select 
                className="drop-down"
                onChange={handleXAxisChange}
                name="yaxis"
                id="yaxis"
                defaultValue={filters[0]}>{options}
            </select>
        </div>

    )
}
