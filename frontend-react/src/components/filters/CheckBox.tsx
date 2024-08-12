export default function CheckBox(
    {items, handleCheckBoxChange} : 
    {items: any, handleCheckBoxChange: any}
 ) {

    const checkbox = items.map((item : any, index: any) =>
        <div key={item.id}>
            <input 
                type='checkbox'
                name={item.position} 
                id={item.index}
                checked={item.checked}
                onChange={handleCheckBoxChange(index)}
            />
            <label htmlFor={item.position}>{item.position}</label>
        </div>
    )

    return (
        <div style={{display : "flex"}}>
            {checkbox}
        </div>
    )
}
