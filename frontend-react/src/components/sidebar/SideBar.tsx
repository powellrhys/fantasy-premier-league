export default function SideBar(
    {handleChange, filters} :
    {handleChange : any, filters : any}
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
                onChange={handleChange}
                name="yaxis"
                id="yaxis"
                defaultValue={filters[0]}>
                    {options}
            </select>
        </div>
    )
}
