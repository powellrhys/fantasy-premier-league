export function MapDataToAxes(
    data: any,
    xAxis: string,
    yAxis: string
) {
    data.map((item:any) => {
        item.x = item[xAxis];
        item.y = item[yAxis]
    })

    return data
}

export function FilterDataByPrice(
    data: any,
    maxPrice: number
) {
    let filterd_data = data.filter((item: any) => 
        item.now_cost <= maxPrice
      )

    return filterd_data
}

export function GeneratePlayerScatterPlot(data: any) {

    const positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
    const backgroundColorList = ['#04f5ff', '#e90052', '#00ff85', '#38003c']

    const data_array: { label: string; data: any , backgroundColor: string}[] = [];
    for (let i = 0; i < positions.length; i++) {
      const filteredData = data.filter(function(item : any) {
        return item.position == positions[i]
      })

      data_array.push({label: positions[i], data: filteredData, backgroundColor: backgroundColorList[i]})
    }

    return data_array
}

export function TogglePositionData(data:any, positionToggle:any) {

    const joinedList = data.map((user : any) => {
        const userOrders = positionToggle.filter((item:any) => item.position === user.label);

        return {
            ...user,
            checked: userOrders.map((item:any) => item.checked)[0] 
        };
      });

    // New list to hold filtered items
    const activeItems = [];

    // For loop to iterate over the items
    for (let i = 0; i < joinedList.length; i++) {
        // Check if the 'checked' key has a value of true
        if (joinedList[i].checked === true) {
            // Append the item to the new list
            activeItems.push(
                {
                    label: joinedList[i]['label'],
                    data: joinedList[i]['data'],
                    backgroundColor: joinedList[i]['backgroundColor']});
        }
    }

    return activeItems

  }